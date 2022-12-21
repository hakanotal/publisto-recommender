from fastapi import FastAPI
import word2vec_rec

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/recs/{user_id}")
async def get_recs(user_id: int):
    return word2vec_rec.get_user_recs(user_id)