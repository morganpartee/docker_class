from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import pickle


app = FastAPI(title="<TEAM> ML Model", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Let's load in the model we used before
with open("model.pkl", "rb") as f:
    clf = pickle.load(f)


class Iris(BaseModel):
    """
    Stores whatever variables your model needs to make a prediction
    Make sure you use type hints!
    """

    sepal_len: float
    sepal_wid: float
    petal_len: float
    petal_wid: float


@app.post("/predict")
def predict(sample: Iris):
    """
    Unpack the responses, predict on the input variables, and return the prediction.
    """
    responses = [
        [sample.sepal_len, sample.sepal_wid, sample.petal_len, sample.petal_wid]
    ]
    return clf.predict(responses)[0]
