import datetime

def ask_business_questions():
    print("Answer the following about the your goal")
    q1 = input("1. What is the main goal of for next month?")
    q2 = input("2. Who is your target audience? ")
    return q1, q2

def ask_industry_details():
    print("Answer the following questions about your business:")
    name = input("Enter name of your business/company ")
    industry = input("Enter your industry (e.g., fashion, tech, food): ")
    description = input("Write a short description of your business: ")
    uniqueness = input("3. What makes your business unique? ")
    return industry, description ,name, uniqueness

def ask_post_topic_questions():
    print("Answer the following about the post topic:")
    topic_q1 = input("1. What topic do you want to focus on in posts? ")
    topic_q2 = input("2. Any specific themes or angles for this topic? ")
    return topic_q1, topic_q2

def get_valid_date_range():
    print("Enter the date range for the campaign (minimum 30 days):")
    while True:
        from_date_str = input("From date (YYYY-MM-DD): ")
        to_date_str = input("To date (YYYY-MM-DD): ")
        try:
            from_date = datetime.datetime.strptime(from_date_str, "%Y-%m-%d")
            to_date = datetime.datetime.strptime(to_date_str, "%Y-%m-%d")
            delta = (to_date - from_date).days
            if delta >= 30:
                return from_date_str, to_date_str
            else:
                print("❌ Duration must be at least 30 days. Try again.")
        except ValueError:
            print("❌ Invalid date format. Please try again.")

def ask_number_of_posts():
    while True:
        try:
            num = int(input("How many posts do you want to generate? (10–21): "))
            if 10 <= num <= 21:
                return num
            else:
                print("❌ Enter a number between 10 and 21.")
        except ValueError:
            print("❌ Please enter a valid number.")