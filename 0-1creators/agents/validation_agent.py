from google.adk import LlmAgent, SessionState
import json

class ValidationAgent(LlmAgent):
    name = "validation_agent"
    model = "gemini-2.5-flash"
    description = (
        "Compare campaign requirements with creator's post and produce a validation report in JSON."
    )

    async def run(self, session: SessionState):
        requirements = session.state["requirement"]
        content = session.state["content"]

        prompt = (
            f"You are a validation agent.\n"
            f"Campaign requirements: {requirements}\n"
            f"Creator's post: {content}\n"
            "Compare each field (media_format, platform, hashtag, mention, video_length, text_length). "
            "Return a JSON object where keys are field names and values are {passed, expected, actual}."
        )

        # Invoke LLM
        response = await self.llm.generate(prompt=prompt)

        # Parse and store
        session.state["validation"] = json.loads(response.text)