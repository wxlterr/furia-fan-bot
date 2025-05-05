from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def home():
    return "Bot da FURIA está rodando!"

def keep_alive():
    t = Thread(target=lambda: app.run(host='0.0.0.0', port=8080))
    t.start()
