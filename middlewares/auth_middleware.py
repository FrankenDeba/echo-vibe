from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from jose import JWTError, jwt
from fastapi.responses import JSONResponse
from constants import SECRET_KEY,ALGORITHM


class AuthMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        authorization: str = request.headers.get("Authorization")
        user = None

        if authorization and authorization.startswith("Bearer "):
            token = authorization[7:]
            try:
                payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
                user_id = payload.get("sub")
                if user_id:
                    user = {"id": int(user_id)}  # Or attach more user info if needed
            except JWTError:
                return JSONResponse(status_code=401, content={"detail": "Invalid token"})

        request.state.user = user
        response = await call_next(request)
        return response
