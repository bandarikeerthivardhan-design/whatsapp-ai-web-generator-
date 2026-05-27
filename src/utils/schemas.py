from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any

class SiteGenerationRequest(BaseModel):
    prompt: str = Field(..., example="Create a modern restaurant website for Bella Italia with online reservations and dark theme.")

class SiteContent(BaseModel):
    hero_heading: str
    hero_description: str
    cta_text: str
    feature_descriptions: Optional[List[str]] = []
    about_text: Optional[str] = ""
    footer_text: Optional[str] = ""

class SiteRequirements(BaseModel):
    business_type: str
    business_name: str
    theme: str
    primary_colors: List[str]
    pages: List[str]
    features: List[str]
    animations: List[str]
    seo_keywords: List[str]
    contact_info: Optional[Dict[str, str]] = {}
    content: SiteContent

class SiteGenerationResponse(BaseModel):
    status: str
    data: Dict[str, Any]
