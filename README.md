# YouTube AI Summarizer

A modern, AI-powered web application that extracts transcripts from YouTube videos and generates intelligent summaries using Google's Gemini AI. Built with Streamlit for a clean, responsive interface.

## 🎬 Features

- **Instant Transcript Extraction**: Automatically fetch transcripts from any YouTube video
- **AI-Powered Summaries**: Generate summaries in three different lengths using Google's Gemini 2.5 Flash Lite model
  - **Short**: 3-5 key bullet points (under 100 words)
  - **Medium**: Structured summary with thematic sections (under 250 words)
  - **Detailed**: Comprehensive analysis with in-depth insights
- **Responsive Design**: Clean, modern UI with custom styling
- **Download Support**: Export summaries as text files
- **Thumbnail Preview**: Visual preview of the YouTube video
- **Error Handling**: Robust error handling for invalid URLs and API failures

## 🚀 Quick Start

### Prerequisites

- Python 3.11+
- Google Gemini API key

### Installation

1. **Clone or download the project**
   ```bash
   cd your-project-directory
   ```

2. **Create and activate a virtual environment** (recommended)
   ```bash
   python -m venv venv
   venv\Scripts\activate  # On Windows
   # or
   source venv/bin/activate  # On macOS/Linux
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   
   Create a `.env` file in the project root:
   ```
   GOOGLE_API_KEY=your_gemini_api_key_here
   ```

### Running the Application

```bash
streamlit run app.py
```

The application will open in your default web browser at `http://localhost:8501`.

## 📖 Usage

1. **Enter YouTube URL**: Paste any valid YouTube video URL in the input field
2. **Choose Summary Length**: Select from Short, Medium, or Detailed summary options
3. **Generate Summary**: Click the "🚀 Generate Summary" button
4. **View Results**: The AI-generated summary appears in the right panel
5. **Download**: Use the download button to save the summary as a text file

## 🛠️ Project Structure

```
├── app.py                 # Main Streamlit application
├── gemini_client.py       # Google Gemini AI integration
├── transcript.py          # YouTube transcript extraction
├── prompts.py            # AI prompt templates and configurations
├── styles.py             # Custom CSS styling
├── history.py            # Session history management
├── export.py             # Export functionality
└── requirements.txt      # Python dependencies
```

## 🔧 Dependencies

- `streamlit` - Web application framework
- `google-genai` - Google Gemini AI client
- `youtube-transcript-api` - YouTube transcript extraction
- `python-dotenv` - Environment variable management
- `pathlib` - Path utilities

## 🔑 API Configuration

This application requires a Google Gemini API key. You can obtain one from the [Google AI Studio](https://makersuite.google.com/app/apikey).

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📄 License

This project is open source. Feel free to use and modify as needed.

## ⚠️ Disclaimer

This tool is for educational and personal use. Please respect YouTube's terms of service and content creators' rights when using extracted transcripts and generated summaries.