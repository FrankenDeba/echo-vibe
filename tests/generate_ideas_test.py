from promts.generate_ideas_promt import generate_idea_prompt
from promts.generate_posts_promt import generate_posts_prompt
from datetime import datetime, timedelta
from llm import call_llm_pai  # Function to call the LLM API

t3_info = (
    "Teenagers aged 14-19",
    "Launching a new programming coaching class",
    "Attractive, Appealing, Value for Money"
)

business_info = (
    "Drive enrollments for new coaching programs",
    "Teenagers and their parents"
)

industry_info = (
    "EdTech",
    "We provide coding education through live classes and hands-on projects",
    "CodeCampX",
    "Interactive, affordable, and community-driven learning"
)

# Call the function
messages = generate_idea_prompt(t3_info, business_info, industry_info)



# Print result
for message in messages:
    print(f"{message['role'].upper()}:\n{message['content']}\n{'-'*40}")




# 1. Mock selected_ideas from the idea generation output
selected_ideas = [
    {
        "idea_title": "Code Your Dream",
        "angle": "Dream Big, Achieve More",
        "relevance_to_trends": "Motivation, Empowerment, Self-Improvement",
        "keyword_focus": ["#CodeYourDream", "#CodingGoals", "#FutureOfWork"]
    }
]

# 2. Optional business and industry info
business_info = ("Inspire teens through coding", "Teenagers aged 14–19")
industry_info = ("EdTech", "An online coding camp for teens", "CodeCampX", "Interactive, affordable, and community-driven learning")

# 3. Optional topic_info (if not passed, you could derive from `selected_ideas`)
# But since `selected_ideas` replaces this, we can pass None or derive like this:
topic_focus = selected_ideas[0]["idea_title"]
topic_angle = selected_ideas[0]["angle"]
topic_info = (topic_focus, topic_angle)

# 4. Date range
from_date = datetime.today().strftime('%Y-%m-%d')
to_date = (datetime.today() + timedelta(days=15)).strftime('%Y-%m-%d')

# 5. Generate messages
messages = generate_posts_prompt(
    selected_ideas=selected_ideas,
    business_info=business_info,
    industry_info=industry_info,
    topic_info=topic_info,
    from_date=from_date,
    to_date=to_date,
    num_posts=3
)

# 6. Output the generated prompts for testing
for message in messages:
    print(f"\n--- {message['role'].upper()} ---")
    print(message["content"])

print("\n \n Generating posts...\n")
call_llm_pai(messages)
