import requests
import json
from constants import PAI_API_KEY, PAI_API_END_POINT, REPORT_FORMAT
from transformers import post_text_transformer


def call_llm_pai(messages):
        # file_path = "pai_data.json"
        # post_json_path = "pai_posts.json"

        headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {PAI_API_KEY}"  # If using an API key
        }

        data = {
            "model": "llama3.1",
            "messages": messages,
            "stream": True,
            "temperture": 0.78
        }

        response = requests.post(PAI_API_END_POINT, headers=headers, json=data)
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)
       
        full_text = ""

        for line in response.iter_lines():
            if line:
                try:
                    chunk = json.loads(line)
                    content = chunk.get("message", {}).get("content", "")
                    print(content, end="", flush=True)  # optional: stream it live
                    full_text += content

                    if chunk.get("done"):
                        break
                except json.JSONDecodeError:
                    continue  # skip malformed lines

        print("\n\nFull response received:\n")

        json_text = post_text_transformer(full_text)
        return json_text

        # print(full_text)
        # with open(file_path, "wb") as f:
        #         f.write(json.dumps(data).encode('utf-8'))
        #         print("content added in " + file_path)
        
        # with open(post_json_path, "wb") as f:
        #         f.write(json.dumps(json_text).encode('utf-8'))
        #         print("content added in " + post_json_path)
        
        # with open(file_path, "rb") as document_file:
        #     files = {"file": document_file}
        

        # if REPORT_FORMAT == "json":
        #     try:
        #         report_data = response.json()
        #         print(json.dumps(report_data, indent=4))  # Pretty print the JSON response
        #     except json.JSONDecodeError:
        #         print("API returned a non-JSON response.")
        #         print(response.text)
        # elif REPORT_FORMAT == "html" or REPORT_FORMAT == "doc":
        #     # Handle PDF or DOC download here.  You'd need to save the content to a file.
        #     with open("pai_report.json", "w") as f:
        #         f.write(full_text)
        #     print("Report downloaded as pai_report.txt")
        # else:
        #     print("Unsupported report format")
    
        # return full_text