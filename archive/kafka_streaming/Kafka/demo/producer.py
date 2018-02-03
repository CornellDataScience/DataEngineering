import time
import cv2
from kafka import SimpleProducer, KafkaClient

kafka = KafkaClient('localhost:9092')
producer = SimpleProducer(kafka)

topic = "demo-topic"

def vid_stream(mov):
    video = cv2.VideoCapture(mov)
    print('We are streaming......')

    while(mov.isOpened):
        val, dat = mov.read()

        if not val:
            break
        val2, img = cv2.imencode('.png', dat)

        producer.send_messages(topic, img.tobytes())
        time.sleep(0.5)

    video.release()
    print("Finished streaming vid")

    if __name__ == "__main__":
        vid_stream('video.mp4')
        