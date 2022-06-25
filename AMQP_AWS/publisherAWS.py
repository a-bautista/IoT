from basicClient import BasicPikaClient
# read the environment variables
from dotenv import load_dotenv
import os

class BasicMessageSender(BasicPikaClient):

    def declare_queue(self, queue_name):
        print(f"Trying to declare queue({queue_name})...")
        self.channel.queue_declare(queue=queue_name)

    def send_message(self, exchange, routing_key, body):
        channel = self.connection.channel()
        channel.basic_publish(exchange=exchange,
                              routing_key=routing_key,
                              body=body)
        print(f"Sent message. Exchange: {exchange}, Routing Key: {routing_key}, Body: {body}")

    def close(self):
        self.channel.close()
        self.connection.close()

if __name__ == "__main__":

    # Initialize Basic Message Sender which creates a connection
    # and channel for sending messages.
    load_dotenv()
    BROKER_ID = os.getenv("BROKER_ID")
    USERNAME = os.getenv("USER_AWS")
    PASSWORD = os.getenv("PASSWORD")
    REGION = os.getenv("REGION")


    basic_message_sender = BasicMessageSender(
        BROKER_ID,
        USERNAME,
        PASSWORD,
        REGION
    )

    # Declare a queue
    basic_message_sender.declare_queue("iot_eq_48")

    # define your message
    message = input("Type in your message: ")
    # Send a message to the queue.
    basic_message_sender.send_message(exchange="", routing_key="iot_eq_48", body=message)

    # Close connections.
    basic_message_sender.close()