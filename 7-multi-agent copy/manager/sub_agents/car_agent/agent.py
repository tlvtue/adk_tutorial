from google.adk.agents import Agent
from google.adk.tools import google_search

# def get_current_time() -> dict:
#     """
#     Get the current time in the format YYYY-MM-DD HH:MM:SS
#     """
#     return {
#         "current_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
#     }

car_agent = Agent(
    name="tool_agent",
    model="gemini-2.0-flash",
    description="You're an agent that recommends the most suitable car campaigns for the user to work with.",
    instruction="""
    - Google search and return top 3 most suitable car campaigns for the influencer using `google_seach` tool. Remember to include brand name.
    """,
    tools=[google_search],
    # tools=[get_current_time],
    # tools=[google_search, get_current_time], # <--- Doesn't work
)