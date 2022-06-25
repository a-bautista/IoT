import pika, os

# class MyCallback():
#     def callback(self, ch, method, properties, body):
#         print("Message received: %r" % body.decode())

def consumer():
    url = 'localhost'
    parameters = pika.ConnectionParameters(host=url)
    connection = pika.BlockingConnection(parameters)
    channel = connection.channel()
    channel.queue_declare(queue="my_queue")

    def callback(ch, method, properties, body):
        print(" [x] Received %r" % body)

    channel.basic_consume(queue="my_queue", on_message_callback=callback)
    channel.start_consuming()

def main():

    consumer()

main()