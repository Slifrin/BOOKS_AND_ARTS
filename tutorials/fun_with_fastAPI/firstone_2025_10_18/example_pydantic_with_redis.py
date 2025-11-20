import redis

from pydantic import BaseModel, EmailStr


class User(BaseModel):
    id: int
    name: str
    email: EmailStr


r = redis.Redis(host="localhost", port=6379, db=0)
QUEUE_NAME = "user_queue"


def push_to_queue(user_data: User) -> None:
    serialized_data = user_data.model_dump_json()
    r.rpush(QUEUE_NAME, serialized_data)
    print(f"Added to queue: {serialized_data}")


user1 = User(id=1, name="John Doe", email="john@example.com")
user2 = User(id=2, name="Jane Doe", email="jane@example.com")

push_to_queue(user1)
push_to_queue(user2)

print("-" * 50)


def pop_from_queue() -> None:
    data = r.lpop(QUEUE_NAME)

    if data:
        user = User.model_validate_json(data)
        print(f"Validated user: {repr(user)}")
    else:
        print(f'Queue "{QUEUE_NAME}" is empty')


pop_from_queue()
pop_from_queue()
pop_from_queue()
