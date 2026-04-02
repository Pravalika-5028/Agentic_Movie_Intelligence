# 🎬 Multi-Agent Movie Intelligence System

A Streamlit-based web application that fetches real-time movie data, analyzes it using a local LLM agent (via Ollama), and generates a downloadable PDF report.

---

## Features

- 🔍 **Movie Data Fetching** — Retrieves detailed movie information from the OMDb API (plot, cast, director, ratings, genre, and more)
- 🤖 **AI-Powered Analysis** — Uses a `phi` Agent backed by `llama3.1` (via Ollama) to answer user questions and generate professional movie summaries
- 📄 **PDF Report Generation** — Exports the AI-generated analysis as a downloadable PDF using `fpdf`
- 🖥️ **Interactive UI** — Clean Streamlit interface with expandable raw data, spinners, and download buttons

---

## Project Structure

```
├── agents.py        # Core logic: OMDb fetcher, PDF generator, and phi Agent setup
├── app.py           # Streamlit UI and application flow
├── .env             # Environment variables (optional)
└── requirements.txt # Python dependencies
```

---

## Prerequisites

- Python 3.9+
- [Ollama](https://ollama.com/) installed and running locally
- `llama3.1` model pulled in Ollama:
  ```bash
  ollama pull llama3.1
  ```

---

## Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/movie-intelligence-system.git
   cd movie-intelligence-system
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment** *(optional)*

   Create a `.env` file if you plan to manage additional secrets:
   ```
   OMDB_API_KEY=your_api_key_here
   ```
   > The OMDb API key is currently hardcoded in `agents.py`. Replace it with your own key from [omdbapi.com](https://www.omdbapi.com/apikey.aspx) for production use.

4. **Start Ollama** (if not already running)
   ```bash
   ollama serve
   ```

---

## Usage

```bash
streamlit run app.py
```

Then open your browser to `http://localhost:8501` and:

1. Enter a movie title (e.g., *Inception*, *The Dark Knight*)
2. Type a question about the movie (optional)
3. Click **Analyze Movie**
4. View the AI-generated summary and download the PDF report

---

## Dependencies

| Package | Purpose |
|---|---|
| `streamlit` | Web UI framework |
| `phidata` | Agent orchestration framework |
| `ollama` | Local LLM runtime |
| `fpdf` | PDF generation |
| `requests` | HTTP calls to OMDb API |
| `python-dotenv` | Environment variable management |

Install all at once:
```bash
pip install streamlit phidata ollama fpdf requests python-dotenv
```

---

## API Reference

**OMDb API** — `http://www.omdbapi.com/`

The app fetches full plot data using the `t` (title) and `plot=full` parameters. A free API key is required; register at [omdbapi.com](https://www.omdbapi.com/apikey.aspx).

---

## How It Works

```
User Input (Title + Question)
        │
        ▼
  OMDb API Fetch
        │
        ▼
  phi Agent (llama3.1 via Ollama)
        │
        ▼
  AI Analysis & Summary
        │
        ▼
  PDF Generation (fpdf)
        │
        ▼
  Streamlit Download Button
```

---

## Notes

- The LLM agent is instructed to use **only the provided movie data** and answer questions strictly related to the movie.
- Ollama must be running locally before launching the app — the agent will fail to respond otherwise.
- The generated PDF is saved as `movie_report.pdf` in the working directory before being served for download.

---

## License

MIT License. Feel free to use, modify, and distribute.
