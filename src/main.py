import pandas as pd
from entities import Person
from typing import Annotated

from model import load_model, load_encoder

from fastapi import FastAPI, HTTPException, Depends, Body
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

app = FastAPI()
bearer = HTTPBearer()

ml_models = {}


@app.on_event("startup")
async def startup_event():
    ml_models["ohe"] = load_encoder()
    ml_models["models"] = load_model()


@app.get("/")
async def root():
    """
    Route to check that API is alive!
    """
    return "Model API is alive!"


def get_username_for_token(token):
    if token == "abc123":
        return "pedro1"
    return ""


async def validate_token(credentials: HTTPAuthorizationCredentials = Depends(bearer)):
    token = credentials.credentials

    username = get_username_for_token(token)
    if username == "":
        raise HTTPException(status_code=401, detail="Invalid token")

    return {"username": username}


@app.post("/predict")
async def predict(
    person: Annotated[
        Person,
        Body(
            examples=[
                {
                    "age": 42,
                    "job": "entrepreneur",
                    "marital": "married",
                    "education": "primary",
                    "balance": 558,
                    "housing": "yes",
                    "duration": 186,
                    "campaign": 2,
                }
            ],
        ),
    ],
    user=Depends(validate_token),
):
    """
    Route to make predictions!
    """
    ohe = ml_models["ohe"]
    model = ml_models["models"]

    person_t = ohe.transform(pd.DataFrame([person.model_dump()]))
    pred = model.predict(person_t)[0]

    return {"prediction": str(pred)}
