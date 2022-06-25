import pika

def producer():

    # define the parameters
    url = 'localhost'
    params = pika.ConnectionParameters(host=url)
    connect = pika.BlockingConnection(params)

    channel = connect.channel()
    # I declare the name of the queue
    channel.queue_declare(queue="my_queue")
    # define the message
    my_message = input("Type your message: ")
    # The exchange is used to specify the queue that you want to send the messages
    # routing_key also contains the queue name
    # send the message to the queue
    channel.basic_publish(exchange='', routing_key="my_queue", body=my_message)
    # flush the messages and send
    connect.close()


def main():

    producer()

main()