def generate_idea_prompt(t3_info, business_profile=None):
    target = t3_info.target
    topic = t3_info.topic
    tone = t3_info.tone

    # SYSTEM message — static business info
    name = industry = description = uniqueness = goal = audience = ""
    if business_profile:
        name = business_profile.name
        industry = business_profile.industry
        description = business_profile.description
        uniqueness = business_profile.uniqueness
        tagline = business_profile.tagline

    system_prompt = f"""
You are EchoVibe, a helpful and creative AI agent that generates high-quality content campaign ideas.

Business Profile:
- Name: {name}
- Industry: {industry}
- Description: {description}
- Unique Value Proposition: {uniqueness}
- Tag Line: {tagline}

Your job is to come up with 3 unique, brand-aligned, trend-aware creative ideas for social media campaigns. 
Each idea must include: 
- idea_title
- angle
- relevance_to_trends
- keyword_focus

Your ideas should be clear, engaging, and tailored to the specified audience and tone.
""".strip()

    # USER message — dynamic prompt based on T3
    user_prompt = f"""
Campaign Direction:
- Target: {target}
- Topic: {topic}
- Tone: {tone}

Instructions:
1. Generate exactly 3 creative campaign ideas.
2. Each idea should include:
   - idea_title: a short and catchy title,
   - angle: the creative perspective or storytelling lens,
   - relevance_to_trends: how it connects with current social media or cultural trends,
   - keyword_focus: 3–5 relevant keywords or hashtags that the post can focus on.
3. Make each idea distinct in direction, but aligned with the brand's voice and tone.
4. Output as a list of JSON objects.
""".strip()

    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt}
    ]

    return messages
