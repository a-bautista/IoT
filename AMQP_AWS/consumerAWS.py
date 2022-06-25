from basicClient import BasicPikaClient
from dotenv import load_dotenv
import os
import time

class BasicMessageReceiver(BasicPikaClient):

    def get_message(self, queue):
        method_frame, header_frame, body = self.channel.basic_get(queue)
        if method_frame:
            print(method_frame, header_frame, body)
            self.channel.basic_ack(method_frame.delivery_tag)
            return method_frame, header_frame, body
        else:
            print('No message returned')

    def close(self):
        self.channel.close()
        self.connection.close()


if __name__ == "__main__":

    load_dotenv()
    BROKER_ID = os.getenv("BROKER_ID")
    USERNAME = os.getenv("USERNAME")
    PASSWORD = os.getenv("PASSWORD")
    REGION = os.getenv("REGION")

    # Create Basic Message Receiver which creates a connection
    # and channel for consuming messages.
    basic_message_receiver = BasicMessageReceiver(
        BROKER_ID,
        USERNAME,
        PASSWORD,
        REGION
    )

    while True:
        try:
            # keep the queue waiting for 2 seconds
            time.sleep(2)
            # Consume the message that was sent.
            basic_message_receiver.get_message("iot_eq_48")
        except KeyboardInterrupt:
            # Close connections.
            print("Closing connection")
            basic_message_receiver.close()
