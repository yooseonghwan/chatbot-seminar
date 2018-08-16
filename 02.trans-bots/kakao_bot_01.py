from flask import Flask
from flask import request
from flask import jsonify
from flask import json
from googletrans import Translator

import logging

app = Flask(__name__)


@app.route("/keyboard", methods=["GET"])
def keyboard():
    return jsonify(type="text")


@app.route("/message", methods=["POST"])
def message():
    data = json.loads(request.data)
    content = data["content"]
    translator = Translator()
    #translated = translator.translate(content, dest="ko", src="en")
    translated = translator.translate(content, dest="en", src="auto")
    translated2 = translator.translate(content, dest="fr", src="auto")
    translated3 = translator.translate(content, dest="ja", src="auto")    
    translated4 = translator.translate(content, dest="ko", src="auto")    
    translated5 = translator.translate(content, dest="zh-tw", src="auto")
    
    translated6 = translator.translate(content, dest="it", src="auto")   
    translated7 = translator.translate(content, dest="th", src="auto")  
    translated8 = translator.translate(content, dest="hi", src="auto")  
    translated9 = translator.translate(content, dest="ru", src="auto")  
    translated10 = translator.translate(content, dest="es", src="auto")
    translated10 = translator.translate(content, dest="vi", src="auto")
    
    response = {
        "message": {
           "text":"[Korean]:"+translated4.text + 
            "\n\n[English]:"+translated.text +         
            "\n\n[French]:"+translated2.text +
            "\n\n[Japanese]:"+translated3.text +
            "\n\n[Chinese]:"+translated5.text +
            "\n\n[Italian]:"+translated6.text +
            "\n\n[Thai]:"+translated7.text +
            "\n\n[Hidi]:"+translated8.text +
            "\n\n[Rusia]:"+translated9.text +
            "\n\n[Spanish]:"+translated10.text +
            "\n\n[vietnamese]:"+translated10.text
            
        }
    }

    response = json.dumps(response, ensure_ascii=False)
    return response


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
