# Main entry for the E-Commerce AI Assistant
# Choose Flask or Streamlit for the interface

import os
from dotenv import load_dotenv
from flask import Flask, render_template, request, session
from utils.openai_utils import ask_question, ask_question_with_history, summarize_text, generate_image
from utils.responsible_ai import filter_inappropriate_content, get_privacy_notice, log_transparency

# Load environment variables
load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("FLASK_SECRET_KEY", "supersecretkey")

@app.route('/', methods=['GET', 'POST'])
def index():
    response = None
    image_url = None
    feature = 'qa'
    if request.method == 'POST':
        user_input = request.form.get('user_input')
        feature = request.form.get('feature')
        if not filter_inappropriate_content(user_input):
            response = "Input contains inappropriate content."
        else:
            if feature == 'qa':
                response = ask_question(user_input)
            elif feature == 'summarize':
                response = summarize_text(user_input)
            elif feature == 'image':
                image_url = generate_image(user_input)
                response = "Image generated below."
            log_transparency(feature, user_input)
    privacy_notice = get_privacy_notice()
    return render_template('index.html', response=response, image_url=image_url, feature=feature, privacy_notice=privacy_notice)

@app.route('/chat', methods=['GET', 'POST'])
def chat():
    if 'chat_history' not in session:
        session['chat_history'] = []
    chat_history = session['chat_history']
    bot_response = None
    if request.method == 'POST':
        user_message = request.form.get('user_message')
        if user_message:
            chat_history.append({'role': 'user', 'content': user_message})
            # Use all previous messages for context
            bot_reply = ask_question_with_history(chat_history)
            chat_history.append({'role': 'assistant', 'content': bot_reply})
            session['chat_history'] = chat_history
            bot_response = bot_reply
    return render_template('chatbot.html', chat_history=chat_history, bot_response=bot_response)

if __name__ == "__main__":
    app.run(debug=True)
    print("running app")
#added new features
