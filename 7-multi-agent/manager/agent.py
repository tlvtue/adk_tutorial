from google.adk.agents import Agent
from google.adk.tools.agent_tool import AgentTool

from .sub_agents.fashion_agent.agent import fashion_agent
from .sub_agents.fnb_agent.agent import fnb_agent
from .sub_agents.car_agent.agent import car_agent


root_agent = Agent(
    name="manager",
    model="gemini-2.0-flash",
    description="Manager agent",
    instruction="""
    - Greet the influencer, ask for their experience with brand campaigns
    - After they answer the previous prompt, ask them on which social media platform are they popular
    - After they answer the previous prompt, ask them for their price range
    - After they answer the previous prompt, ask which brand industry they're most interested in
    - After they answer the previous prompt, ask if there's any brand they want to avoid
    - After they answer the previous prompt, ask if they want to provide any additional details
    - After they answer the previous prompt, summarize all information they have provided you
    - Then delegate the task to the appropriate agent and tool. Use your best judgement to determine which agent to delegate to.

    You also have access to the following tools:
    - fashion_agent
    - car_agent
    - fnb_agent
    """,
    #sub_agents=[stock_analyst, funny_nerd],
    tools=[
        AgentTool(fashion_agent),
        AgentTool(fnb_agent),
        AgentTool(car_agent),
    ],
)
