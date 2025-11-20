import sys

import pika
import pika.channel
import pika.spec

from pydantic import BaseModel, EmailStr


class User(BaseModel):
    id: int
    name: str
    email: EmailStr


def main() -> None:
    print(f"Hello main from : {__file__} executed by {sys.executable}")

    connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
    channel = connection.channel()
    QUEUE_NAME = "user_queue"
    channel.queue_declare(queue=QUEUE_NAME)

    def process_message(
        ch: pika.channel.Channel,
        method: pika.spec.Basic.Deliver,
        properties: pika.spec.BasicProperties,
        body: bytes,
    ):
        user = User.model_validate_json(body)
        print(f"Validate user: {repr(user)}")
        ch.basic_ack(delivery_tag=method.delivery_tag)

    channel.basic_consume(queue=QUEUE_NAME, on_message_callback=process_message)
    channel.start_consuming()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass
