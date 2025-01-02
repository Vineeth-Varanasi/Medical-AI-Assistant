# Medical-AI-Assistant
## Flask App with Environment Variables Integration

This project is a Flask-based application that utilizes environment variables for secure API key management. It demonstrates the integration of Pinecone, Groq, and other AI components to handle question-answering tasks.

---

## Features
- Flask backend for routing and request handling.
- Utilization of the `.env` file to manage sensitive API keys (e.g., `PINECONE_API_KEY`, `GROQ_API_KEY`).
- Integration with Pinecone for document retrieval and Groq for language model interactions.
- Question-answering functionality with context-based retrieval.
- HTML template for chat interface.

---

## Requirements

- Python 3.8+
- Flask
- python-dotenv
- Pinecone
- Groq API integration
- Other dependencies listed in `requirements.txt`

---

## Setup

### 1. Install Dependencies

Install the required Python libraries:

```bash
pip install -r requirements.txt
```

### 2. Create a `.env` File

In the root directory, create a `.env` file and add the following environment variables:

```
PINECONE_API_KEY=your_pinecone_api_key_here
GROQ_API_KEY=your_groq_api_key_here
```

Replace `your_pinecone_api_key_here` and `your_groq_api_key_here` with your actual API keys.

### 3. Run the Application

Start the Flask application with:

```bash
python app.py
```

## File Structure

```
project/
|
|-- app.py                # Main Flask application
|-- .env                  # Environment variables file
|-- templates/
|   |-- chat.html         # HTML template for chat UI
|-- src/
|   |-- helper.py         # Helper functions (e.g., embeddings)
|   |-- prompt.py         # Prompt configuration
|-- requirements.txt      # Dependencies
```

---

## Usage

1. Open a web browser and navigate to `http://localhost:8080`.
2. Type your query in the chat interface.
3. The system will retrieve relevant context and provide concise answers.

---

## Security Best Practices
- **Do not commit the `.env` file to version control.** Add `.env` to `.gitignore`:

```
.env
```

- **Validate environment variables** in `app.py` before using them:

```python
if not PINECONE_API_KEY or not GROQ_API_KEY:
    raise ValueError("API keys must be set in the .env file.")
```

---

## License
This project is licensed under the MIT License.

---

## Contributions
Contributions are welcome! Feel free to open issues or submit pull requests.

