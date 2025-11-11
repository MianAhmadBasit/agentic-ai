from fastapi import Body, FastAPI
from ollama import Client
app = FastAPI()
# Use the Ollama client class (imported above). The original code attempted
# to instantiate `Client(...)` which is undefined and causes a NameError.
client = Client(
    host="http://localhost:11434",
)
@app.get("/")
def read_root():
    return {"Hello": "World"}
@app.post("/chat")
def chat(
         message: str = Body(..., description="The Message")

):
    response = client.chat(model="gemma:2b" , messages=[
        {"role": "user", "content": message}])

    return {"response": response.message.content}