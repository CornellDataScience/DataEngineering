from flask import Flask, Response
from kafka import KafkaConsumer

consumer = KafkaConsumer('demo-topic', group_id = 'view', bootstrap_servers = "[0.0.0.0:9092]")

app = Flask(__name__)
@app.route('/')

def index():
    return Response(kafkastream(), mimetype = "multipart/x-mixed-replace; boundary = frame")

def kafkastream():
    for msg in consumer:
        yield (b'--frame\r\n'b'Content-Type: image/png\r\n\r\n + msg.value
        + b'\r\n\r\n')

if __name__ == "__main__":
    app.run(host = "0.0.0.0", debug = True)