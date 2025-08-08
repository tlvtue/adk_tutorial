import uuid

from dotenv import load_dotenv
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai import types
from agents.master_agent import master_agent
from data.campaign import requirement
from data.creator import post

load_dotenv()


# Create a new session service to store state
session_service_stateful = InMemorySessionService()


initial_state = {
    "requirement": requirement,
    "post": post,
}

# Create a NEW session
APP_NAME = "1Creators Compliance AI"
USER_ID = "tue_tran"
SESSION_ID = str(uuid.uuid4())
stateful_session = session_service_stateful.create_session(
    app_name=APP_NAME,
    user_id=USER_ID,
    session_id=SESSION_ID,
    state=initial_state,
)
print("CREATED NEW SESSION:")
print(f"\tSession ID: {SESSION_ID}")

runner = Runner(
    agent=master_agent,
    app_name=APP_NAME,
    session_service=session_service_stateful,
)

new_message = types.Content(
    role="user", parts=[types.Part(text="give feedbacks on why or why not the creator's post satisfies campaign's requirements and what the creator can do to improve it.")]
)

for event in runner.run(
    user_id=USER_ID,
    session_id=SESSION_ID,
    new_message=new_message,
):
    if event.is_final_response():
        if event.content and event.content.parts:
            print(f"Final Response: {event.content.parts[0].text}")

print("==== Session Event Exploration ====")
session = session_service_stateful.get_session(
    app_name=APP_NAME, user_id=USER_ID, session_id=SESSION_ID
)

# Log final Session state
print("=== Final Session State ===")
for key, value in session.state.items():
    print(f"{key}: {value}")
