from google.adk import SequentialAgent, SessionState
from agents.validation_agent import ValidationAgent
from agents.feedback_agent import FeedbackAgent
import dummy_data

class MasterAgent(SequentialAgent):
    def __init__(self):
        super().__init__(sub_agents=[ValidationAgent(), FeedbackAgent()])

    def initialize(self, session: SessionState):
        # Seed session state with dummy data
        session.state["requirement"] = dummy_data.campaign_requirement
        session.state["content"] = dummy_data.creator_post