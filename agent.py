import os
import logging
from typing import Dict, List, Any, Iterator
from datetime import datetime
import pytz

from google.cloud import aiplatform
from langchain_community.vectorstores import FAISS
from langchain_google_vertexai import VertexAIEmbeddings, VertexAI
from langchain.prompts import PromptTemplate
from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory
from langchain.schema import Document

# Configurações do Google Cloud
PROJECT_ID = os.environ.get("GOOGLE_CLOUD_PROJECT", "ccdsiaa")
LOCATION = os.environ.get("GOOGLE_CLOUD_LOCATION", "us-central1")

# Caminho para o índice FAISS local
try:
    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
except NameError:
    SCRIPT_DIR = os.getcwd()
INDEX_PATH = os.path.join(SCRIPT_DIR, "rag_project", "models", "faiss_index")

# Configuração de logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class RAGTool:
    """Ferramenta para recuperação e geração de respostas utilizando RAG com memória e streaming."""

    def __init__(self) -> None:
        self.embeddings: VertexAIEmbeddings
        self.vector_index: FAISS
        self.llm: VertexAI
        self.rag_chain: ConversationalRetrievalChain
        self.memory: ConversationBufferMemory
        self.prompt_template: PromptTemplate
        self.retriever = None
        self.initialized = False

    def _get_current_datetime(self) -> str:
        """Retorna a data e hora atual formatada em português brasileiro."""
        tz = pytz.timezone("America/Sao_Paulo")
        now = datetime.now(tz)
        months = [
            "janeiro", "fevereiro", "março", "abril", "maio", "junho",
            "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"
        ]
        weekdays = [
            "segunda-feira", "terça-feira", "quarta-feira", "quinta-feira",
            "sexta-feira", "sábado", "domingo"
        ]
        month_name = months[now.month - 1]
        weekday_name = weekdays[now.weekday()]
        return f"{weekday_name}, {now.day} de {month_name} de {now.year}, {now.hour:02d}:{now.minute:02d}"  

    def initialize(self) -> None:
        """Inicializa os componentes da ferramenta RAG."""
        if self.initialized:
            return

        logger.info("Inicializando a ferramenta RAG...")
        
        
        print("Data/hora atual:", self._get_current_datetime())

        # Embeddings e índice vetorial
        self.embeddings = VertexAIEmbeddings(
            model_name="text-embedding-004",
            project=PROJECT_ID,
            location=LOCATION
        )
        try:
            self.vector_index = FAISS.load_local(
                INDEX_PATH,
                self.embeddings,
                allow_dangerous_deserialization=True
            )
            logger.info(f"Índice vetorial carregado de {INDEX_PATH}")
        except Exception as e:
            logger.error(f"Erro ao carregar o índice vetorial: {e}")
            raise

        # Prompt e memória
        template = (
          """
          Você é o "Guia UTFPR-CM", o assistente virtual especialista da UTFPR, Câmpus Campo Mourão. Sua personalidade é amigável, inteligente e prestativa, como um membro experiente da equipe da universidade pronto para ajudar.
          Sua missão é fornecer respostas diretas, claras e úteis aos alunos, transformando as informações do CONTEXTO em uma conversa natural e não em uma simples extração de texto.
          **Princípios para suas respostas:**
          1.  **Tom Natural e Pessoal:** Fale como uma pessoa, não como um robô. Use uma linguagem amigável e acessível. Cumprimente o aluno apenas na primeira mensagem da conversa. Nas seguintes, vá direto ao ponto.
          2.  **Inteligência e Precisão:** Sua base de conhecimento é o CONTEXTO. Use-o para formular uma resposta precisa e completa à pergunta do aluno. Seja direto e conciso. Evite rodeios e informações que não foram solicitadas. Se a pergunta incluir informações de contexto temporal (entre colchetes), considere sempre essas informações para dar respostas contextualizadas (ex: prazos, períodos letivos, etc.).
          3.  **Honestidade e Proatividade:** Se a resposta não estiver no CONTEXTO, admita que não tem a informação específica no momento. Por exemplo: "Não encontrei os detalhes sobre X aqui, mas posso te ajudar a encontrar." Sempre que não tiver a resposta, seja proativo. Indique o melhor caminho para o aluno, sugerindo o contato com o departamento correto (DERAC, coordenação de curso, etc.) para obter a informação.
          4.  **Didática e Clareza:** Organize a informação de forma lógica. Use listas e parágrafos curtos para que a resposta seja fácil de entender.
          5.  **Honestidade e Limites:** Se a pergunta for sobre algo que não está no CONTEXTO, como questões pessoais ou opiniões, responda de forma educada, mas firme, que não pode ajudar com isso. Por exemplo: "Desculpe, não posso ajudar com questões pessoais ou opiniões." ou "Não tenho informações sobre isso, mas posso ajudar com outras questões relacionadas à UTFPR-CM."
          ---
          **DATefrA/HORA ATUAL:**
          {current_datetime}
          ---
          **CONTEXTO:**
          {context}
          ---
          **PERGUNTA DO ALUNO:**
          {question}
          ---
          **RESPOSTA (COMO GUIA UTFPR-CM):**
          """
        )
        self.prompt_template = PromptTemplate(
            template=template,
            input_variables=["current_datetime", "context", "question"]
        )

        self.memory = ConversationBufferMemory(
            memory_key="chat_history", 
            return_messages=True,
            output_key="answer"
        )

        # Retriever reutilizável
        self.retriever = self.vector_index.as_retriever(
            search_type="similarity",
            search_kwargs={"k": 5}
        )

        # Cadeia RAG para chamadas sem streaming
        self.llm = VertexAI(
            model_name="gemini-2.5-flash",
            max_output_tokens=1024,
            temperature=0.2,
            top_p=0.8,
            top_k=40,
            project=PROJECT_ID,
            location=LOCATION,
            streaming=True
        )
        self.rag_chain = ConversationalRetrievalChain.from_llm(
            llm=self.llm,
            retriever=self.retriever,
            memory=self.memory,
            return_source_documents=True,
            combine_docs_chain_kwargs={"prompt": self.prompt_template}
        )

        self.initialized = True
        logger.info("Ferramenta RAG inicializada com sucesso.")

    def answer_question(self, question: str) -> Dict[str, Any]:
        """Responde a uma pergunta (sem streaming)."""
        if not self.initialized:
            self.initialize()

        logger.info(f"Processando pergunta: {question}")
        timestamped = f"[Contexto temporal: {self._get_current_datetime()}] {question}"

        result = self.rag_chain.invoke({"question": timestamped})

        sources = []
        for doc in result.get("source_documents", []):
            src = doc.metadata.get("source", "Desconhecida")
            if src not in sources:
                sources.append(src)

        return {"resposta": result["answer"], "fontes": sources}

    def answer_question_stream_generator(self, question: str) -> Iterator[str]:
        """
        Responde a uma pergunta em streaming real, token a token.
        """
        if not self.initialized:
            self.initialize()

        # 1) Recupera documentos
        docs: List[Document] = self.retriever.get_relevant_documents(question)
        context = "\n\n".join(doc.page_content for doc in docs)

        # 2) Prepara prompt
        prompt = self.prompt_template.format(
            current_datetime=self._get_current_datetime(),
            context=context,
            question=question
        )

        # 3) Stream dos tokens
        for token in self.llm.stream(prompt):
            yield token

    def clear_history(self) -> None:
        """Limpa o histórico da conversa."""
        if self.memory:
            self.memory.clear()
            logger.info("Histórico da conversa limpo.")


# Instância global e funções de interface
rag_tool = RAGTool()

def query_knowledge_base(question: str) -> Iterator[str]:
    return rag_tool.answer_question_stream_generator(question)


def clear_conversation_history() -> None:
    rag_tool.clear_history()


# Exemplo de uso
if __name__ == "__main__":
    print("=== Teste de streaming ===")
    for t in query_knowledge_base("Como faço matrícula?"):
        print(t, end="", flush=True)
    print()
