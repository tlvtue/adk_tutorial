from google.adk.agents import Agent, LlmAgent
from pydantic import BaseModel, Field


root_agent = LlmAgent(
    name = "get_requirement",
    model="gemini-2.5-flash-lite",
    description="Get a requirement list from brand's campaign requirements",
    instruction="""
    You must read brand's campaign requirements from user's request and create a list of requirements based on those requirements.
    The fields include (media_format, start_date, end_date, platfrom, hashtag, mention, video_length, text).
    IMPORTANT: Your response MUST be valid JSON matching this structure:
    {
        {"field_1": "the requirement related to the field here"
        },

        {"field_2": "the requirement related to the field here"
        },


        .....,
        {"field_n": "the requirement related to the field here"
        },

    }
    The fields include (media_format, start_date, end_date, platfrom, hashtag, mention, video_length, text_length, content).
    media_format can include: video, photo or text.
    If you don't find requirements for a field from user's request, leave it as field_name:null in your output.
    DO NOT include any explanations or additional text outside the JSON response.
    """,
    output_key="campaign_requirement_json"
)

#################################################
# the post must include video and text, must be on youtube and instagram, must mention @vinamilk, must hashtag #kiwimilk, video must be at least 300 seconds long and you must have a positive tone















# #update to improve performance
# checklist_agent = ParallelAgent(
#     name="checklist_agent",
#     sub_agents=[comparer_1, comparer_2, comparer_3],
# )

# master_agent = SequentialAgent(
#     name="master_agent",
#     sub_agents=[checklist_agent, report_agent],
# )



