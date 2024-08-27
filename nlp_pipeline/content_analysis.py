import os
import re
import pandas as pd
from textblob import TextBlob
from dotenv import load_dotenv
from typing import List, Tuple
from spacy_llm.util import assemble
load_dotenv(override=True)

os.environ["AZURE_OPENAI_API_KEY"] = os.getenv('AZURE_OPENAI_API_KEY')
os.environ["AZURE_OPENAI_KEY"] = os.getenv("AZURE_OPENAI_API_KEY")
vi_api_key = os.getenv("VT_API_KEY")
nlp_pipeline_dir_path = "/".join(os.path.abspath(__file__).split('\\')[:-2])+'/nlp_pipeline'
black_listed_url_file_path =  "/".join(os.path.abspath(__file__).split('\\')[:-2])+'/assets/blacklisted_url.txt'


def url_analyzer_blist(url_list: List[str]) -> List[dict]:
    """
    For blacklisted url tagging by using blacklisted url dump
    """
    url_stats: List[dict] = list()
    df= pd.read_csv(black_listed_url_file_path, sep = ",", skiprows=8)
    filtered_df = df.loc[df.url.apply(lambda x: x in url_list)]
    url_stats = filtered_df.apply(lambda row: {'url': row['url'], 'threat': row['threat']}, axis=1).tolist()
    if not url_stats:
        return [{"url_status":"No url is blacklisted"}]
    else:
        return url_stats


def ner_extractor(msg: str) -> list:
    """
    For NER extraction through spacy-llm
    """
    nlp = assemble(os.path.join(nlp_pipeline_dir_path,"ner.cfg"))
    doc = nlp(msg)
    return [(ent.text, ent.label_) for ent in doc.ents]


def spam_classifier(msg: str) -> list:
    """
    For spam classification through spacy-llm
    """
    nlp = assemble(os.path.join(nlp_pipeline_dir_path,"spam_classification.cfg"))
    doc = nlp(msg)
    return [key for key,value in doc.cats.items() if value == 1]


def sen_analyzer(msg: str) -> List[dict] :
    """
    For sentiment analysis through spacy-llm
    """
    data = TextBlob(msg)
    sen_result_list =list(data.sentiment)
    return [{"polarity" :sen_result_list[0]},  {"subjectivity":sen_result_list[1]}]


def content_analyzer(msg:str) -> Tuple[list, list, List[dict], List[dict]]:
    """
    For content analysis which includes:
    1. Spam Classification
    2. Ner Extraction
    3. Sentiment Analysis
    4. Balcklisted URL Tagging

    NOTE: Only analyse reports/complaints/content of message when it starts with syntax:
    SATVA:[------ Content ---]
    """
    spam_stats = spam_classifier(msg)
    ner_stats = ner_extractor(msg)
    sen_stats = sen_analyzer(msg)

    url_pattern = r'https?://\S+'
    url_list = re.findall(url_pattern, msg)

    url_stats = url_analyzer_blist(url_list)
    return spam_stats, sen_stats, ner_stats, url_stats
