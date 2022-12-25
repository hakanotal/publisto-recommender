from fastapi import FastAPI
import word2vec_rec
import uvicorn
import nltk
nltk.download('wordnet')
nltk.download('stopwords')

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/recs/{user_id}")
async def get_recs(user_id: int):
    return await word2vec_rec.get_user_recs(user_id)

if __name__ == "__main__":
  uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)