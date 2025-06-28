<div id="top" >
<div align="center" >

# GUIA-UTFPR

<em>Melhorando a Navegação no Campus Através de Conversas Inteligentes</em>

<!-- BADGES -->
<img src="https://img.shields.io/github/license/marrielly/Guia-UTFPR?style=flat&logo=opensourceinitiative&logoColor=white&color=0080ff" alt="license">
<img src="https://img.shields.io/github/last-commit/marrielly/Guia-UTFPR?style=flat&logo=git&logoColor=white&color=0080ff" alt="last-commit">
<img src="https://img.shields.io/github/languages/top/marrielly/Guia-UTFPR?style=flat&color=0080ff" alt="repo-top-language">
<img src="https://img.shields.io/github/languages/count/marrielly/Guia-UTFPR?style=flat&color=0080ff" alt="repo-language-count">

<em>Construído com as ferramentas e tecnologias:</em>

<img src="https://img.shields.io/badge/LangChain-1C3C3C.svg?style=flat&logo=LangChain&logoColor=white" alt="LangChain">
<img src="https://img.shields.io/badge/Python-3776AB.svg?style=flat&logo=Python&logoColor=white" alt="Python">
<img src="https://img.shields.io/badge/pandas-150458.svg?style=flat&logo=pandas&logoColor=white" alt="pandas">

</div>
<br/>

---

## 📄 Índice

- [Visão Geral](https://www.google.com/search?q=%23-vis%C3%A3o-geral)
- [Começando](https://www.google.com/search?q=%23-come%C3%A7ando)
  - [Pré-requisitos](https://www.google.com/search?q=%23-pr%C3%A9-requisitos)
  - [Instalação](https://www.google.com/search?q=%23-instala%C3%A7%C3%A3o)
  - [Uso](https://www.google.com/search?q=%23-uso)
  - [Testes](https://www.google.com/search?q=%23-testes)
- [Recursos](https://www.google.com/search?q=%23-recursos)
- [Estrutura do Projeto](https://www.google.com/search?q=%23-estrutura-do-projeto)
  - [Índice do Projeto](https://www.google.com/search?q=%23-%C3%ADndice-do-projeto)
- [Licença](https://www.google.com/search?q=%23-licen%C3%A7a)

---

## ✨ Visão Geral

O Guia-UTFPR é uma ferramenta de desenvolvedor inovadora que combina interfaces web e de mensagens para fornecer informações precisas e em tempo real sobre o campus por meio de técnicas avançadas de geração aumentada por recuperação. Ele permite interações de usuário fluidas, tornando o conhecimento do campus acessível e envolvente.

**Por que o Guia-UTFPR?**

Este projeto visa aprimorar a acessibilidade às informações do campus com chatbots e interfaces web alimentados por IA. Os principais recursos incluem:

- 🧩 **🔍 Geração aumentada por recuperação:** Utiliza a ingestão de documentos e a busca vetorial para melhorar a relevância das respostas.
- 🚀 **🌐 Interface web interativa:** Oferece uma plataforma envolvente para os usuários fazerem perguntas sobre o campus e os serviços da UTFPR-CM.
- 📱 **🤖 Chatbot do Telegram:** Oferece assistência instantânea e acessível por meio de um aplicativo de mensagens popular.
- ⚙️ **☁️ Integração com IA na nuvem:** Suporta implantação escalável com o Google Cloud Vertex AI e LangChain.
- 📝 **🧹 Gerenciamento de conversas:** Inclui a limpeza do histórico para uma experiência de usuário tranquila.

---

## 📌 Recursos

|     | Componente              | Detalhes                                                                                                                                                                                                                                                         |
| :-- | :---------------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ⚙️  | **Arquitetura**         | <ul><li>Design modular que separa o processamento de dados, a inferência do modelo e os componentes da UI</li><li>Usa notebooks Jupyter para experimentação e prototipagem</li><li>Potencial arquitetura em camadas integrando serviços de IA na nuvem</li></ul> |
| 🔩  | **Qualidade do Código** | <ul><li>Segue as melhores práticas de Python com clara separação de funções</li><li>Usa `requirements.txt` para gerenciamento de dependências</li><li>Comentários de código e docstrings presentes nos módulos principais</li></ul>                              |
| 📄  | **Documentação**        | <ul><li>README básico com visão geral do projeto e instruções de configuração</li><li>Inclui lista de dependências e exemplos de uso</li><li>Nenhuma documentação extensa de API ou de desenvolvedor observada</li></ul>                                         |
| 🔌  | **Integrações**         | <ul><li>Integra-se com o Google Cloud Vertex AI via `langchain-google-vertexai`</li><li>Usa o Gradio para implantação da UI</li><li>Inclui integração com bot do Telegram com `python-telegram-bot`</li><li>Utiliza o pandas para manipulação de dados</li></ul> |
| 🧩  | **Modularidade**        | <ul><li>Scripts/notebooks separados para ingestão de dados, inferência de modelo e UI</li><li>Utiliza componentes do LangChain para encadear fluxos de trabalho de IA</li><li>A abordagem modular facilita a extensão e a personalização</li></ul>               |
| 🧪  | **Testes**              | <ul><li>Nenhum framework de teste explícito ou scripts de teste identificados</li><li>Potencial dependência da experimentação em notebooks</li></ul>                                                                                                             |
| ⚡️ | **Desempenho**          | <ul><li>Usa serviços de IA na nuvem para inferência escalável</li><li>Emprega o Gradio para uma UI leve, reduzindo a carga local</li><li>Potencial gargalo no processamento de dados baseado em notebook</li></ul>                                               |
| 🛡️  | **Segurança**           | <ul><li>Nenhuma medida de segurança explícita documentada</li><li>Usa chaves de API ou credenciais provavelmente armazenadas em variáveis de ambiente</li></ul>                                                                                                  |
| 📦  | **Dependências**        | <ul><li>Gerenciadas via `requirements.txt`</li><li>As principais dependências incluem: `google-cloud-aiplatform`, `langchain`, `gradio`, `python-telegram-bot`, `pandas`</li></ul>                                                                               |

---

## 📁 Estrutura do Projeto

```sh
└── Guia-UTFPR/
    ├── LICENCE
    ├── agent.py
    ├── interface.py
    ├── rag.ipynb
    ├── rag_project
    │   └── data
    ├── requirements.txt
    └── telegram_bot.py
```

---

### 📑 Índice do Projeto

 <details open >
 <summary > <b > <code >GUIA-UTFPR/ </code > </b > </summary >
 <details >
 <summary > <b >**root** </b > </summary >
 <blockquote >
 <div class='directory-path' style='padding: 8px 0; color:  #666;' >
 <code > <b >⦿ **root** </b > </code >
 <table style='width: 100%; border-collapse: collapse;' >
 <thead >
 <tr style='background-color:  #f8f9fa;' >
 <th style='width: 30%; text-align: left; padding: 8px;' >Nome do Arquivo </th >
 <th style='text-align: left; padding: 8px;' >Resumo </th >
 </tr >
 </thead >
 <tr style='border-bottom: 1px solid  #eee;' >
 <td style='padding: 8px;' > <b > <a href='[https://github.com/marrielly/Guia-UTFPR/blob/master/interface.py](https://github.com/marrielly/Guia-UTFPR/blob/master/interface.py)' >interface.py </a > </b > </td >
 <td style='padding: 8px;' >- Fornece uma interface web interativa para um chatbot baseado em conhecimento, permitindo que os usuários façam perguntas sobre o campus e os serviços da UTFPR-CM <br >- Facilita interações de usuário fluidas, exibe respostas em tempo real e inclui funcionalidade para limpar o histórico de conversas, apoiando uma experiência envolvente e amigável dentro da arquitetura geral do sistema. </td >
 </tr >
 <tr style='border-bottom: 1px solid  #eee;' >
 <td style='padding: 8px;' > <b > <a href='[https://github.com/marrielly/Guia-UTFPR/blob/master/telegram_bot.py](https://github.com/marrielly/Guia-UTFPR/blob/master/telegram_bot.py)' >telegram_bot.py </a > </b > </td >
 <td style='padding: 8px;' >- Implementa um chatbot do Telegram que serve como um guia interativo do campus, tratando as perguntas dos usuários consultando uma base de conhecimento e gerenciando o histórico de conversas <br >- Facilita o engajamento do usuário por meio de comandos de ajuda e limpeza de histórico, fornecendo respostas em tempo real às perguntas, melhorando assim a acessibilidade e o suporte às informações do campus. </td >
 </tr >
 <tr style='border-bottom: 1px solid  #eee;' >
 <td style='padding: 8px;' > <b > <a href='[https://github.com/marrielly/Guia-UTFPR/blob/master/rag.ipynb](https://github.com/marrielly/Guia-UTFPR/blob/master/rag.ipynb)' >rag.ipynb </a > </b > </td >
 <td style='padding: 8px;' >- O arquivo  <code >rag.ipynb </code > serve como o script de orquestração principal para o pipeline de Geração Aumentada por Recuperação (RAG) dentro do projeto <br >- Seu objetivo principal é carregar, processar e preparar dados textuais de um diretório especificado, transformando documentos brutos em um armazenamento vetorial estruturado e otimizado para recuperação eficiente <br >- Essa configuração permite que o sistema utilize fontes de conhecimento externas durante as interações com o modelo de linguagem, aprimorando a precisão e a relevância das respostas geradas <br >- No geral, este notebook facilita a integração da ingestão de documentos, divisão de texto, geração de embeddings e armazenamento vetorial, formando a etapa fundamental para a construção de um sistema robusto de perguntas e respostas aumentado por recuperação dentro da arquitetura mais ampla. </td >
 </tr >
 <tr style='border-bottom: 1px solid  #eee;' >
 <td style='padding: 8px;' > <b > <a href='[https://github.com/marrielly/Guia-UTFPR/blob/master/LICENCE](https://github.com/marrielly/Guia-UTFPR/blob/master/LICENCE)' >LICENCE </a > </b > </td >
 <td style='padding: 8px;' >- Define os termos de licenciamento e as permissões de uso para todo o projeto de software, garantindo clareza legal e direitos de distribuição adequados <br >- Estabelece a estrutura sob a qual o software pode ser livremente usado, modificado e compartilhado, apoiando a colaboração de código aberto e salvaguardando os direitos dos autores <br >- Esta licença sustenta a arquitetura aberta e acessível do projeto. </td >
 </tr >
 <tr style='border-bottom: 1px solid  #eee;' >
 <td style='padding: 8px;' > <b > <a href='[https://github.com/marrielly/Guia-UTFPR/blob/master/agent.py](https://github.com/marrielly/Guia-UTFPR/blob/master/agent.py)' >agent.py </a > </b > </td >
 <td style='padding: 8px;' >- Implementa um sistema de Geração Aumentada por Recuperação (RAG) que utiliza busca por similaridade vetorial e modelos de linguagem grandes para fornecer respostas precisas e com reconhecimento de contexto <br >- Integra recuperação de documentos, memória conversacional e capacidades de streaming para facilitar interações dinâmicas e naturais, servindo principalmente como um assistente virtual inteligente para a comunidade da UTFPR-CM. </td >
 </tr >
 <tr style='border-bottom: 1px solid  #eee;' >
 <td style='padding: 8px;' > <b > <a href='[https://github.com/marrielly/Guia-UTFPR/blob/master/requirements.txt](https://github.com/marrielly/Guia-UTFPR/blob/master/requirements.txt)' >requirements.txt </a > </b > </td >
 <td style='padding: 8px;' >- Facilita a integração dos componentes do Google Cloud Vertex AI e LangChain para permitir fluxos de trabalho escaláveis e orientados por IA <br >- Suporta a implantação fluida de modelos de linguagem, processamento de dados e interfaces de interação do usuário dentro da arquitetura mais ampla <br >- Garante que todas as dependências necessárias sejam instaladas para o desenvolvimento e execução eficientes de aplicativos alimentados por IA que utilizam aprendizado de máquina baseado em nuvem e ferramentas de conversação. </td >
 </tr >
 </table >
 </blockquote >
 </details >
 </details >

---

## 🚀 Começando

### 📋 Pré-requisitos

Este projeto requer as seguintes dependências:

- **Linguagem de Programação:** Python
- **Gerenciador de Pacotes:** Pip

### ⚙️ Instalação

Compile o Guia-UTFPR a partir do código-fonte e instale as dependências:

1.  **Clone o repositório:**

    ```sh
    ❯ git clone https://github.com/marrielly/Guia-UTFPR
    ```

2.  **Navegue até o diretório do projeto:**

    ```sh
    ❯ cd Guia-UTFPR
    ```

3.  **Instale as dependências:**

**Usando [pip](https://pypi.org/project/pip/):**

```sh
❯ pip install -r requirements.txt
```

### 💻 Uso

Execute o projeto com:

**Usando [pip](https://pypi.org/project/pip/):**

```sh
python {ponto_de_entrada}
```

### 🧪 Testes

O Guia-utfpr usa o framework de testes {**framework_de_teste**}. Execute a suíte de testes com:

**Usando [pip](https://pypi.org/project/pip/):**

```sh
pytest
```

---

## 📜 Licença

O Guia-utfpr está protegido sob a Licença [LICENÇA](https://choosealicense.com/licenses). Para mais detalhes, consulte o arquivo [LICENÇA](https://choosealicense.com/licenses/).

---

 <div align="left" > <a href=" #top" >⬆ Voltar </a > </div >

---
