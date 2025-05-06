import requests  # For making API calls to the LLM
from promts.generate_posts_promt import generate_posts_prompt  # Importing the function to generate prompts for LLM
from questions import ask_business_questions, ask_industry_details, ask_number_of_posts, ask_post_topic_questions, get_valid_date_range  # Functions to gather user inputs
from llm import call_llm_pai  # Function to call the LLM API
import time  # For implementing the loading animation
import threading  # For running the loading animation in parallel with the API call

REPORT_FORMAT = "html"  # The format for report output (could be doc, json, or html)

# Function for displaying a loading animation while the post is being generated
def loading_animation(stop_event):
    while not stop_event.is_set():  # Continue as long as the stop event is not triggered
        for dot_count in range(1, 4):  # Displays 1-3 dots for animation
            print("\rGenerating your post" + "." * dot_count + " " * (3 - dot_count), end="")
            time.sleep(0.5)  # Pauses briefly between dots
    print("\rPost generated!            ")  # Final message when post generation is complete

def main():
    print("\n🤖 Welcome to **EchoVibe** — Your AI-Powered Social Media Strategist\n")
    print("Let's get to know your brand and goals so we can generate impactful content.\n")

    # Gathering necessary inputs from the user
    industry_info = ask_industry_details()  # Industry-related details
    business_info = ask_business_questions()  # General business information
    topic_info = ask_post_topic_questions()  # Questions related to post topics
    from_date, to_date = get_valid_date_range()  # Date range for the campaign
    num_posts = ask_number_of_posts()  # Number of posts to generate

    # Summarizing the input details for confirmation
    print("\n✅ All inputs collected. Summary by EchoVibe:")
    print(f"Business Qs: {business_info}")
    print(f"Industry: {industry_info[0]}, Description: {industry_info[1]}")
    print(f"Post Topic Qs: {topic_info}")
    print(f"Date Range: {from_date} to {to_date}")
    print(f"Number of Posts: {num_posts}")

    print("\n🔄 EchoVibe is preparing to generate your content...")

    # Generating the prompt to send to the LLM
    messages = generate_posts_prompt(business_info, industry_info, topic_info, from_date, to_date, num_posts)

    # Displaying the generated prompt for debugging/confirmation
    print("here is the Prompt\n")
    print(messages)

    stop_event = threading.Event()  # Event to signal when the loading animation should stop
    loader_thread = threading.Thread(target=loading_animation, args=(stop_event,))  # Thread for the loading animation
    loader_thread.start()  # Start the loader animation in a separate thread

    try:
        # Calling the LLM API to generate posts based on the provided prompt
        call_llm_pai(messages)

    except requests.exceptions.RequestException as e:
        print(f"Error sending data to API: {e}")  # Error handling for API requests
    
    stop_event.set()  # Stop the loading animation
    loader_thread.join()  # Wait for the loader thread to finish

# Calling the main function to execute the program
main()
