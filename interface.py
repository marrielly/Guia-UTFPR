import gradio as gr
from agent import query_knowledge_base, clear_conversation_history

print("Preparando a interface conversacional do Gradio...")

def chatbot_interaction(message, history):
    """
    Função que lida com a interação do chatbot.
    Recebe a mensagem do usuário e retorna a resposta do agente.
    """
    if not message:
        yield "Por favor, digite uma pergunta."
        return
    
    # Usar o streaming simples para obter tokens
    response = ""
    try:
        for token in query_knowledge_base(message):
            response += token
            yield response
    except Exception as e:
        yield f"Erro ao processar a pergunta: {str(e)}"

def clear_chat():
    """
    Função para ser chamada pelo botão de limpar.
    Ela chama a função do agente que limpa a memória.
    """
    clear_conversation_history()
    return None

with gr.Blocks() as demo:
    gr.Markdown(
        """
        # Guia UTFPR-CM
        Tá perdido(a) na UTFPR-CM? Relaxa, o guia tá aqui pra isso! 
        
        Pergunta o que quiser sobre o campus, os serviços, a vida de estudante e muito mais.
        """
    )
    
    # O componente principal do chatbot
    chatbot = gr.Chatbot(label="Conversa")
    
    # O ChatInterface gerencia a interação do chatbot
    chat_iface = gr.ChatInterface(
        fn=chatbot_interaction,
        chatbot=chatbot,
        examples=[
            ["Como funciona o RU?"],
            ["Como posso acessar a versão digital do RA?"],
        ],
        title=None,
        description=None,
    )

    # Botão customizado para limpar o histórico do agente
    clear_btn = gr.Button("🗑️ Limpar Conversa")
    # Ao clicar no botão, a função clear_chat é chamada, que por sua vez chama clear_conversation_history
    # e também limpa o componente do chatbot na interface.
    clear_btn.click(fn=clear_chat, outputs=[chatbot])

# Lança a interface
if __name__ == "__main__":
    print("Interface pronta! Acesse o link local no seu navegador.")
    demo.launch(share=False)
