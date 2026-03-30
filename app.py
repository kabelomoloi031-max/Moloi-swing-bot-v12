import streamlit as st
import google.generativeai as genai
from PIL import Image

# 1. SETUP
st.set_page_config(page_title="AI Swing Bot", layout="centered")
st.title("📈 AI Swing Trade Bot")

# --- IMPORTANT: Paste your Google API Key inside the quotes below ---
API_KEY = AIzaSyAxFAFZ-PlIBu-Qg-AXKfdLZJFeLaLjAk4
# ------------------------------------------------------------------

genai.configure(api_key=API_KEY)

# 2. INTERFACE
st.write("Upload a screenshot of your MT5 chart for a swing trade signal.")
uploaded_file = st.file_uploader("Choose a chart screenshot...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
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
                
                st.success("Analysis Complete!")
                st.markdown("### 🤖 AI Trade Signal:")
                st.write(response.text)
            except Exception as e:
                st.error(f"Error: {e}")

st.divider()
st.info("Remember: Always test signals on a Demo Account first.")
