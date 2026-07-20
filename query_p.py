from fastapi import FastAPI

app =FastAPI()

all_customers = [
    {"id":101, "name":"Ravi", "city":"bengaluru", "risk":"high"},
    {"id":102, "name":"Anish", "city":"Hyderabad", "risk":"medium"},
    {"id":103, "name":"Kumaran", "city":"Chennai", "risk":"low"},
    {"id":104, "name":"Sahil", "city":"Durgapur", "risk":"high"},
    {"id":105, "name":"Debraj", "city":"bengaluru", "risk":"high"},
]

@app.get("/customers")
def get_customers(city:str,risk:str):
    filtered =[
        c for c in all_customers
        if c["city"] == city and c["risk"] == risk
    ]
    
    return {
        "city":city,
        "risk":risk,
        "count":len(filtered),
        "results":filtered
    }