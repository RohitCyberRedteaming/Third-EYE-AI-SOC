from fastapi import FastAPI, Header

app = FastAPI()

TENANTS = {"demo":"CompanyA"}

@app.get("/")
def home():
    return {"status":"SaaS running"}

@app.get("/tenant")
def tenant(x_api_key: str = Header(...)):
    return {"tenant": TENANTS.get(x_api_key,"invalid")}