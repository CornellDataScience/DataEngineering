from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json
import io
import avro.datafile
import avro.io
import avro.ipc
import avro.schema
from time import sleep

access_token = 
access_token_secret = 
consumer_key = 
consumer_secret = 
topic = "data_raw"


SCHEMA = avro.schema.parse(
    json.dumps(
        {"namespace": "avro",
        "type": "record",
        "name":"Twit",
        "fields": [
            {"name": "created_at", "type": "string"},
            {"name": "id", "type": "long"},
            {"name": "text", "type": "string"},
            {"name": "location", "type": "string"},
            {"name": "name", "type": "string"}
        ]
        }
    )
)


class StdOutListener(StreamListener):


    def on_data(self, data):
        parsed_data = json.loads(data)
        if(parsed_data["created_at"]!=None):
            created = parsed_data["created_at"]
            print created
        else:
            created = "Not Available"

        if(parsed_data["id"]!=None):
            id_num = parsed_data["id"]
            print id_num
        else:
            id_num = 0

        if(parsed_data["text"]!=None):
            text = parsed_data["text"]
            print text
        else:
            text = "No Text"

        if(parsed_data["user"]["location"]!=None):
            location = parsed_data["user"]["location"]
            print location
        else:
            location = "Not Available"

        if(parsed_data["user"]["screen_name"]!= None):
            screen_name = parsed_data["user"]["screen_name"]
            print screen_name
        else:
            screen_name = "Not Available"

        message = {
            "created_at": created,
            "id": id_num,
            "text": text,
            "location": location,
            "name": screen_name
        }

        buf = io.BytesIO()
        writer = avro.datafile.DataFileWriter(buf, avro.io.DatumWriter(), SCHEMA)
        writer.append(message)
        writer.flush()
        buf.seek(0)
        output_data = buf.read()

        producer.send_messages(topic, output_data.encode('utf-8'))
        print(output_data)
        print("Sent!!!")
        sleep(.5)
        return True

    def onError(self, status):
        print status


if __name__ == '__main__':
    kafka = KafkaClient("localhost:9092")
    producer = SimpleProducer(kafka)
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)
    stream.filter(track = ['Christmas'])
   

