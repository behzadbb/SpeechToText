import pika
from SpeechToText import SpeechToText
import pandas as pd
import json

class CallCenter:
    def lineQueueInitiator(self, lines):
        connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
        channel = connection.channel()
        
        for line in lines:
            channel.queue_declare(queue=line)
            
        channel.close()

    def pushToQueue(self, line, data):
        connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
        channel = connection.channel()
        channel.basic_publish(exchange='', routing_key=line, body=data)

    def getFromQueue(self, line):
        print("\n\n_____________\n\n\n\n\ngetFromQueue:\n\n")
        connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
        channel = connection.channel()
        
        def callback(ch, method, properties, body):
            ssaw = body.decode('utf-8')
            ssssss = json.loads(ssaw)
            _tempData = pd.read_json(body,)
            nnn = _tempData["VoiceData"]
            stt = SpeechToText()
            text = stt.speechToText(nnn)
            print(text)
            
        channel.basic_consume(queue=line, auto_ack=True, on_message_callback=callback)

        channel.start_consuming()
        return "0"