from codigo import chain
from fastapi import FastAPI
from langserve import add_routes

app = FastAPI(
    title="TRANSLATIONS POWERED BY LANGCHAIN", 
    description="Translations of texts into various languages.", 
    version="1.0"
    )

add_routes(app, chain, path="/translator")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)