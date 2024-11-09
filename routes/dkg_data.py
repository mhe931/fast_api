from fastapi import APIRouter, Depends, HTTPException
from db.connection import create_connection
from schemas.dkg_schema import DkgData
from dependencies.dependencies import get_current_user
import jwt
from config import JWT_SECRET_KEY, JWT_ALGORITHM

router = APIRouter()

@router.get("/dkg_data", response_model=list[DkgData])
async def get_dkg_data(request: Request, token: str = Depends(get_current_user)):
    try:
        # Decode the token to get IP, username, and dates
        payload = jwt.decode(token, JWT_SECRET_KEY, algorithms=[JWT_ALGORITHM])
        client_ip = payload.get("ip")
        username = payload.get("sub")
        from_date = payload.get("from_date")
        to_date = payload.get("to_date")

        # Check if the current request IP matches the token's IP
        if client_ip != request.client.host:
            raise HTTPException(status_code=401, detail="IP address mismatch")

        # Proceed with database query or other logic as needed
        connection = create_connection()
        cursor = connection.cursor(dictionary=True)
        query = """
            SELECT * FROM dkg_view 
            WHERE date BETWEEN %s AND %s
        """
        cursor.execute(query, (from_date, to_date))
        results = cursor.fetchall()
        return results

    except jwt.DecodeError:
        raise HTTPException(status_code=401, detail="Invalid token format")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()
