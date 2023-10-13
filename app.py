from gingerit import GingerIt
import pandas as pd
from flask import Flask, render_template, request, jsonify
from gingerit import GingerIt
#from gingerit.gingerit import GingerIt
from chat import chatbot

app = Flask(__name__)


@app.route("/")
def hello():
    return render_template('chat.html')


@app.route("/ask", methods=['POST'])
def ask():
    """
    message = str(request.form['messageText'])
    # Handle the grammar correction
    parser = GingerIt()
    corrected_text = parser.parse(message)
    print(corrected_text['result'])
    
    bot_response = chatbot(corrected_text['result']) 
    # print(bot_response)
    return jsonify({'status':'OK','answer':bot_response})
    
    """
    message = str(request.form['messageText'])
    
    
    bot_response = chatbot(message) 
    # print(bot_response)
    return jsonify({'status':'OK','answer':bot_response})
    

if __name__ == "__main__":
    #app.run()
    app.run(host='0.0.0.0', port=8080)
    