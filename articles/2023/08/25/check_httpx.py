"""
https://www.twilio.com/blog/asynchronous-http-requests-in-python-with-httpx-and-asyncio
"""
import asyncio
import httpx
import time


async def simple():
    pokemon_url = "https://pokeapi.co/api/v2/pokemon/151"

    async with httpx.AsyncClient() as client:
        resp = await client.get(pokemon_url)
        pokemon = resp.json()
        print(pokemon["name"])


async def more_requests():
    async with httpx.AsyncClient() as client:
        for number in range(1, 151):
            pokemon_url = f"https://pokeapi.co/api/v2/pokemon/{number}"

            resp = await client.get(pokemon_url)

            pokemon = resp.json()
            print(pokemon["name"])


def more_requests_but_synchronous():
    with httpx.Client() as client:
        for number in range(1, 151):
            pokemon_url = f"https://pokeapi.co/api/v2/pokemon/{number}"

            resp = client.get(pokemon_url)

            pokemon = resp.json()
            print(pokemon["name"])


async def more_requests_but_better():
    async def get_pokemon(client: httpx.AsyncClient, url:str) -> str:
        resp = await client.get(url)
        pokemon = resp.json()

        return pokemon['name']

    async with httpx.AsyncClient() as client:

        tasks = []
        for number in range(1, 151):
            pokemon_url = f"https://pokeapi.co/api/v2/pokemon/{number}"

            tasks.append(asyncio.ensure_future(get_pokemon(client, pokemon_url)))

        original_pokemons = await asyncio.gather(*tasks)
        for pokemon in original_pokemons:
            print(pokemon)

if __name__ == "__main__":
    start = time.perf_counter()

    # asyncio.run(more_requests())
    # more_requests_but_synchronous()
    asyncio.run(more_requests_but_better())

    print(f"It took {time.perf_counter() - start}s")
