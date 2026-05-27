import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

from app.api.endpoints import router as api_router

app = FastAPI(
    title="AI Website Generator API",
    description="Backend for generating React-based websites using Gemini AI",
    version="1.0.0"
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # In production, replace with your frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include API routes
app.include_router(api_router, prefix="/api/v1")

@app.get("/")
async def root():
    return {"message": "AI Website Generator API is running"}

if __name__ == "__main__":
    port = int(os.getenv("PORT", 8000))
    print(f"\n🚀 Server starting at http://localhost:{port}")
    print(f"📖 Documentation available at http://localhost:{port}/docs\n")
    uvicorn.run("main:app", host="0.0.0.0", port=port, reload=True)
