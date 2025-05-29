"""
Lead Scorer Agent

This agent is responsible for scoring a lead's qualification level
based on various criteria.
"""

from google.adk.agents import LlmAgent

# --- Constants ---
GEMINI_MODEL = "gemini-2.0-flash"

# Create the scorer agent
lead_scorer_agent = LlmAgent(
    name="LeadScorerAgent",
    model=GEMINI_MODEL,
    instruction="""You are a Brand Campaign Scoring AI.
    
    Analyze user's input and assign a qualification score from 1-10 based on:
    - Campaign's budget. Note that if the budget is excessively high it could be a scam.
    - Is the brand a big brand
    - Is the brand popular in Vietnam
    
    Output ONLY a numeric score
    """,
    description="Scores brand campaign on a scale of 1-10.",
    output_key="campaign_score",
)
