"""
    https://developer.spotify.com/documentation/general/guides/authorization/client-credentials/
"""
import base64
import os
import requests
import json

from pprint import pprint

from dotenv import load_dotenv

def get_token(auth_string:str) -> str:
    """ Returns string with access token to Spotify """
    auth_bytes = auth_string.encode("utf-8")
    auth_base64 = str(base64.b64encode(auth_bytes), "utf-8")
    url = "https://accounts.spotify.com/api/token"
    headers = {
        "Authorization": "Basic " + auth_base64,
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {
        "grant_type": "client_credentials"
    }

    resp = requests.post(url, headers=headers, data=data)
    json_result = json.loads(resp.content)
    token = json_result["access_token"]
    return token


def get_auth_header(token:str) -> str:
    return {"Authorization": "Bearer " + token}


def serach_for_artist(token: str, artist_name: str) -> dict:
    url = "https://api.spotify.com/v1/search"
    headers = get_auth_header(token)
    query = f"?q={artist_name}&type=artist&limit=1"
    
    query_url = url + query 
    resp = requests.get(query_url, headers=headers)
    result_json = json.loads(resp.content)["artists"]["items"]

    if len(result_json) == 0:
        print(f"Artist {artist_name} does not exist.")
        return None
    
    return result_json[0]
    
def get_topp_traks(token: str, artist_id: str) -> dict:
    """"""
    url = f"https://api.spotify.com/v1/artists/{artist_id}/top-tracks?market=PL"
    headers = get_auth_header(token)
    
    resp = requests.get(url, headers=headers)
    resp_json = json.loads(resp.content)
    traks = resp_json["tracks"]
    print(len(traks))
    pprint(traks[1])
    
    return sorted(list(traks), key=lambda x: x['popularity'])
    

def main() -> None:
    print(f'Hello main from : {__file__}')
    load_dotenv()
    
    client_id = os.getenv("CLIENT_ID")
    client_secret = os.getenv("CLIENT_SECRET")
    auth_string = client_id + ":" + client_secret
        
    token = get_token(auth_string)
    artist = serach_for_artist(token, "Metallica")
    artist_id = artist["id"]
    
    traks = get_topp_traks(token, artist_id)

    
    for i, song in enumerate(traks):
        print(f"{i + 1}. {song['name']} popularity {song['popularity']}")

if __name__ == '__main__':
    main()