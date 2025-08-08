from google.adk import LlmAgent, SessionState

class FeedbackAgent(LlmAgent):
    name = "feedback_agent"
    model = "gemini-2.5-flash"
    description = (
        "Generate natural-language feedback based on the validation report."
    )

    async def run(self, session: SessionState):
        validation = session.state.get("validation", {})

        prompt = (
            f"You are a feedback agent.\n"
            f"Validation report: {validation}\n"
            "Produce a concise list of suggestions for the creator."
        )

        response = await self.llm.generate(prompt=prompt)
        session.state["feedback"] = response.text
