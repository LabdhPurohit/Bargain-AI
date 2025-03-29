import json
import re

def preprocess_text(text):
    """Lowercase, remove punctuation, and strip spaces."""
    text = text.lower().strip()
    text = re.sub(r'[^\w\s\$]', '', text)
    return text

def parse_conversations(file_path):
    """Convert raw chat logs into structured JSON format."""
    conversations = []
    
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    user_message, bot_response = None, None

    for line in lines:
        line = line.strip()
        if line.startswith("User:"):
            if user_message and bot_response:
                conversations.append({"user_message": preprocess_text(user_message),
                                      "bot_response": preprocess_text(bot_response)})
            user_message = line.replace("User:", "").strip()
        elif line.startswith("Bot:"):
            bot_response = line.replace("Bot:", "").strip()
    
    if user_message and bot_response:
        conversations.append({"user_message": preprocess_text(user_message),
                              "bot_response": preprocess_text(bot_response)})

    return conversations

def save_json(data, output_file):
    """Save structured data to JSON."""
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)

if __name__ == "__main__":
    input_file = "negotiation_raw.txt"
    output_file = "negotiation_data.json"
    structured_data = parse_conversations(input_file)
    save_json(structured_data, output_file)
    print("Data processing complete. Saved to", output_file)
