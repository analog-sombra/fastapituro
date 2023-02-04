from fastapi import FastAPI
from typing import Union
import instaloader
L = instaloader.Instaloader()


app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/{username}")
async def read_item(username: str, q: Union[str, None] = None):
    try:
        profile = instaloader.Profile.from_username(L.context, username)
        return {"status": True, "username": username, "follower": profile.followers, "following": profile.followees, "avatar": profile.get_profile_pic_url(), "q": q}
    except:
        return {"status": False}
