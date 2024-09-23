from fastapi import FastAPI

# Create an instance of FastAPI.
app = FastAPI()

# Default route that returns a simple message.
@app.get("/")
def get_root():
  return {"message": "Hello, World!"}