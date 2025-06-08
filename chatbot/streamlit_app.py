import streamlit as st
import requests
import json
import time
import random
from datetime import datetime

st.set_page_config(
    page_title="Chatbot AI - Your Intelligent Assistant", 
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# === Enhanced Beautiful Styling ===
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');
@import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;500&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');

/* Hide Streamlit elements */
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}
.stDeployButton {display:none;}

/* Main app styling with animated background */
.stApp {
    background: linear-gradient(-45deg, #667eea, #764ba2, #f093fb, #f5576c, #4facfe, #00f2fe);
    background-size: 400% 400%;
    animation: gradientShift 15s ease infinite;
    font-family: 'Inter', sans-serif;
    min-height: 100vh;
}

@keyframes gradientShift {
    0% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}

/* Glassmorphism effect */
.glass-effect {
    background: rgba(255, 255, 255, 0.15);
    backdrop-filter: blur(20px);
    border-radius: 20px;
    border: 1px solid rgba(255, 255, 255, 0.2);
    box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.15);
}

/* Ensure full height coverage */
html, body, [data-testid="stAppViewContainer"] {
    background: transparent;
    min-height: 100vh;
}

.main .block-container {
    padding-top: 1rem;
    padding-bottom: 1rem;
    max-width: 1200px;
}

/* Enhanced header styling */
.main-header {
    text-align: center;
    font-family: 'Poppins', sans-serif;
    font-weight: 800;
    font-size: 4rem;
    background: linear-gradient(45deg, #fff, #f0f8ff, #e6f3ff);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    margin-bottom: 0.5rem;
    text-shadow: 0 4px 20px rgba(255, 255, 255, 0.3);
    animation: glow 2s ease-in-out infinite alternate;
}

@keyframes glow {
    from { text-shadow: 0 4px 20px rgba(255, 255, 255, 0.3); }
    to { text-shadow: 0 4px 30px rgba(255, 255, 255, 0.6); }
}

.sub-header {
    text-align: center;
    font-size: 1.2rem;
    color: rgba(255, 255, 255, 0.9);
    font-weight: 400;
    margin-bottom: 2rem;
    text-shadow: 0 2px 10px rgba(0, 0, 0, 0.2);
}

.compact-header {
    font-size: 2.5rem !important;
    margin-bottom: 1rem !important;
}

.compact-sub {
    font-size: 1rem !important;
    margin-bottom: 1.5rem !important;
}

/* Enhanced chat container */
.chat-container {
    background: rgba(255, 255, 255, 0.1);
    backdrop-filter: blur(25px);
    border-radius: 25px;
    padding: 2.5rem;
    margin: 1.5rem 0;
    box-shadow: 0 25px 50px rgba(0, 0, 0, 0.1);
    border: 1px solid rgba(255, 255, 255, 0.3);
    transition: all 0.3s ease;
}

.chat-container:hover {
    transform: translateY(-2px);
    box-shadow: 0 30px 60px rgba(0, 0, 0, 0.15);
}

/* Enhanced message bubbles */
.user-message {
    display: flex;
    justify-content: flex-end;
    margin: 1.5rem 0;
    animation: slideInRight 0.4s cubic-bezier(0.25, 0.46, 0.45, 0.94);
}

.user-bubble {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
    padding: 1.2rem 1.5rem;
    border-radius: 25px 25px 8px 25px;
    max-width: 75%;
    font-size: 1rem;
    font-weight: 500;
    box-shadow: 0 8px 25px rgba(102, 126, 234, 0.4);
    word-wrap: break-word;
    position: relative;
    transition: all 0.3s ease;
}

.user-bubble:hover {
    transform: scale(1.02);
    box-shadow: 0 12px 35px rgba(102, 126, 234, 0.5);
}

.user-bubble::before {
    content: '';
    position: absolute;
    bottom: -2px;
    right: -2px;
    width: 0;
    height: 0;
    border: 8px solid transparent;
    border-top-color: #764ba2;
    border-left-color: #764ba2;
}

.assistant-message {
    display: flex;
    justify-content: flex-start;
    margin: 1.5rem 0;
    animation: slideInLeft 0.4s cubic-bezier(0.25, 0.46, 0.45, 0.94);
}

.assistant-bubble {
    background: linear-gradient(135deg, rgba(255, 255, 255, 0.95) 0%, rgba(248, 250, 255, 0.95) 100%);
    color: #2d3748;
    padding: 1.2rem 1.5rem;
    border-radius: 25px 25px 25px 8px;
    max-width: 75%;
    font-size: 1rem;
    font-weight: 400;
    box-shadow: 0 8px 25px rgba(0, 0, 0, 0.08);
    border: 1px solid rgba(255, 255, 255, 0.3);
    word-wrap: break-word;
    position: relative;
    backdrop-filter: blur(10px);
    transition: all 0.3s ease;
}

.assistant-bubble:hover {
    transform: scale(1.02);
    box-shadow: 0 12px 35px rgba(0, 0, 0, 0.12);
}

.assistant-bubble::before {
    content: '';
    position: absolute;
    bottom: -2px;
    left: -2px;
    width: 0;
    height: 0;
    border: 8px solid transparent;
    border-top-color: rgba(248, 250, 255, 0.95);
    border-right-color: rgba(248, 250, 255, 0.95);
}

/* Enhanced search bubble */
.search-bubble {
    background: linear-gradient(135deg, #ffeaa7 0%, #fdcb6e 100%);
    color: #2d3748;
    padding: 1rem 1.25rem;
    border-radius: 20px;
    max-width: 60%;
    font-size: 0.9rem;
    font-weight: 600;
    box-shadow: 0 8px 25px rgba(253, 203, 110, 0.4);
    border: 1px solid rgba(253, 203, 110, 0.3);
    margin-bottom: 0.5rem;
    animation: pulse 2s infinite;
    display: flex;
    align-items: center;
    gap: 0.5rem;
}

@keyframes pulse {
    0%, 100% { opacity: 1; }
    50% { opacity: 0.8; }
}

/* Enhanced animations */
@keyframes slideInRight {
    from { 
        transform: translateX(100px) scale(0.8); 
        opacity: 0; 
    }
    to { 
        transform: translateX(0) scale(1); 
        opacity: 1; 
    }
}

@keyframes slideInLeft {
    from { 
        transform: translateX(-100px) scale(0.8); 
        opacity: 0; 
    }
    to { 
        transform: translateX(0) scale(1); 
        opacity: 1; 
    }
}

@keyframes fadeInUp {
    from { 
        opacity: 0; 
        transform: translateY(30px); 
    }
    to { 
        opacity: 1; 
        transform: translateY(0); 
    }
}

/* Enhanced welcome animation */
.welcome-container {
    text-align: center;
    color: white;
    padding: 4rem 2rem;
    animation: fadeInUp 1s ease-out;
}

.welcome-text {
    font-family: 'Poppins', sans-serif;
    font-size: 2.5rem;
    font-weight: 600;
    margin: 1.5rem 0;
    text-shadow: 0 4px 15px rgba(0, 0, 0, 0.3);
    animation: fadeInUp 0.8s ease-out;
}

.welcome-subtitle {
    font-size: 1.2rem;
    font-weight: 300;
    opacity: 0.9;
    margin-bottom: 2rem;
}

/* Enhanced sidebar styling */
.sidebar-content {
    background: rgba(255, 255, 255, 0.15);
    backdrop-filter: blur(15px);
    border-radius: 20px;
    padding: 2rem;
    margin: 1rem 0;
    border: 1px solid rgba(255, 255, 255, 0.2);
    box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
}

.sidebar-title {
    color: white;
    font-size: 1.8rem;
    font-weight: 700;
    margin-bottom: 1.5rem;
    text-align: center;
    text-shadow: 0 2px 10px rgba(0, 0, 0, 0.2);
}

/* Enhanced button styling */
.stButton > button {
    background: linear-gradient(135deg, rgba(255, 255, 255, 0.2) 0%, rgba(255, 255, 255, 0.1) 100%);
    color: white;
    border: 1px solid rgba(255, 255, 255, 0.3);
    border-radius: 15px;
    padding: 0.75rem 1.5rem;
    font-weight: 600;
    font-size: 1rem;
    transition: all 0.3s ease;
    backdrop-filter: blur(10px);
    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
}

.stButton > button:hover {
    transform: translateY(-3px) scale(1.05);
    box-shadow: 0 8px 25px rgba(0, 0, 0, 0.2);
    background: linear-gradient(135deg, rgba(255, 255, 255, 0.3) 0%, rgba(255, 255, 255, 0.2) 100%);
}

/* Enhanced chat input styling */
.stChatInput > div > div > div > div {
    background: rgba(255, 255, 255, 0.15);
    border-radius: 25px;
    border: 2px solid rgba(255, 255, 255, 0.2);
    backdrop-filter: blur(15px);
    color: white;
    font-size: 1rem;
    padding: 1rem 1.5rem;
}

.stChatInput > div > div > div > div:focus-within {
    border-color: rgba(255, 255, 255, 0.5);
    box-shadow: 0 0 25px rgba(255, 255, 255, 0.2);
    transform: scale(1.02);
}

.stChatInput input::placeholder {
    color: rgba(255, 255, 255, 0.7);
}

/* Code blocks styling */
pre {
    background: rgba(0, 0, 0, 0.8) !important;
    border-radius: 10px !important;
    padding: 1rem !important;
    border: 1px solid rgba(255, 255, 255, 0.1) !important;
}

code {
    font-family: 'JetBrains Mono', monospace !important;
    font-size: 0.9rem !important;
}

/* Links styling */
a {
    color: #667eea;
    text-decoration: none;
    font-weight: 600;
    transition: all 0.3s ease;
}

a:hover {
    color: #4facfe;
    text-decoration: underline;
    text-shadow: 0 2px 10px rgba(102, 126, 234, 0.3);
}

/* Enhanced scrollbar */
::-webkit-scrollbar {
    width: 12px;
}

::-webkit-scrollbar-track {
    background: rgba(255, 255, 255, 0.1);
    border-radius: 10px;
}

::-webkit-scrollbar-thumb {
    background: linear-gradient(45deg, rgba(255, 255, 255, 0.3), rgba(255, 255, 255, 0.5));
    border-radius: 10px;
    border: 2px solid transparent;
    background-clip: content-box;
}

::-webkit-scrollbar-thumb:hover {
    background: linear-gradient(45deg, rgba(255, 255, 255, 0.5), rgba(255, 255, 255, 0.7));
}

/* Status indicators */
.status-indicator {
    display: inline-flex;
    align-items: center;
    gap: 0.5rem;
    padding: 0.5rem 1rem;
    background: rgba(255, 255, 255, 0.1);
    border-radius: 20px;
    margin: 0.5rem 0;
    font-size: 0.9rem;
    color: white;
    backdrop-filter: blur(10px);
}

.typing-indicator {
    display: inline-flex;
    align-items: center;
    gap: 0.25rem;
}

.typing-dot {
    width: 6px;
    height: 6px;
    background: #667eea;
    border-radius: 50%;
    animation: typingDots 1.4s infinite ease-in-out;
}

.typing-dot:nth-child(2) { animation-delay: 0.2s; }
.typing-dot:nth-child(3) { animation-delay: 0.4s; }

@keyframes typingDots {
    0%, 80%, 100% { opacity: 0.3; transform: scale(0.8); }
    40% { opacity: 1; transform: scale(1); }
}

/* Responsive design */
@media (max-width: 768px) {
    .main-header { font-size: 2.5rem; }
    .compact-header { font-size: 2rem !important; }
    .user-bubble, .assistant-bubble { max-width: 90%; }
    .chat-container { padding: 1.5rem; margin: 1rem 0; }
    .welcome-text { font-size: 2rem; }
}
</style>
""", unsafe_allow_html=True)

# === Session State ===
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
if "first_visit" not in st.session_state:
    st.session_state.first_visit = True
if "first_message_sent" not in st.session_state:
    st.session_state.first_message_sent = False
if "checkpoint_id" not in st.session_state:
    st.session_state.checkpoint_id = None
if "conversation_count" not in st.session_state:
    st.session_state.conversation_count = 0

# === Header ===
header_class = "compact-header" if st.session_state.first_message_sent else ""
sub_class = "compact-sub" if st.session_state.first_message_sent else ""

st.markdown(f"""
<div class="main-header {header_class}">🤖 Chatbot AI</div>
<div class="sub-header {sub_class}">Your intelligent conversation partner powered by advanced AI</div>
""", unsafe_allow_html=True)

# === Enhanced Sidebar ===
with st.sidebar:
    st.markdown("""
    <div class="sidebar-content">
        <div class="sidebar-title">🤖 Chatbot AI</div>
        <div style="text-align: center; color: rgba(255,255,255,0.8); margin-bottom: 1.5rem;">
            <div style="font-size: 0.9rem;">Version 2.0</div>
            <div style="font-size: 0.8rem;">Powered by Groq & Tavily</div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("🆕 New Chat", use_container_width=True):
            st.session_state.chat_history = []
            st.session_state.checkpoint_id = None
            st.session_state.first_visit = True
            st.session_state.first_message_sent = False
            st.session_state.conversation_count += 1
            st.rerun()
    
    with col2:
        if st.button("🔄 Refresh", use_container_width=True):
            st.rerun()
    
    # Stats
    st.markdown(f"""
    <div class="sidebar-content">
        <h4 style="color: white; margin-bottom: 1rem; text-align: center;">📊 Session Stats</h4>
        <div style="color: rgba(255,255,255,0.8); font-size: 0.9rem; text-align: center;">
            <div>💬 Messages: {len(st.session_state.chat_history)}</div>
            <div>🔄 Conversations: {st.session_state.conversation_count}</div>
            <div>⏰ Session: {datetime.now().strftime('%H:%M')}</div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Features
    st.markdown("""
    <div class="sidebar-content">
        <h4 style="color: white; margin-bottom: 1rem;">✨ Features</h4>
        <div style="color: rgba(255,255,255,0.8); font-size: 0.9rem; line-height: 1.8;">
            <div>💬 Natural conversations</div>
            <div>🔍 Real-time web search</div>
            <div>🧠 Context-aware responses</div>
            <div>📚 Multi-source research</div>
            <div>🎯 Intelligent tool usage</div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Tips
    st.markdown("""
    <div class="sidebar-content">
        <h4 style="color: white; margin-bottom: 1rem;">💡 Tips</h4>
        <div style="color: rgba(255,255,255,0.7); font-size: 0.85rem; line-height: 1.6;">
            <div>• Ask about current events for web search</div>
            <div>• Have natural conversations</div>
            <div>• Ask follow-up questions</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# === Chat Container ===
chat_container = st.container()

with chat_container:
    # Show chat history with enhanced styling
    for i, msg in enumerate(st.session_state.chat_history):
        if msg["role"] == "user":
            st.markdown(f"""
            <div class="user-message">
                <div class="user-bubble">
                    {msg["content"]}
                    <div style="font-size: 0.7rem; opacity: 0.7; margin-top: 0.5rem; text-align: right;">
                        {datetime.now().strftime('%H:%M')}
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown(f"""
            <div class="assistant-message">
                <div class="assistant-bubble">
                    {msg["content"]}
                    <div style="font-size: 0.7rem; opacity: 0.6; margin-top: 0.5rem; color: #666;">
                        Chatbot • {datetime.now().strftime('%H:%M')}
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)

# === Enhanced Chat Input ===
user_input = st.chat_input("💭 Ask me anything... I can help with questions, coding, research, and more!", key="chat_input")

if user_input:
    # Add user message
    st.session_state.chat_history.append({"role": "user", "content": user_input})
    st.session_state.first_message_sent = True

    # Display user message immediately with timestamp
    st.markdown(f"""
    <div class="user-message">
        <div class="user-bubble">
            {user_input}
            <div style="font-size: 0.7rem; opacity: 0.7; margin-top: 0.5rem; text-align: right;">
                {datetime.now().strftime('%H:%M')}
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    reply = ""
    response_placeholder = st.empty()
    searching_placeholder = st.empty()
    status_placeholder = st.empty()
    search_started = False

    # Show typing indicator
    status_placeholder.markdown("""
    <div class="status-indicator">
        <div class="typing-indicator">
            <div class="typing-dot"></div>
            <div class="typing-dot"></div>
            <div class="typing-dot"></div>
        </div>
        <span>Chatbot is thinking...</span>
    </div>
    """, unsafe_allow_html=True)

    try:
        response = requests.get(
            f"http://localhost:8000/chat_stream/{user_input}",
            params={"checkpoint_id": st.session_state.checkpoint_id},
            stream=True,
            timeout=60
        )

        for line in response.iter_lines():
            if line:
                decoded = line.decode("utf-8").strip()
                if not decoded.startswith("data: "):
                    continue
                raw_json = decoded[6:]

                try:
                    # Now we can directly parse the JSON since it's properly serialized
                    data = json.loads(raw_json)
                except json.JSONDecodeError as e:
                    st.error(f"JSON parsing error: {e}")
                    continue

                if data["type"] == "checkpoint":
                    st.session_state.checkpoint_id = data["checkpoint_id"]

                elif data["type"] == "search_start":
                    search_started = True
                    status_placeholder.empty()
                    searching_placeholder.markdown(f"""
                    <div class="assistant-message">
                        <div class="search-bubble">
                            🔍 Searching the web for: "{data.get('query', 'information')}"
                        </div>
                    </div>
                    """, unsafe_allow_html=True)

                elif data["type"] == "content":
                    status_placeholder.empty()
                    reply += data["content"]
                    # Enhanced message display with better formatting
                    formatted_reply = reply.replace('\n', '<br>').replace('```', '<pre><code>').replace('`', '<code>')
                    response_placeholder.markdown(f"""
                    <div class="assistant-message">
                        <div class="assistant-bubble">
                            {formatted_reply}
                        </div>
                    </div>
                    """, unsafe_allow_html=True)

                elif data["type"] == "search_results":
                    urls = data["urls"]
                    if search_started and urls:
                        links_md = "<br>".join(
                            f"🔗 <a href='{url}' target='_blank'>Source {i+1}</a>" 
                            for i, url in enumerate(urls[:3])
                        )
                        reply = f"<strong>📚 Sources:</strong><br>{links_md}<br><br>" + reply
                    search_started = False
                    searching_placeholder.empty()

    except requests.exceptions.RequestException as e:
        status_placeholder.empty()
        reply = f"⚠️ Connection error: {str(e)}<br><br>Please check if the FastAPI server is running on localhost:8000"
        response_placeholder.markdown(f"""
        <div class="assistant-message">
            <div class="assistant-bubble" style="background: linear-gradient(135deg, #ff9a9e 0%, #fecfef 100%); color: #2d3748;">
                {reply}
            </div>
        </div>
        """, unsafe_allow_html=True)
    except Exception as e:
        status_placeholder.empty()
        reply = f"⚠️ Unexpected error: {str(e)}"
        response_placeholder.markdown(f"""
        <div class="assistant-message">
            <div class="assistant-bubble" style="background: linear-gradient(135deg, #ff9a9e 0%, #fecfef 100%); color: #2d3748;">
                {reply}
            </div>
        </div>
        """, unsafe_allow_html=True)

    # Add to chat history and rerun
    st.session_state.chat_history.append({"role": "assistant", "content": reply})
    time.sleep(0.5)  # Small delay for better UX
    st.rerun()

# === Enhanced Welcome Animation ===
if st.session_state.first_visit and not st.session_state.first_message_sent:
    welcome_messages = [
        {
            "title": "Welcome to Chatbot AI! 👋",
            "subtitle": "Your intelligent conversation partner",
        },
        {
            "title": "Hello there! 🌟", 
            "subtitle": "Ready to assist with anything you need",
        },
        {
            "title": "Hey friend! 🤗",
            "subtitle": "Let's explore the world of AI together", 
        }
    ]
    
    selected_welcome = random.choice(welcome_messages)
    
    placeholder = st.empty()
    
    with placeholder.container():
        st.markdown('<div class="welcome-container">', unsafe_allow_html=True)
        
        # Animated title
        title_placeholder = st.empty()
        subtitle_placeholder = st.empty()
        
        # Animate title
        animated_title = ""
        for char in selected_welcome["title"]:
            animated_title += char
            title_placeholder.markdown(
                f'<div class="welcome-text">{animated_title}</div>', 
                unsafe_allow_html=True
            )
            time.sleep(0.05)
        
        time.sleep(0.5)
        
        # Show subtitle
        subtitle_placeholder.markdown(
            f'<div class="welcome-subtitle">{selected_welcome["subtitle"]}</div>',
            unsafe_allow_html=True
        )
        
        time.sleep(1)
                
        st.markdown('</div>', unsafe_allow_html=True)
        time.sleep(2)

    st.session_state.first_visit = False