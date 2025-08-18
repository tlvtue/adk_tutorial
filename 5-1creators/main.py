import uuid
import time
from dotenv import load_dotenv
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai import types
from compliance_agent.agent import root_agent
from data.campaign import campaign_requirement
from data.creator import creator_post, creator_id 

start_time = time.time()

load_dotenv()


# Create a new session service to store state
session_service_stateful = InMemorySessionService()


initial_state = {
    "campaign_requirement": campaign_requirement,
    "creator_post": creator_post,
}

# Create a NEW session
APP_NAME = "1Creators Compliance AI"
USER_ID = creator_id
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
    agent=root_agent,
    app_name=APP_NAME,
    session_service=session_service_stateful,
)

new_message = types.Content(
    # role="user", parts=[types.Part(text="Respond in Vietnamese and use natural language, do not include json objects.")]
    role="user", parts=[types.Part(text="")]
)


for event in runner.run(
    user_id=USER_ID,
    session_id=SESSION_ID,
    new_message=new_message,
):
    # if event.is_final_response():
    #     if event.content and event.content.parts:
    #         print(f"Final Response: {event.content.parts[0].text}")
    pass

end_time = time.time()
print(f"Execution time: {end_time - start_time:.4f} seconds")



print("==== Session Event Exploration ====")
session = session_service_stateful.get_session(
    app_name=APP_NAME, user_id=USER_ID, session_id=SESSION_ID
)

# Log final Session state
print("=== Final Session State ===")
for key, value in session.state.items():
    print(f"{key}: {value}")
# print(session.state["compare_result"])

