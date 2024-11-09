# Fastapi


## Map
project/
├── main.py                       # FastAPI application entry point
├── config.py                     # Configuration for environment variables, JWT, and database
├── .env                          # Environment file to store secrets like JWT_SECRET_KEY, DB credentials
├── db/                           # Database-related code
│   ├── __init__.py
│   └── connection.py             # MySQL database connection setup
├── routes/                       # API routes for specific resources
│   ├── __init__.py
│   └── dkg_data.py               # Routes for accessing data from dkg_view with JWT protection
├── schemas/                      # Data schemas for request and response validation
│   ├── __init__.py
│   └── dkg_schema.py             # Schema for data in dkg_view
├── auth/                         # JWT authentication module
│   ├── __init__.py
│   └── auth.py                   # Endpoint for generating JWT tokens
├── dependencies/                 # Security and other shared dependencies
│   ├── __init__.py
│   └── dependencies.py           # JWT token validation dependency
└── requirements.txt              # List of dependencies for the project


## Run the Server

Start the FastAPI server:

```bash
uvicorn main:app --host 0.0.0.0 --port 8000

```

## requirements

```bash
pip install -r requirements.txt

```

## Generate JWT_SECRET_KEY
```bash
openssl rand -hex 32
```


## test api

```bash
curl -X POST "http://localhost:8000/token" -d "username=authorized_user"


```

### will get this 

```bash
{
  "access_token": "your_generated_jwt_token",
  "token_type": "bearer"
}

```

### Access Protected Route: 
Use the token to access the protected API route:
```bash

curl -X GET "http://localhost:8000/api/dkg_data" -H "Authorization: Bearer your_generated_jwt_token"

```