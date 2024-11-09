from fastapi import APIRouter, HTTPException, Request, Form
from datetime import datetime, timedelta
import jwt
from config import JWT_SECRET_KEY, JWT_ALGORITHM, AUTHORIZED_USER, CLIENT_IP

router = APIRouter()

def create_token(data: dict, expires_delta: timedelta = timedelta(hours=1)):
    to_encode = data.copy()
    expire = datetime.utcnow() + expires_delta
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, JWT_SECRET_KEY, algorithm=JWT_ALGORITHM)
    return encoded_jwt

@router.post("/token")
async def generate_token(
    request: Request,
    username: str = Form(...),
    from_date: str = Form(...),
    to_date: str = Form(...)
):
    # Retrieve the client's IP address
    client_ip = request.client.host
    print(f"Client IP: {client_ip}")

    # Validate the username and IP combination (add custom validation here if needed)
    if (username == AUTHORIZED_USER) and (client_ip == CLIENT_IP):  
        # Generate token with IP and username in the payload
        token = create_token({
            "sub": username,
            "ip": client_ip,
            "from_date": from_date,
            "to_date": to_date
        })
        return {"access_token": token, "token_type": "bearer"}
    else:
        raise HTTPException(status_code=401, detail="Unauthorized")
