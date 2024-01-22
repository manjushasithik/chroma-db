from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from create_database import create_vector_db
from retrieve import retrieve_vector_db

import subprocess

# Uninstall old version
subprocess.run(['pip', 'uninstall', 'sqlite3', '-y'])

# Install latest version
subprocess.run(['pip', 'install', 'sqlite3'])

print("SQLite updated successfully.")
@asynccontextmanager
async def lifespan(app: FastAPI):
    create_vector_db("chromadbtest")
    yield

app = FastAPI(lifespan=lifespan)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/chromadb/v1/{query}")
async def read_item(query: str):
    return {'data' : retrieve_vector_db(query)}
