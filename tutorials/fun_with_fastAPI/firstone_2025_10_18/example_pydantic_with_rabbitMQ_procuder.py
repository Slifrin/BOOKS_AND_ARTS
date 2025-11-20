import pika

from pydantic import BaseModel, EmailStr


class User(BaseModel):
    id: int
    name: str
    email: EmailStr


connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
channel = connection.channel()
QUEUE_NAME = "user_queue"
channel.queue_declare(queue=QUEUE_NAME)


def push_to_queue(user_data: User) -> None:
    serialized_data = user_data.model_dump_json()
    channel.basic_publish(
        exchange="",
        routing_key=QUEUE_NAME,
        body=serialized_data,
    )
    print(f"Added to queue: {serialized_data}")


user1 = User(id=1, name="John Doe", email="john@example.com")
user2 = User(id=2, name="Jane Doe", email="jane@example.com")

push_to_queue(user1)
push_to_queue(user2)

connection.close()
