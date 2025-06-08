# 🤖 Chatbot AI - Intelligent Chat Assistant

A beautiful, intelligent chat application built with Streamlit and FastAPI that provides natural conversations with smart web search capabilities.

![Chatbot AI Demo](https://img.shields.io/badge/Status-Active-brightgreen)
![Python](https://img.shields.io/badge/Python-3.8+-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-Latest-red)
![FastAPI](https://img.shields.io/badge/FastAPI-Latest-green)

## ✨ Features

- 💬 **Natural Conversations**: Engage in casual chat without unnecessary web searches
- 🔍 **Smart Web Search**: Automatically searches the web only when current information is needed
- 🧠 **Context Awareness**: Maintains conversation context across messages
- 🎯 **Intelligent Tool Usage**: Only uses search tools when genuinely needed

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- API keys for:
  - Groq API (for LLM)
  - Tavily API (for web search)

### Installation

1. **Clone the repository**

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**
   Create a `.env` file in the root directory:
   ```env
   GROQ_API_KEY=your_groq_api_key_here
   TAVILY_API_KEY=your_tavily_api_key_here
   ```

4. **Run the backend server**
   ```bash
   python app.py
   # or
   uvicorn app:app --host 0.0.0.0 --port 8000
   ```

5. **Run the Streamlit frontend**
   ```bash
   streamlit run streamlit_app.py
   ```

6. **Open your browser**
   Navigate to `http://localhost:8501` to start chatting!

## 📋 Requirements

Create a `requirements.txt` file with these dependencies:

```txt
streamlit
fastapi
uvicorn
langchain-openai
langchain-groq
langchain-core
langchain-community
langgraph
python-dotenv
requests
tavily-python
```

## 🏗️ Architecture

```
┌─────────────────┐    HTTP Requests    ┌─────────────────┐
│   Streamlit     │◄──────────────────► │   FastAPI       │
│   Frontend      │    (Streaming)      │   Backend       │
└─────────────────┘                     └─────────────────┘
         │                                        │
         │                                        ▼
         ▼                              ┌─────────────────┐
┌─────────────────┐                     │   LangGraph     │
│   Beautiful     │                     │   Workflow      │
│   Chat UI       │                     └─────────────────┘
└─────────────────┘                              │
                                                 ▼
                                        ┌─────────────────┐
                                        │  Groq LLM +     │
                                        │  Tavily Search  │
                                        └─────────────────┘
```
## 🧠 AI Intelligence

### Smart Search Logic
The AI is programmed to distinguish between:

**No Search Needed:**
- Casual greetings ("hi", "hello", "how are you")
- General conversation and small talk
- Creative writing requests

**Search Required:**
- Current events and news
- Recent information after training cutoff
- Real-time data (weather, stocks, etc.)
- Specific facts the AI is unsure about
- Recent developments in technology

### Conversation Flow
1. User sends message
2. AI analyzes if web search is needed
3. If needed: Search → Process results → Respond
4. If not needed: Direct intelligent response
5. Context maintained throughout conversation

## ⚙️ Configuration

### Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `GROQ_API_KEY` | Your Groq API key for LLM access | Yes |
| `TAVILY_API_KEY` | Your Tavily API key for web search | Yes |

### Customization

You can customize various aspects:

- **LLM Model**: Change the model in `app.py` (currently using `llama3-70b-8192`)
- **Search Results**: Modify `max_results` in the search tool configuration

## 🔧 API Endpoints

### FastAPI Backend

- `GET /chat_stream/{message}` - Main chat endpoint
  - Parameters:
    - `message` (path): The user's message
    - `checkpoint_id` (query, optional): Conversation ID for context

### Response Format

The API returns Server-Sent Events (SSE) with these event types:

```json
{"type": "checkpoint", "checkpoint_id": "uuid"}
{"type": "search_start", "query": "search query"}
{"type": "content", "content": "response chunk"}
{"type": "search_results", "urls": ["url1", "url2"]}
{"type": "end"}
```

## 🎯 Usage Examples

### Casual Chat (No Search)
```
User: "Hi, how are you?"
Bot: "Hello! I'm doing great, thank you for asking! I'm here and ready to help with whatever you'd like to chat about. How are you doing today?"
```

### Information Request (With Search)
```
User: "What's the latest news about AI developments?"
Bot: 🔍 Searching the web...

📚 Sources:
🔗 Source 1
🔗 Source 2

Based on recent developments, here are the latest AI news highlights...
```
## 🙏 Acknowledgments

- **LangChain & LangGraph** for the AI workflow framework
- **Streamlit** for the beautiful frontend framework
- **FastAPI** for the high-performance backend
- **Groq** for fast LLM inference
- **Tavily** for intelligent web search


*Chatbot AI - Making conversations smarter, one chat at a time.*
