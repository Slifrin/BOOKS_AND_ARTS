import asyncio
import sys

from typing import Any

from arq import create_pool, ArqRedis
from arq.connections import RedisSettings

from pydantic import BaseModel, EmailStr


class User(BaseModel):
    id: int
    name: str
    email: EmailStr


REDIS_SETTINGS = RedisSettings()


async def process_user(ctx: dict[str, Any], user_data: dict[str, Any]) -> None:
    user = User.model_validate(user_data)
    print(f"Processing user: {user}")


async def enqueue_jobs(redis: ArqRedis):
    user1 = User(id=1, name="John Doe", email="john@example.com")
    user2 = User(id=2, name="Jane Doe", email="jane@example.com")

    await redis.enqueue_job("process_user", user1.model_dump())
    print(f"Enqueued user: {repr(user1)}")

    await redis.enqueue_job("process_user", user2.model_dump())
    print(f"Enqueued user: {repr(user2)}")


class WorkerSettings:
    functions = [process_user]
    redis_settings = REDIS_SETTINGS


async def main():
    redis = await create_pool(REDIS_SETTINGS)
    await enqueue_jobs(redis)


if __name__ == "__main__":
    asyncio.run(main())
