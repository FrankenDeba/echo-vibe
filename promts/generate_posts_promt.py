from datetime import datetime, timedelta
import calendar

def format_campaign_idea(business_info, campaign_ideas):
    # Header with business information
    formatted_text = f"**Campaign Ideas for {business_info.name}**\n\n"
    formatted_text += f"**Tagline:** *{business_info.tagline}*\n\n"
    formatted_text += f"**Description:** {business_info.description}\n\n"
 
    # Format each campaign idea
    for i, idea in enumerate(campaign_ideas, 1):
        formatted_text += f"{i}. **Idea Title:** *{idea.idea_title}*\n"
        formatted_text += f"   - **Angle:** {idea.angle}\n"
        formatted_text += f"   - **Relevance to Trends:** {idea.relevance_to_trends}\n"
        formatted_text += f"   - **Keyword Focus:** {', '.join(idea.keyword_focus)}\n\n"

    return formatted_text

def generate_posts_prompt(selected_ideas,t3_info, business_info, num_posts=3):

    # SYSTEM message - defines assistant's role
    system_prompt = (
        "You are EchoVibe, a helpful and creative AI agent that generates engaging, brand-aligned social media posts "
        "based on Business Overview, Campaign Plan. "
        "Follow given instructions properly and output the posts in structured JSON format, where each post includes: "
          "caption: a fun, bold, highly engaging post message with emojis, hooks.\n"
        "hash_tags: a array of highly trending hashtags.\n"
        "media: {\n"
        "  type: ' type of post media. image/video/etc',\n"
        "  description: {\n"
        "    - image: a descriptive prompt for AI-generated or description of real image, aesthetic,\n"
        "    - video_storyboard: a creative idea for a short video or reel,\n"
        "    - voiceover_or_song: catchy phrase for overlay or trending song in hindi/english,\n"
        "    - tips: 2-3 creative suggestions for visuals, colors, or framing to stand out on social platforms.\n"
        "  }\n"
        "}"
        "Additionally, use the selected ideas and transform them into detailed posts."
    )

    # USER message - the full request context
    user_prompt = f"""
        Campaign Info:
        - Tone: {t3_info.tone}
        - Target: {t3_info.target}
        - Topic: {t3_info.topic}
        - Number of Posts Required: {num_posts}

        Business Info:
        - Name: {business_info.name}
        - Industry: {business_info.industry}
        - Tag Line: {business_info.tagline}
        - Description: {business_info.description}
        - Unique Value: {business_info.uniqueness}

        {format_campaign_idea(business_info,selected_ideas)}
        

        Instructions:
        1. From the selected ideas, generate {num_posts} social media posts.
        2. Each post should be creative, relevant, and consistent with the business information.
        3.** Use the Campaign Ideas as a base and expand on them to create a full post, including:**
            - An attention-grabbing caption
            - A detailed description (post_content)
            - An image description for visual appeal (image_text)
            - **3-4 relevant and trendy hashtags**
        4. Avoid repetition, maintain variety, and ensure the tone stays engaging and professional.
        5. **Use the Business Info as a guiding filter — do NOT generate any idea that contradicts or harms the brand's values, industry relevance, or audience expectations.**
        6. Ensure that each post aligns with the campaign target, topic and tone.
        7. Output as a list of JSON objects.
        """

    # Message list format (for models expecting chat messages)
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt.strip()}
    ]

    print(f"The generated prompt message: \n \n {messages} \n")

    return messages
