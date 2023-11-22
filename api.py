"""API with FastAPI."""

from fastapi import FastAPI
from pydantic import BaseModel

from calculator import calculate

users = [

 { "id": 1, "nom": "Dupont", "prénom": "Jean", "email": "jean.dupont@example.com", },

 { "id": 2, "nom": "Martin", "prénom": "Marie", "email": "marie.martin@example.com", },

 { "id": 3, "nom": "Robert", "prénom": "Paul", "email": "paul.robert@example.com", },

 { "id": 4, "nom": "Ignace", "prénom": "Simon", "email": "simon.robert@example.com", },

 { "id": 5, "nom": "Lancelot", "prénom": "Nicolas", "email": "nicolas.lancelot@example.com", },

 { "id": 7, "nom": "Baudin", "prénom": "Raphaelle", "email": "raphaelle.baudin@example.com", },

 { "id": 8, "nom": "Lusignet", "prénom": "Josseline", "email": "josseline.lusignet@example.com", },

]

class UserInput(BaseModel):
    operation: str
    x: float
    y: float


app = FastAPI()


@app.post("/calculate")
def operate(user_input: UserInput):
    """

    Args:
        user_input: user input parameters

    Returns:
        Union[float, str]

    """
    result = calculate(user_input.operation, user_input.x, user_input.y)
    return result

@app.get("/get_user")
def load_questions():
    return users