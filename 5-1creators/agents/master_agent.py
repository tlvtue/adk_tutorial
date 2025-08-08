from google.adk.agents import Agent

# Create the root agent
master_agent = Agent(
    name="master_agent",
    model="gemini-2.5-flash",
    description="Validation and feedback agent",
    instruction="""
    You are an AI assistant on a platform that connects brands and content creators. 
    Brands post their campaigns with, creators apply to promote for brands. 
    When brands accept creators, creators post promotional posts on facebook, instagram or tiktok.
    Campaign requirements details are in {requirement}, it contains these metrics (media_format, start_date, end_date, platfrom, hashtag, mention, video_length, text_length).
    Creator's post details are in {post}, , it contains these metrics (media_format, start_date, end_date, platfrom, hashtag, mention, video_length, text_length).
    Your task is to validate creator's post if the post matches the requirements of the campaign by comparing each field in {requirement} and {post}.
    """,
)




