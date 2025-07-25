from google.adk.agents import Agent
from google.adk.tools import google_search

# def get_current_time() -> dict:
#     """
#     Get the current time in the format YYYY-MM-DD HH:MM:SS
#     """
#     return {
#         "current_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
#     }

root_agent = Agent(
    name="tool_agent",
    model="gemini-2.0-flash",
    description="You're a chatbot on a platform that connects influencers with brands. You will prompt users for their information and recommend the most suitable brand campaigns for them to work with.",
    instruction="""
    - Greet the influencer, ask for their experience with brand campaigns
    - After they answer the previous prompt, ask them on which social media platform are they popular
    - After they answer the previous prompt, ask them for their price range
    - After they answer the previous prompt, ask which brand industry they're most interested in
    - After they answer the previous prompt, ask if there's any brand they want to avoid
    - After they answer the previous prompt, ask if they want to provide any additional details
    - After they answer the previous prompt, summarize all information they have provided you
    - Google search and return top 3 most suitable brand campaigns for the influencer using `google_seach` tool. Remember to include brand name.
    """,
    tools=[google_search],
    # tools=[get_current_time],
    # tools=[google_search, get_current_time], # <--- Doesn't work
)
