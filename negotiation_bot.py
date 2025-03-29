import openai
import time


client = openai.OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key="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",
)


messages = [
    {
        "role": "system",
        "content": (
            "You are a polite, professional shopkeeper selling premium clothing in minimalistic price and your shop name is Urban Vogue. "
            "Defend prices by emphasizing quality and craftsmanship. "
            "You are only here for bargaining. "
            "After final price is agreed, you can exit the conversation by saying 'Thank you for visiting! Have a great day. 😊'. "
            "Only offer a 10% discount if the customer insists, and 15% if they push further—never more.\n\n"
            "Product Prices:\nT-shirt - $15, Jeans - $40, Jacket - $60, Hoodie - $35, Sweater - $30."
        )
    }
]

def get_bot_response(user_message: str) -> str:
    """Processes user input and returns the chatbot's response."""
    if user_message.lower() in ["exit", "quit", "bye"]:
        return "Thank you for visiting! Have a great day. 😊"

    messages.append({"role": "user", "content": user_message})

    try:
        completion = client.chat.completions.create(
            model="google/gemini-2.5-pro-exp-03-25:free",
            messages=messages,
            temperature=0.7,
            max_tokens=100
        )
        time.sleep(2)


        response = completion.choices[0].message.content
        messages.append({"role": "assistant", "content": response})
        return response

    except Exception as e:
        return f"Error: {str(e)}"
