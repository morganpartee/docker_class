from fastapi import FastAPI
from pickle import load
import numpy as np
import uvicorn

app = FastAPI()

with open("model.pkl", "rb") as f:
    clf = load(f)


@app.get("/")
def root():
    return {"Hello": "World"}


@app.get("/predict")
def predict(sep_len: int, sep_wid: int, ped_len: int, ped_wid: int):
    return {
        "result": clf.predict(
            np.array([sep_len, sep_wid, ped_len, ped_wid]).reshape(1, -1)
        )[0]
    }


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=80)
