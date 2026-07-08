# 📈 AI Swing Trade Bot

An intelligent swing trading assistant that analyzes MT5 chart screenshots using Google Gemini AI to provide trading signals with Entry, Stop Loss, and Take Profit levels.

## Features

- 🤖 **AI-Powered Analysis**: Uses Google Gemini AI to analyze trading charts
- 📊 **Swing Trade Signals**: Identifies trends, support/resistance, and trade opportunities
- 📱 **User-Friendly Interface**: Built with Streamlit for easy chart uploads
- ⚡ **Fast Processing**: Real-time chart analysis

## Requirements

- Python 3.9 or higher
- Google Generative AI API key ([Get one here](https://ai.google.dev))
- MT5 terminal (for generating chart screenshots)

## Installation

### Option 1: Using pip (Recommended)

```bash
# Clone the repository
git clone https://github.com/kabelomoloi031-max/Moloi-swing-bot-v12.git
cd Moloi-swing-bot-v12

# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install the package
pip install -e .
```

### Option 2: Using requirements.txt

```bash
# Clone the repository
git clone https://github.com/kabelomoloi031-max/Moloi-swing-bot-v12.git
cd Moloi-swing-bot-v12

# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

## Configuration

1. **Copy the environment template**:
   ```bash
   cp .env.example .env
   ```

2. **Add your Google API Key** to `.env`:
   ```
   GOOGLE_API_KEY=your_actual_api_key_here
   ```

   Get your API key:
   - Visit [Google AI Studio](https://aistudio.google.com/apikey)
   - Create a new API key
   - Copy and paste it into your `.env` file

## Usage

Run the application with Streamlit:

```bash
streamlit run app.py
```

The app will open in your browser at `http://localhost:8501`

1. Upload a screenshot of your MT5 chart
2. Click "Analyze for Swing Trade"
3. Review the AI-generated analysis with Entry, Stop Loss, and Take Profit levels
4. Test signals on a Demo Account first before trading live

## Project Structure

```
Moloi-swing-bot-v12/
├── app.py                 # Main Streamlit application
├── requirements.txt       # Python dependencies
├── setup.py              # Package setup configuration
├── .env.example          # Environment variables template
├── .gitignore            # Git ignore rules
└── README.md             # This file
```

## Environment Variables

- `GOOGLE_API_KEY`: Your Google Generative AI API key (required)

## Security Notes

⚠️ **Important**:
- Never commit your `.env` file with actual API keys
- Keep your API key confidential
- The `.env` file is already in `.gitignore` to prevent accidental commits
- Always use environment variables for sensitive data

## Troubleshooting

### "Google API Key not found"
- Ensure `.env` file exists in the project root
- Check that `GOOGLE_API_KEY` is properly set
- Restart the Streamlit app

### "Module not found" errors
- Ensure virtual environment is activated
- Run `pip install -r requirements.txt` or `pip install -e .`

### API errors
- Verify your Google API key is valid
- Check your API quota hasn't been exceeded
- Ensure the chart image is in a supported format (JPG, PNG)

## Disclaimer

⚠️ **Trading Disclaimer**: This tool is for educational and analytical purposes. Always:
- Test signals on a Demo Account first
- Never rely solely on AI analysis for trading decisions
- Maintain proper risk management
- Consult with financial advisors if needed
- Only trade what you can afford to lose

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contributing

Contributions are welcome! Feel free to submit issues and pull requests.

## Support

For issues, questions, or suggestions, please open an issue on the [GitHub repository](https://github.com/kabelomoloi031-max/Moloi-swing-bot-v12/issues).

---

**Happy Trading! 📈**
