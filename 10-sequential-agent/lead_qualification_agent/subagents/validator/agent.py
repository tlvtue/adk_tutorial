"""
Lead Validator Agent

This agent is responsible for validating if a lead has all the necessary information
for qualification.
"""

from google.adk.agents import LlmAgent

# --- Constants ---
GEMINI_MODEL = "gemini-2.0-flash"

# Create the validator agent
lead_validator_agent = LlmAgent(
    name="LeadValidatorAgent",
    model=GEMINI_MODEL,
    instruction="""
    Examine the brand campaign and determine if it's valid or invalid.
    A valid brand campaign needs to include:
    -Real brand name
    -What they expect you to do 
    -Budget
    -Timeline
    
    Output ONLY 'valid' or 'invalid' with a single reason if invalid.
    
    Example valid output: 'valid'
    Example invalid output: 'invalid: is not a legit brand'
    """,
    description="You're an agent that validates if the input is a legit brand",
    output_key="validation_status",
)
