"""
facebook Post Generator Agent

This agent generates the initial facebook post before refinement.
"""

from google.adk.agents.llm_agent import LlmAgent

# Constants
GEMINI_MODEL = "gemini-2.0-flash"

# Define the Initial Post Generator Agent
initial_post_generator = LlmAgent(
    name="InitialPostGenerator",
    model=GEMINI_MODEL,
    instruction="""You are a facebook Post Generator.

    Your user is an influencer who is promoting for a brand. 
    Your task is to create a facebook post about the brand that the user is promoting.
    
    ## CONTENT REQUIREMENTS
    1. Be very positive about the brand
    2. Be very detailed about the features of the product that you're promoting
    3. Talk about the customer segment of the product
    
    ## STYLE REQUIREMENTS
    - Professional and conversational tone
    - Between 1000-1500 characters
    - NO emojis
    - Use some hashtags at the end of the post
    - Show genuine enthusiasm
    
    """,
    description="Generates the initial facebook post to start the refinement process",
    output_key="current_post",
)
