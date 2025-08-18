from fastapi import FastAPI, BackgroundTasks
from pydantic import BaseModel

app = FastAPI()

class GenerationRequest(BaseModel):
    prompt: str

# This would be a more complex service call in reality
async def process_ai_generation(project_id: str, prompt: str):
    print(f"Starting AI generation for project {project_id} with prompt: '{prompt}'")
    # 1. Call LLM service to get structured JSON
    # 2. Call layout engine
    # 3. Save result to project's design_document in DB
    # 4. Notify user via WebSocket
    pass

@app.post("/generate/{project_id}")
async def generate_design(project_id: str, request: GenerationRequest, background_tasks: BackgroundTasks):
    background_tasks.add_task(process_ai_generation, project_id, request.prompt)
    return {"message": "AI generation started in the background."}
