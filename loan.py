from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class LoanApplication(BaseModel):
    age:int
    income:float
    loan_amount:float
    employeement_years:int

@app.post("/predict")
def predict_loan(application:LoanApplication):

    #pretend this trained model
    if application.income > 50000 and application.employeement_years > 2:
        decesion = "approved"
    else:
        decesion = "rejected"

    return {
        "application_age": application.age,
        "decesion":{f"Loan is ":decesion}
    }        


@app.get("/customer/{customer_id}")
def get_customer(customer_id:int):
    return {
        "customer_id":customer_id
    }