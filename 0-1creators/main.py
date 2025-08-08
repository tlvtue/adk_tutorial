import asyncio
from google.adk.sessions import InMemorySessionService
from google.adk.runners import Runner
from google.genai import types
from agents.master import MasterAgent

async def main():
    # Initialize session infrastructure
    session_service = InMemorySessionService()
    session = session_service.create_session(
        app_name="1creators_ai",
        user_id="creator_1",
        session_id="session_1"
    )

    # Instantiate and seed MasterAgent
    master = MasterAgent()
    master.initialize(session)

    # Run the pipeline
    runner = Runner(
        agent=master,
        app_name="1creators_ai",
        session_service=session_service
    )

    start_msg = types.Content(role="system", parts=[types.Part(text="__start__")])

    # Drive the workflow
    async for event in runner.run_async(
        user_id="creator_1",
        session_id=session.id,
        new_message=start_msg
    ):
        if event.is_final_response():
            break

    # Print results
    print("Validation Results:", session.state.get("validation"))
    print("Feedback to Creator:\n", session.state.get("feedback"))

if __name__ == "__main__":
    asyncio.run(main())
