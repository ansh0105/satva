# SATVA: Spam Analysis and Tagging with Virtual Assistant

## Overview

SATVA is an advanced spam detection and analysis tool that integrates multiple layers of text analysis, including Spam Classification, Named Entity Recognition (NER) Extraction, Sentiment Analysis, and Blacklisted URL Tagging. It also leverages Generative AI to produce detailed responses based on the analysis. The project offers two main utilities:

1. **Telegram Bot Integration:** Users can interact with a registered Telegram bot to analyze messages and receive detailed spam analysis.
2. **Streamlit Web Application:** Users can input text for analysis via a web interface with built-in authentication features.

## Features

- **Spam Classification:** Detects and categorizes different types of spam (e.g., phishing, promotional).
- **NER Extraction:** Identifies key entities and personal information within the text.
- **Sentiment Analysis:** Analyzes the sentiment (subjectivity and polarity) of the message.
- **Blacklisted URL Tagging:** Checks URLs against a blacklist to flag malicious links.
- **Generative AI Response:** Provides a human-readable explanation and detailed analysis of the message.

## Getting Started

### Prerequisites

- Python 3.9 (or above)
- Virtual Environment (optional but recommended)
- Telegram API credentials
- Azure OpenAI credentials

### Installation

1. **Clone the Repository:**
    ```bash
    git clone <repository_url>
    ```
2. **Create a Python Virtual Environment:**
    ```bash
    python -m venv env
    source env/bin/activate  # On Windows use `env\Scripts\activate`
    ```
3. **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

### Configuration

1. **Update the `.env` File:**
   - Navigate to the `satva` directory.
   - Update the `.env` file with your Telegram `API_ID` and `API_HASH`. Obtain these credentials from [here](https://core.telegram.org/api/obtaining_api_id).

   Example `.env` file:
    ```env
    API_ID=<your_telegram_api_id>
    API_HASH=<your_telegram_api_hash>
    ```

2. **Update NER and Spam Classification Config Files:**
   - In the `nlp_pipeline` folder, update the `.env`, `ner.cfg` and `spam_classification.cfg` files with your Azure OpenAI credentials. Obtain these credentials from [here](https://learn.microsoft.com/en-us/azure/ai-services/openai/how-to/create-resource?pivots=web-portal).

   Example configuration for `.env`:
    ```env
    AZURE_OPENAI_API_KEY=<your_azure_openai_api_key>
    OPENAI_API_TYPE=<your_azure_openai_type e.g azure>
    OPENAI_API_VERSION=<your_azure_openai_version>
    AZURE_OPENAI_ENDPOINT=<your_azure_openai_endpoint>
    
    ```

   Example configuration for `.cfg`:
    ```env
    deployment_name=<your_azure_openai_model_name e.g gpt-35-turbo, gpt-4, gpt-4-turbo>
    name=<your_azure_openai_model_name e.g gpt-35-turbo, gpt-4, gpt-4-turbo>
    model_type=<your_azure_openai_model_type e.g chat,instruct>
    api_version=<your_azure_openai_version>
    base_url=<your_azure_openai_endpoint>
    
    ```

### Running the Telegram Bot Integration

1. **Create a Telegram Session File:**
    ```bash
    cd telegram
    python create_telegram_sessionfile.py
    ```
    - Follow the steps to create a session file using your Telegram credentials.

2. **Start the Telegram Session:**
    ```bash
    python message_handler.py
    ```
    - Now, you can send messages to the registered Telegram channel, and SATVA will analyze them.

    **Note:** To receive a response, start your message with:
    ```
    SATVA: <your_message_content>
    ```
 **Here is few screenshots of SATVA Telegram Bot in action:**

<img src="https://github.com/user-attachments/assets/c6af23cd-dd06-4752-9253-6f502d5aae4d" alt="Image 1" width="1000" height="150"/>
<p align="justify">
  <img src="https://github.com/user-attachments/assets/927e1550-1be6-44c6-9a36-ef7ff4cff590" alt="Image 2" width="500" height="340" />
  <img src="https://github.com/user-attachments/assets/35462cb1-21e2-451f-9880-0f5e7da7f099" alt="Image 3" width="500" height="340"/>
</p>




### Running the Streamlit Web Application

1. **Navigate to the Streamlit Package Directory:**
    ```bash
    cd streamlit_package
    ```

2. **Start the Application:**
    ```bash
    python start_app.py
    ```
    - Open the application in your web browser.

    **Default Login Credentials:**
    - **Username:** admin
    - **Password:** admin
    - **Email:** admin@gmail.com

    After logging in, you can update your username and password using the "Update User Details" feature.

 **Here is a demonstration video of SATVA Web Application in action:**
 
[SATVA Web Application](https://github.com/user-attachments/assets/5a9f7791-9358-4e86-bcb6-82541308fac4)


## Notes

- **Security:** Ensure that your API credentials are kept secure and not exposed in public repositories.
- **Scalability:** The architecture can be expanded with additional layers or integrated with other messaging platforms.

