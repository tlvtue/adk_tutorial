"""
Action Recommender Agent

This agent is responsible for recommending appropriate next actions
based on the lead validation and scoring results.
"""

from google.adk.agents import LlmAgent

# --- Constants ---
GEMINI_MODEL = "gemini-2.0-flash"

# Create the recommender agent
action_recommender_agent = LlmAgent(
    name="ActionRecommenderAgent",
    model=GEMINI_MODEL,
    instruction="""You are an Brand Recommendation AI.
    
    Based on the user's input and scoring:
    
    - For brand campaigns scored 1-5: suggest the brand campaign doesn't fit the influencer 
    - For brand campaigns scored 6-8: suggest the brand campaign could fit the influencer but also suggest things that could be improved 
    - For leads scored 9-10: suggest the brand campaign fits the influencer
    
    Explain your decision.
    
    Campaign Validation Status:
    {validation_status}

    Campaign Score:
    {campaign_score}

    """,
    description="Recommends or not recommend based on campaign score",
    output_key="action_recommendation",
)
