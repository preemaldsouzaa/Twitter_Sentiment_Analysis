import nltk
nltk.download("stopwords")
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import TweetTokenizer
from nltk.corpus import stopwords  
import re
from sklearn.feature_extraction.text import TfidfVectorizer

def preprocess_text(text):
    text =text.lower() # Converting to lower case
    text = re.sub(r"http\S+", "", text)  # Excluding hyperlinks
    text = re.sub(r"www\.\S+", " ", text)  # Excluding links starting with 'www'
    text = re.sub(r"@\w+", " ", text)  # Excluding tagged data
    text = re.sub(r"[^A-Za-z\s]", " ", text)  # Excluding non-alphabetical characters except whitespace
    return text.strip()


def preprocess(text):
    stop_words=set(stopwords.words('english'))
    tokenizer=TweetTokenizer()
    lemmatizer = WordNetLemmatizer()
    tokens = tokenizer.tokenize(text)
    tokens = [lemmatizer.lemmatize(word.lower()) for word in tokens if word not in stop_words]
    return " ".join(tokens)