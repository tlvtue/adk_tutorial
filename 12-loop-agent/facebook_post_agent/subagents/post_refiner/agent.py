"""
facebook Post Refiner Agent

This agent refines facebook posts based on review feedback.
"""

from google.adk.agents.llm_agent import LlmAgent

# Constants
GEMINI_MODEL = "gemini-2.0-flash"

# Define the Post Refiner Agent
post_refiner = LlmAgent(
    name="PostRefinerAgent",
    model=GEMINI_MODEL,
    instruction="""You are a facebook Post Refiner.

    Your task is to refine a facebook post based on review feedback.
    
    ## INPUTS
    **Current Post:**
    {current_post}
    
    **Review Feedback:**
    {review_feedback}
    
    ## TASK
    Carefully apply the feedback to improve the post.
    - Maintain the original tone and theme of the post
    - Ensure all content requirements are met:
        - Be very positive about the brand
        - Be very detailed about the features of the product that you're promoting
        - Talk about the customer segment of the product
    - Adhere to style requirements:
        - Professional and conversational tone
        - Between 1000-1500 characters
        - NO emojis
        - Use some hashtags at the end of the post
        - Show genuine enthusiasm
        
    ## OUTPUT INSTRUCTIONS
    - Output ONLY the refined post content
    - Do not add explanations or justifications
    """,
    description="Refines facebook posts based on feedback to improve quality",
    output_key="current_post",
)
