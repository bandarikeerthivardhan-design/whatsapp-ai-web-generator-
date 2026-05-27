from fastapi import APIRouter, HTTPException
from app.models.schemas import SiteGenerationRequest, SiteGenerationResponse
from app.ai.gemini_client import get_gemini_model
from app.prompts.extraction_prompt import EXTRACTION_SYSTEM_PROMPT
from app.generators.site_generator import SiteGenerator
import json

router = APIRouter()

@router.post("/generate-site", response_model=SiteGenerationResponse)
async def generate_site(request: SiteGenerationRequest):
    """
    Endpoint to trigger the website generation process.
    """
    try:
        # 1. Initialize Gemini Model
        model = get_gemini_model()

        # 2. Format the prompt
        formatted_prompt = EXTRACTION_SYSTEM_PROMPT.format(user_prompt=request.prompt)

        # 3. Call Gemini API
        response = model.generate_content(formatted_prompt)

        # 4. Parse the response
        try:
            extracted_data = json.loads(response.text)
        except json.JSONDecodeError:
            raise HTTPException(status_code=500, detail="Failed to parse AI response as JSON")

        # 5. Generate the actual files
        generator = SiteGenerator()
        generated_path = generator.generate_files(extracted_data)

        return SiteGenerationResponse(
            status="success",
            data={
                "requirements": extracted_data,
                "business_type": extracted_data.get("business_type"),
                "generated_site_path": generated_path
            }
        )

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
