import streamlit as st
import google.generativeai as genai
import os
from pathlib import Path
from dotenv import load_dotenv
from PIL import Image

# Load environment variables from .env file
load_dotenv()

# 1. SETUP
st.set_page_config(page_title="AI Swing Bot", layout="centered")
st.title("📈 AI Swing Trade Bot")

# Load API key from environment variable
API_KEY = os.getenv("GOOGLE_API_KEY")
if not API_KEY:
    st.error("❌ Google API Key not configured.")
    st.info("Please create a `.env` file with your GOOGLE_API_KEY or set the environment variable.")
    st.stop()

genai.configure(api_key=API_KEY)

# 2. INTERFACE
st.write("Upload a screenshot of your MT5 chart for a swing trade signal.")
uploaded_file = st.file_uploader("Choose a chart screenshot...", type=["jpg", "jpeg", "png"])

MAX_FILE_SIZE = 5 * 1024 * 1024  # 5MB

if uploaded_file is not None:
    # Validate file size
    if uploaded_file.size > MAX_FILE_SIZE:
        st.error(f"❌ File too large. Maximum size is 5MB. Your file is {uploaded_file.size / 1024 / 1024:.2f}MB")
    else:
        image = Image.open(uploaded_file)
        st.image(image, caption='Uploaded Chart', use_column_width=True)
        
        if st.button('Analyze for Swing Trade'):
            with st.spinner('AI is analyzing the price action...'):
                try:
                    model = genai.GenerativeModel('gemini-1.5-flash')
                    prompt = """
                    Analyze this MT5 trading chart. 
                    1. Identify the Trend (Bullish/Bearish).
                    2. Identify Support and Resistance levels.
                    3. Action: BUY, SELL, or WAIT?
                    4. If Buy/Sell, give Entry, Stop Loss (SL), and Take Profit (TP).
                    Keep the response short and professional for a swing trader.
                    """
                    response = model.generate_content([prompt, image])
                    
                    st.success("✅ Analysis Complete!")
                    st.markdown("### 🤖 AI Trade Signal:")
                    st.write(response.text)
                except genai.GoogleGenerativeAIException as e:
                    st.error(f"❌ AI Error: {str(e)}")
                except Exception as e:
                    st.error(f"❌ Unexpected error: {str(e)}")

st.divider()
st.info("⚠️ Remember: Always test signals on a Demo Account first.")

def main():
    """Main entry point for the application."""
    pass

if __name__ == "__main__":
    main()
