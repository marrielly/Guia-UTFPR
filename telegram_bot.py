# telegram_bot.py
import os
import telebot
from agent import (
    query_knowledge_base,
    clear_conversation_history
)
import time

TELEGRAM_BOT_TOKEN = "7841263841:AAGqzmObb8VaDwXQKrmZ_OIdAAdfm6aRnns"

if not TELEGRAM_BOT_TOKEN:
    print("Erro: O token do bot do Telegram não foi encontrado.")
    print("Por favor, configure a variável de ambiente TELEGRAM_BOT_TOKEN.")
    exit()

# Inicializa o bot
bot = telebot.TeleBot(TELEGRAM_BOT_TOKEN)

print("Bot do Telegram 'Guia UTFPR-CM' iniciado...")
print("Aguardando mensagens...")

user_sessions = {} 

@bot.message_handler(commands=['start', 'ajuda'])
def send_welcome(message):
    """
    Handler para os comandos /start e /ajuda.
    Envia uma mensagem de boas-vindas e instruções.
    """
    welcome_text = (
        "🎓 Olá! Eu sou o Guia UTFPR-CM, seu assistente para tudo sobre o campus.\n\n"
        "Você pode me perguntar sobre:\n"
        "✔️ Como funciona o RU\n"
        "✔️ Acessar a versão digital do seu RA\n"
        "✔️ Prazos importantes do semestre\n"
        "✔️ Como solicitar documentos\n"
        "✔️ Onde fica a coordenação do seu curso\n\n"
        "E muito mais! É só mandar sua pergunta.\n\n"
        "Para limpar o nosso histórico de conversa e começar de novo, use o comando /limpar."
    )
    bot.reply_to(message, welcome_text)

@bot.message_handler(commands=['limpar'])
def handle_clear_history(message):
    """
    Handler para o comando /limpar.
    Chama a função para limpar o histórico da conversa.
    """
    try:
        clear_conversation_history()
        
        bot.reply_to(message, "🗑️ Nosso histórico de conversa foi limpo! Podemos começar de novo.")
        print(f"Histórico limpo para o chat ID: {message.chat.id}")
    except Exception as e:
        bot.reply_to(message, f"Ocorreu um erro ao tentar limpar o histórico: {str(e)}")
        print(f"Erro ao limpar histórico para o chat ID {message.chat.id}: {e}")

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    """
    Handler para todas as outras mensagens de texto.
    Processa a pergunta usando o agente e envia a resposta.
    """
    question = message.text
    chat_id = message.chat.id
    
    print(f"Recebida pergunta de {message.from_user.first_name} (ID: {chat_id}): \"{question}\"")
    
    if not question.strip():
        bot.reply_to(message, "Por favor, digite uma pergunta.")
        return

    thinking_message = bot.reply_to(message, "🤔 Pensando...")

    response_text = ""
    try:
        stream = query_knowledge_base(question)
        for token in stream:
            response_text += token
        
        if response_text:
            bot.edit_message_text(chat_id=chat_id, message_id=thinking_message.message_id, text=response_text)
            print(f"Resposta enviada para o chat ID {chat_id}.")
        else:
            bot.edit_message_text(chat_id=chat_id, message_id=thinking_message.message_id, text="Não consegui encontrar uma resposta para isso.")
            print(f"Nenhuma resposta encontrada para o chat ID {chat_id}.")

    except Exception as e:
        error_message = f"😕 Desculpe, ocorreu um erro ao processar sua pergunta: {str(e)}"
        bot.edit_message_text(chat_id=chat_id, message_id=thinking_message.message_id, text=error_message)
        print(f"Erro ao processar pergunta para o chat ID {chat_id}: {e}")

if __name__ == "__main__":
    try:
        bot.polling(none_stop=True)
    except Exception as e:
        print(f"O bot parou devido a um erro: {e}")
        time.sleep(10)

