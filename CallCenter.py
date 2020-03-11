import pika
from SpeechToText import SpeechToText
import base64

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
            _tempData = base64.b64decode(body)
            stt = SpeechToText()
            text = stt.speechToText(_tempData)
            print("\n",text,"\n")
            
        channel.basic_consume(queue=line, auto_ack=True, on_message_callback=callback)

        channel.start_consuming()