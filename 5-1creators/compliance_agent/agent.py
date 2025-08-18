from google.adk.agents import ParallelAgent, SequentialAgent, LoopAgent
from compliance_agent.subagents.get_post import get_post
from compliance_agent.subagents.get_requirement import get_requirement
from compliance_agent.subagents.compare import compare



get_details = ParallelAgent(
    name="get_details",
    sub_agents=[get_requirement, get_post],
)

# refinement_loop = LoopAgent(
#     name="refinement_loop",
#     max_iterations=10,
#     sub_agents=[
#         reviewer,
#         refiner,
#     ],
#     description="Iteratively reviews and refines feedback result until requirements are met",
# )

root_agent = SequentialAgent(
    name="root_agent",
    sub_agents=[get_details, compare],
)
















