from machinetranslation import translator
from flask import Flask, render_template, request
import json
import machinetranslation

app = Flask("Web Translator")

@app.route("/englishToFrench")
def englishToFrench():
    textToTranslate = request.args.get('textToTranslate')
    return machinetranslation.translator.englishtofrench(textToTranslate)            

@app.route("/frenchToEnglish")
def frenchToEnglish():
    textToTranslate = request.args.get('textToTranslate')
    return machinetranslation.translator.frenchtoenglish(textToTranslate)

@app.route("/")
def renderIndexPage():
        return render_template('index.html')
if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080)
