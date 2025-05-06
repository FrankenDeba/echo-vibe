from llm import call_llm_pai  # Function to call the LLM API
import requests  # For making API calls to the LLM
import threading  # For running the loading animation in parallel with the API call
import time  # For implementing the loading animation
from promts.generate_posts_promt import generate_posts_prompt  # Importing the function to generate prompts for LLM

# Function for displaying a loading animation while the post is being generated
def loading_animation(stop_event):
    while not stop_event.is_set():  # Continue as long as the stop event is not triggered
        for dot_count in range(1, 4):  # Displays 1-3 dots for animation
            print("\rGenerating your posts" + "." * dot_count + " " * (3 - dot_count), end="")
            time.sleep(0.5)  # Pauses briefly between dots
    print("\rPost generated!            ")  # Final message when post generation is complete

data = {
    "model": "llama3.1",
    "messages": [
        {
            "role": "system",
            "content": "You are EchoVibe, a helpful and creative AI agent that generates engaging, brand-aligned social media posts based on Business Overview, Campaign Plan. Output posts in a visually appealing HTML format with professional CSS styles."
        },
        {
            "role": "user",
            "content": {
                "Business Overview": {
                    "Name": "Echo-Vibe",
                    "Industry": "AI-powered Social Media Strategy and Content Creation",
                    "Description": "Echo-Vibe is an AI-driven platform that helps businesses create engaging, brand-aligned social media content. We generate personalized posts based on business goals, audience insights, and content performance history, allowing companies to boost their online presence and engage their audience effectively. Our goal is to simplify content creation with cutting-edge AI technology, offering businesses the ability to post consistently and with impact.",
                    "Unique Value": "Echo-Vibe stands out by combining advanced AI with personalized content creation. We don't just generate generic posts; we tailor each piece of content based on the specific goals, target audience, and trends relevant to the business. Additionally, our platform continuously learns and adapts, ensuring that the content gets better and more impactful over time. By aligning every post with business values and performance insights, we help businesses grow their social media presence authentically and efficiently."
                },
                "Campaign Plan": {
                    "Topic Focus": [
                        "AI-driven marketing: How businesses can leverage AI to stay ahead.",
                        "Efficiency & Time-saving: Demonstrating how businesses can save time and resources using Echo-Vibe.",
                        "Personalization: Highlighting how AI can generate personalized, brand-aligned content.",
                        "Engagement: Tips on how AI-generated content helps boost customer engagement and interaction.",
                        "Trending topics: We can tie some posts into popular events or seasonal trends, like 'AI in marketing during Q4' or 'Leveraging AI for holiday season sales campaigns.'"
                    ],
                    "Specific Angle": [
                        "AI-Powered Efficiency: 'Echo-Vibe creates content faster, saving you time while keeping your brand ahead of the competition.'",
                        "Personalized Content: 'Tailored posts that match your unique brand voice, reflecting your business’s personality.'",
                        "Real-time Trends: 'Stay relevant by adapting content to trending topics and global events with Echo-Vibe.'",
                        "Maximized Engagement: 'Generate posts that boost engagement, backed by AI optimized for social media algorithms.'",
                        "Scalable Content Creation: 'Whether small or large, Echo-Vibe helps you scale content creation effortlessly.'",
                        "AI & Sustainability: 'Echo-Vibe reduces resource waste, offering sustainable content creation powered by AI.'"
                    ],
                    "Date Range": "2025-05-01 to 2025-05-31",
                    "Goal": "The main goal for next month is to expand Echo-Vibe's customer base by promoting our AI-powered content generation platform. We aim to demonstrate how businesses can streamline their social media content creation while improving engagement. We will focus on increasing awareness about Echo-Vibe’s unique capabilities and how it helps businesses stay consistent and relevant on social media. We plan to encourage sign-ups for our service with targeted campaigns and calls to action like 'Start your free trial today!'",
                    "Target Audience": "Our target audience includes small to medium-sized business owners, marketing managers, and social media managers who are looking to optimize their content creation process. This includes businesses across various industries such as retail, hospitality, food and beverage, health and wellness, and professional services. These individuals are interested in leveraging AI to improve their social media engagement, save time, and create more personalized content without the need for extensive resources or a dedicated in-house team.",
                    "Number of Posts Required": 10
                },
                "Instructions": [
                    "Generate 10 high-quality, varied social media posts.",
                    "Posts should be creative, relevant, and aligned with the business’s tone and objectives.",
                    "Include relevant 3-4 hashtags.",
                    "Mention space for images (describe the expected image).",
                    "Avoid repetition and keep the tone engaging.",
                    "Number the posts clearly."
                ]
            }
        }
    ],
    "stream": True,
    "temperature": 0.78
}


def transform_sample_data(data):
    # Extract the main content
    user_content = data["messages"][1]["content"]

    # Extract business overview details
    business_overview = user_content["Business Overview"]
    industry = business_overview["Industry"]
    description = business_overview["Description"]
    name = business_overview["Name"]
    uniqueness = business_overview["Unique Value"]

    # Extract campaign plan
    campaign_plan = user_content["Campaign Plan"]
    topic_focus = campaign_plan["Topic Focus"]
    topic_angle = campaign_plan["Specific Angle"]
    from_date, to_date = campaign_plan["Date Range"].split(" to ")
    goal = campaign_plan["Goal"]
    audience = campaign_plan["Target Audience"]
    num_posts = campaign_plan["Number of Posts Required"]

    # Transform into the expected input format
    business_info = (goal, audience)
    industry_info = (industry, description, name, uniqueness)
    topic_info = (topic_focus, topic_angle)

    return business_info, industry_info, topic_info, from_date.strip(), to_date.strip(), num_posts


print("\n🔄 EchoVibe is preparing to generate your content...")
stop_event = threading.Event()  # Event to signal when the loading animation should stop
loader_thread = threading.Thread(target=loading_animation, args=(stop_event,))  # Thread for the loading animation
loader_thread.start()  # Start the loader animation in a separate thread
try:

    # Assuming `data` is your sample dataset
    business_info, industry_info, topic_info, from_date, to_date, num_posts = transform_sample_data(data)
    messages = generate_posts_prompt(business_info, industry_info, topic_info, from_date, to_date, num_posts)
    # Calling the LLM API to generate posts based on the provided prompt
    call_llm_pai(messages)

except requests.exceptions.RequestException as e:
    print(f"Error sending data to API: {e}")  # Error handling for API requests

stop_event.set()  # Stop the loading animation
loader_thread.join()  # Wait for the loader thread to finish


