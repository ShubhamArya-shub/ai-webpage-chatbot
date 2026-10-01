  🔗 **Live Demo:** [Try the app here](https://ai-webpage-chatbot-ahpmqfqzu3gnjwzm8vkaj9.streamlit.app/)

# 🤖 AI Webpage Chatbot

An AI-powered chatbot that reads any webpage and answers questions about its content — built using **LangChain**, **Google Gemini**, and **Streamlit**.

## 🚀 Features

- Load content from any public webpage URL
- Ask multiple questions about the same page without reloading
- Clean, robotic-themed dark UI
- Powered by Google's Gemini LLM through LangChain

## 🛠️ Tech Stack

- **Python**
- **LangChain** (WebBaseLoader, PromptTemplate, Output Parsers)
- **Google Gemini API** (via `langchain-google-genai`)
- **Streamlit** (UI)

## 📸 How it works

1. Enter a webpage URL
2. Click **Load Page** — the app scrapes and processes the page content
3. Ask any question about the page
4. Get an AI-generated answer based on the actual page content

## ⚙️ Setup & Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/ShubhamArya-shub/ai-webpage-chatbot.git
   cd ai-webpage-chatbot
   ```

2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   venv\Scripts\activate      # Windows
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the root folder and add your Google API key:
   ```
   GOOGLE_API_KEY=your_api_key_here
   ```

5. Run the app:
   ```bash
   streamlit run app.py
   ```

## 📌 Note

Some websites (e.g., heavily JavaScript-based or bot-protected sites like e-commerce platforms) may block scraping. Works best with blogs, articles, Wikipedia pages, and similar content-based sites.

## 👤 Author

**Shubham Kumar**
[GitHub](https://github.com/ShubhamArya-shub) | [LinkedIn](https://linkedin.com/in/shubham-arya-1706b7391)
