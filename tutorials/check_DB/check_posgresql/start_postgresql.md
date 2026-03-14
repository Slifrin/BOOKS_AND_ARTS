# Starting postgresql

Article

https://oneuptime.com/blog/post/2026-01-17-postgresql-docker-persistence/view


Start container with named volume

```bash

docker run -d \
  --name postgres-dev \
  -e POSTGRES_USER=devuser \
  -e POSTGRES_PASSWORD=devpassword \
  -e POSTGRES_DB=myapp \
  -p 5432:5432 \
  -v first_pgdata:/var/lib/postgresql/data \
  postgres:latest

```

Connect to started container

```bash
docker exec -it postgres-dev psql -U devuser -d myapp
```

Local volume

```bash

docker run -d \
  --name postgres-dev \
  -e POSTGRES_USER=devuser \
  -e POSTGRES_PASSWORD=devpassword \
  -e POSTGRES_DB=myapp \
  -p 5432:5432 \
  -v ./check_pgdata:/var/lib/postgresql/data \
  postgres:latest

```

Simpler setup 

```bash
docker run --name=db -e POSTGRES_PASSWORD=secret -d -v postgres_data:/var/lib/postgresql postgres:18

docker exec -ti db psql -U postgres
```

```SQL
CREATE TABLE tasks (
    id SERIAL PRIMARY KEY,
    description VARCHAR(100)
);
INSERT INTO tasks (description) VALUES ('Finish work'), ('Have fun');
```

tart a new container by running the following command, attaching the same volume with the persisted data:

```bash
 docker run --name=new-db -d -v postgres_data:/var/lib/postgresql postgres:18
```

You might have noticed that the POSTGRES_PASSWORD environment variable has been omitted. That’s because that variable is only used when bootstrapping a new database.
