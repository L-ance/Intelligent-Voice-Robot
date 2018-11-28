from geventwebsocket.handler import WebSocketHandler
from gevent.pywsgi import WSGIServer
from geventwebsocket.websocket import WebSocket

from uuid import uuid4

from flask import Flask, render_template, request, send_file

import baidudashazi

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/ws")
def ws():
    user_socket = request.environ.get("wsgi.websocket")  # type: WebSocket
    while 1:
        audio_file = user_socket.receive()
        file_name = uuid4()
        with open(f"{file_name}.wav", "wb") as f:
            f.write(audio_file)
        text = baidudashazi.audio2text(f"{file_name}.wav")
        filename = baidudashazi.my_nlp(text)
        print(filename, type(filename))
        user_socket.send(filename)


@app.route("/get_audio/<filename>")
def get_audio(filename):
    return send_file(filename)


if __name__ == '__main__':
    # app.run()
    http_serv = WSGIServer(("0.0.0.0", 5003), app, handler_class=WebSocketHandler)
    http_serv.serve_forever()
