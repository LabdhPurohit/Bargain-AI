# 🛍️ Bargaining Chatbot API

This project implements a **Negotiation Chatbot** using **FastAPI** and an LLM-based model. The chatbot mimics a shopkeeper who negotiates with customers.

## 📂 Project Structure
- `process_data.py` → Preprocesses and structures bargaining conversations into JSON.
- `negotiation_bot.py` → Handles negotiation logic and calls the LLM for responses.
- `api.py` → FastAPI backend for handling chatbot API requests.

## 🚀 Setup Instructions

### 1️⃣ Install Dependencies
Ensure you have **Python 3.8+** installed.  
Run the following command:

```sh
pip install -r requirements.txt
```

### 2️⃣ Run the API Server
Start the FastAPI server using:

```sh
python api.py
```

### 3️⃣ Test the Chatbot API

Use **Postman, Curl, or any API tool** to interact with the chatbot.

#### ✅ API Endpoint:
```
POST http://localhost:8000/chat/
```

#### 🔹 Example Request:
```json
{
  "message": "Can I get a discount on this?"
}
```

#### 🔹 Example Response:
```json
{
  "shopkeeper": "This is a premium item. I can offer a 10% discount."
}
```

## 🎥 Demo (Optional)
If available, attach a demo video showcasing the chatbot in action.

---

## 🤝 Contributing
Feel free to open issues or submit pull requests for improvements!

