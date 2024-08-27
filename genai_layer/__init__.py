import os
from typing import List
from dotenv import load_dotenv
from openai import AzureOpenAI
load_dotenv(override=True)

role_init = """You are an expert in spam filtering and advanced NLP and give interactive styling response that can be use in markdown"""
prompt_init = """Analyze the following message and provide a detailed response. The response should include a greeting to the 
        sender, a consolidation of all analysis points, and a summary message for the end user with action points.
        NOTE: Response should not include any closing and signature such as Best regards or Best name etc at the end of the response.

        Message Information:
        Sender Name: {}
        Message: {}
        Spam Category: {}
        Sentiment Analysis: {}
        Named Entity Recognition (NER): {}
        URL Analysis: {}

        NOTE for message information: Polarity - Ranges from -1 to 1, indicating positive or negative sentiment.
        Subjectivity - Indicates whether the message is full of personal opinions, emotions, or judgments.
        URL has been scanned by different engines and is considered harmless by the majority

        Guidelines for Response:
        Greet the sender.
        Summarize in summary about -the spam analysis points which is:
        Identify the spam category.
        Mention the sentiment analysis results.
        Highlight the NER results.
        Provide details from the URL analysis.

        While also conclude with a short summary message about the spam status and recommended actions for the end user.
        Ends the response with quote 'Stay Vigilant Stay Safe!'.
        """

def generate_response(sender_name:str, msg:str, spam_stat:list, sen_stat:list, ner_stat:List[dict], url_stat:List[dict]) -> str:
    """
    Perform advance analysis and generate response through llm  
    """
    client = AzureOpenAI(
                        azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT"), 
                        api_key= os.getenv("AZURE_OPENAI_API_KEY"),  
                        api_version= os.getenv("OPENAI_API_VERSION"),
                        )

    response = client.chat.completions.create(
    model = "gpt-4-turbo",
    messages = [
                {"role": "system", "content": role_init},
                {"role": "user", "content": prompt_init.format(sender_name, msg, spam_stat, sen_stat, ner_stat, url_stat)}
            ]
            )
    return response.choices[0].message.content

__all__ = ['generate_response']



