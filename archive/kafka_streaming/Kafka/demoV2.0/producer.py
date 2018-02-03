from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json

access_token = "936766436772663297-lDZ1AyP3z6NiZ1L0qQLQdo5PQXW6VZR"
access_token_secret = "NY1x4ZIdTjBDgfMAIgknz1urSPE3AZK2tDPEwyXIl3ovS"
consumer_key = "7Dzvyp5IKeB0dgj9wdcBEP2Fi"
consumer_secret = "eTxZwEydglZeQIZguMiYcaQokRzNA04MG1mOY2uwEwMEZhxNd9"
topic = ""


class StdOutListener(StreamListener):

    def on_data(self, data):
        parsed_data = json.loads(data)
        formated_data = parsed_data["user"]["screen_name"]
        print(formated_data)
        #print(data)
        #producer.send_messages(topic, formated_data.encode('utf-8'))
        return True

    def on_error(self, status):
        print status


if __name__ == '__main__':
    #kafka = KafkaClient("localhost:9092")
    #producer = SimpleProducer(kafka)
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)
    stream.filter(track=['pokemon', 'kafka', 'zelda', 'christmas', 'politics', 
    'memes', 'mathematics', 'elon musk'])
