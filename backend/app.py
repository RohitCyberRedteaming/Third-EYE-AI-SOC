from fastapi import FastAPI, Request, HTTPException
from integrations.qradar_api import get_offenses
from backend.brain import analyze_offense

# 🔐 NEW IMPORTS
from backend.auth import create_token, verify_token
from backend.roles import get_role

app = FastAPI()


# ✅ HEALTH CHECK
@app.get("/")
def home():
    return {"status": "Third EYE AI SOC Running"}


# 📊 EXISTING FUNCTION (UNCHANGED - IMPORTANT)
@app.get("/analyze")
def analyze():
    try:
        offenses = get_offenses()
        results = []

        for off in offenses:
            results.append(analyze_offense(off))

        return results

    except Exception as e:
        return {"error": str(e)}


# 🔐 LOGIN API (NEW)
@app.post("/login")
async def login(request: Request):
    try:
        body = await request.json()
        user = body.get("username")

        if not user:
            raise HTTPException(status_code=400, detail="Username required")

        token = create_token(user)
        role = get_role(user)

        return {
            "token": token,
            "role": role,
            "message": f"Login successful for {user}"
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 🤖 SECURE AI QUERY (NEW)
@app.post("/ai-secure")
async def ai_secure(request: Request):
    try:
        body = await request.json()

        token = body.get("token")
        query = body.get("query")

        if not token:
            raise HTTPException(status_code=401, detail="Token missing")

        user_data = verify_token(token)
        user = user_data.get("user")

        # 🧠 SIMPLE AI LOGIC (UPGRADE LATER)
        if "critical" in query.lower():
            return {"response": "Showing critical alerts from QRadar"}

        elif "block" in query.lower():
            return {"response": "Triggering SOAR playbook to block threat"}

        elif "status" in query.lower():
            return {"response": "SOC is running normally"}

        return {"response": f"AI processed query: {query} for user {user}"}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 📊 SECURE ANALYZE (ROLE BASED)
@app.post("/analyze-secure")
async def analyze_secure(request: Request):
    try:
        body = await request.json()
        token = body.get("token")

        if not token:
            raise HTTPException(status_code=401, detail="Token missing")

        user_data = verify_token(token)
        user = user_data.get("user")

        role = get_role(user)

        offenses = get_offenses()
        results = []

        for off in offenses:
            results.append(analyze_offense(off))

        return {
            "user": user,
            "role": role,
            "data": results
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
