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
            model="google/gemini-2.0-flash-exp:free",
            messages=messages,
            temperature=0.7,
            max_tokens=100
        )
        time.sleep(2)


        print("API Response:", completion)


        if not completion or not hasattr(completion, "choices") or not completion.choices:
            return "Error: No valid response from AI model."


        response = completion.choices[0].message.content if completion.choices[0].message else "Error: Empty response."

        messages.append({"role": "assistant", "content": response})
        return response

    except openai.OpenAIError as e:
        return f"OpenAI API Error: {str(e)}"

    except Exception as e:
        return f"Error: {str(e)}"
