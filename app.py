from flask import Flask, render_template, request, jsonify
from chat import gpt_model, gpt16k

app = Flask(__name__)

@app.route("/")
@app.route("/gpt")
def gpt():
    return render_template('chat.html')

@app.route("/gpt16k")
def gpt16k():
    return render_template('chat.html')

@app.route("/llama2")
def llama2():
    return render_template('chat.html')


import re
@app.route("/ask", methods=['POST'])
def ask():

    message = str(request.form['messageText'])
    model_type = request.form.get('model_type')
    bot_response = ""
    print(model_type)
    if model_type == '/gpt16K' :
        bot_response = gpt16k(message) 
    else:
        bot_response = gpt_model(message) 
    # print(bot_response)
    output_string = re.sub(r"```\w+\s(.*?)```", r"<code onclick='copyCode(this)'>\1</code>", bot_response, flags=re.DOTALL)

    # print(output_string)
    # print(len(parts), parts)
    return jsonify({'status':'OK','answer':output_string})


if __name__ == "__main__":
    app.run()