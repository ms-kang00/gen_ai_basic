import uuid
from fastapi import APIRouter
from schema.image_schema import PromptRequest, PromptResponse
from datetime import datetime
from service.ai_service import AIService

router = APIRouter(prefix="/api")

@router.post("/image", response_model=PromptResponse)
async def gen_image(req: PromptRequest):
    print(f"Human Prompt: {req}")
    unique_id = str(uuid.uuid4())
    print(f">> unique_id: {unique_id}")
    
    current_time = datetime.now()
    ai_service = AIService()
    
    graph = ai_service.gen_graph(req.prompt)
    state = graph.invoke({
        "id": unique_id,
        "prompt": req.prompt,
        "image_url": ""
    })
    
    return {"url": state["image_url"]}