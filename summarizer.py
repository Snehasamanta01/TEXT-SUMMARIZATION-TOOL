# Text Summarization Tool
# Author: Sneha Samanta
# Description: Summarizes lengthy articles using NLP techniques

import nltk
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer

# Download required NLTK data
nltk.download('punkt')

def summarize_text(text, sentences_count=3):
    """
    Summarizes input text into a concise version.
    
    :param text: Input article text
    :param sentences_count: Number of summary sentences
    :return: Summary text
    """
    parser = PlaintextParser.from_string(text, Tokenizer("english"))
    summarizer = LsaSummarizer()

    summary = summarizer(parser.document, sentences_count)
    summarized_text = " ".join(str(sentence) for sentence in summary)
    
    return summarized_text


if __name__ == "__main__":
    print("TEXT SUMMARIZATION TOOL")
    print("-" * 30)

    input_text = input("\nEnter the text to summarize:\n\n")

    if len(input_text.strip()) == 0:
        print("❌ No text provided!")
    else:
        summary = summarize_text(input_text)
        print("\n🔹 SUMMARY:\n")
        print(summary)
