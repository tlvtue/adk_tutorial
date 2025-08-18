from google.adk.agents import LlmAgent
# from pydantic import BaseModel
# from typing import Optional

# class CampaignRequirementExtract(BaseModel):
#     media_format: Optional[str] = None       # "video" | "photo" | "text"
#     start_date: Optional[str] = None         # "YYYY-MM-DD"
#     end_date: Optional[str] = None           # "YYYY-MM-DD"
#     platform: Optional[str] = None           # "facebook" | "instagram" | "tiktok"
#     hashtag: Optional[str] = None            # e.g., "#BrandX"
#     mention: Optional[str] = None            # e.g., "@BrandHandle"
#     video_length: Optional[int] = None       # seconds
#     text_length: Optional[int] = None        # words
#     content: Optional[str] = None            # raw text content if present

get_requirement = LlmAgent(
    name = "get_requirement",
    model="gemini-2.5-flash-lite",
    description="Extract a normalized requirement json object from brand's campaign requirements.",
    instruction="""
    You must read brand's campaign requirements from {campaign_requirement} and create a list of requirements based on those requirements.
    IMPORTANT: Your response MUST be ONE valid JSON matching this structure:
    {
        "field_1": "the requirement related to the field here",

        "field_2": "the requirement related to the field here",
        .....,
        "field_n": "the requirement related to the field here",
    }
    The fields include:
    - media_format (one or more of: "video", "photo", "text")
    - start_date (YYYY-MM-DD)
    - end_date (YYYY-MM-DD)
    - platform (one ore more of: "facebook", "instagram", "tiktok")
    - hashtag (e.g., "#BrandX"),can have multiple hashtags
    - mention (e.g., "@BrandHandle"), can have multiple mentions
    - video_length 
    - text_length 
    - content (can be main ideas, tone, etc.)
    DO NOT exclude any field from your output and don't add any new field to your output.
    If you don't find details for a field from {campaign_requirement}, leave it as field_name:null in your output.

    DO NOT include any explanations or additional text outside the JSON response.
    """,
    output_key="campaign_requirement_json",
    # output_schema=CampaignRequirementExtract, 
)

