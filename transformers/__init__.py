import json
import re
def post_text_transformer(raw_text):
   # Regex to extract all JSON-like blocks
    json_blocks = re.findall(r"```json\s*({.*?})\s*```", raw_text, re.DOTALL)

    cleaned_posts = []
    for block in json_blocks:
        try:
            # Fix common encoding issues like �
            cleaned_block = block.replace("�", "'").strip()
            data = json.loads(cleaned_block)
            cleaned_posts.append(data)
        except json.JSONDecodeError as e:
            print(f"Error parsing block: {e}")
            continue

    return cleaned_posts
