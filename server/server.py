from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Prime checking function

def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for i in range(2, n//2):
        if n % i == 0:
            return False
    return True



print(is_prime(29))

# Request model
class PrimeRequest(BaseModel):
    numbers: int

# API route to check prime numbers
@app.post("/check_prime/")
async def check_prime(request: PrimeRequest):
    result = is_prime(request.number)
    return {"number": request.number, "is_prime": result}