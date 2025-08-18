from google.adk.agents import LlmAgent
# from pydantic import BaseModel
# from typing import Optional, List

# class Feedback(BaseModel):
#     feedback: Optional[str] = None

compare = LlmAgent(
    name="compare",
    model="gemini-2.5-flash-lite",
    description="Extract a normalized json object for comparison between campaign requirement and creator post and feedback.",
    instruction="""
    You are an AI assistant on a platform that connects brands and content creators. 
    Brands post their campaigns with, creators apply to promote for brands. 
    When brands accept creators, creators post promotional posts on social media platforms.
    Campaign requirements details are in {campaign_requirement_json}.
    Creator's post details are in {creator_post_json}.
    You must compare creator's post and campaign's requirements by comparing each field in {campaign_requirement_json} and {creator_post_json}, then give me a response.

    IMPORTANT: Your response MUST be ONE valid JSON object matching this structure:
    {
        {"field_1":"give detailed feedback and detailed advice for improvement where creator post doesn't meet campaign requirement in field_1"},
        {"field_2":"give detailed feedback and detailed advice for improvement where creator post doesn't meet campaign requirement in field_2"},
        ...,
        {"field_n":"give detailed feedback and detailed advice for improvement where creator post doesn't meet campaign requirement in field_n"},

    }

    The fields that could be included are:
    - media_format: must match all to be valid and must not have any redundant format
    - start_date: must be after to be valid
    - end_date: must be before to be valid
    - platform: must match all to be valid
    - hashtag: must match all to be valid and must not have any redundant hashtag
    - mention: must match all to be valid and must not have any redundant mention
    - video_length: must match to be valid 
    - text_length: must match to be valid
    - content: must match all to be valid and must not have any redundant content

    Only include fields where creator post doesn't meet campaign requirement in your final response.

    DO NOT include any explanations or additional text outside the JSON response.

    Your response must be in Vietnamese.
    """,
    output_key="compare_result",
    # output_schema=Feedback,
    # disallow_transfer_to_parent=True, 
    # disallow_transfer_to_peers=True
)













# Create the root agent
# compare = LlmAgent(
#     name="compare",
#     model="gemini-2.5-flash-lite",
#     description="Extract a normalized json object for comparison between campaign requirement and creator post.",
#     instruction="""
#     You are an AI assistant on a platform that connects brands and content creators. 
#     Brands post their campaigns with, creators apply to promote for brands. 
#     When brands accept creators, creators post promotional posts on social media platforms.
#     Campaign requirements details are in {campaign_requirement_json}.
#     Creator's post details are in {creator_post_json}.
#     You must compare creator's post and campaign's requirements by comparing each field in {campaign_requirement_json} and {creator_post_json}, then give me a response.

#     IMPORTANT: Your response MUST be a valid JSON object matching this structure:
#     {
#         {"field_1": "name of the field here",
#         "valid_1": "a boolean value that marks the validity of creator post given campaign requirements",
#         "feedback_2": "if creator post is invalid, give feedback on how they can improve it, be detailed about it."},

#         {"field_2": "name of the field here",
#         "valid_2": "a boolean value that marks the validity of creator post given campaign requirements",
#         "feedback_2": "if creator post is invalid, give feedback on how they can improve it, be detailed about it."},
#         .....,
#         {"field_n": "name of the field here",
#         "valid_n": "a boolean value that marks the validity of creator post given campaign requirements",
#         "feedback_n": "if creator post is invalid, give feedback on how they can improve it, be detailed about it."},
    
#     }

#     The fields include (media_format, start_date, end_date, platfrom, hashtag, mention, video_length, text_length, content).
#     media_format can include: video, photo or text.
#     If a field is null in {campaign_requirement_json} and is not null in {creator_post_json}, that field should be marked valid in your output.
#     If a field is null in {campaign_requirement_json} and is null in {creator_post_json}, that field should be null in your output.

#     DO NOT include any explanations or additional text outside the JSON response.
#     """,
#     output_key="compare_result",
# )



