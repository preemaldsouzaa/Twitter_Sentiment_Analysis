# Twitter Sentiment Analysis
Twitter Sentiment Analysis is the process of using NLP and ML techniques to determine the sentiment or emotional tone expressed in tweets on the social media platform Twitter. This project aims to understand whether tweets are generally positive, negative, or neutral in their sentiment. 

## **Introduction**
The world of natural language processing (NLP) has witnessed a transformative revolution thanks to the advent of machine learning models. These models have proven to be invaluable in their ability to automatically decipher complex language patterns, scale effectively to process vast volumes of text data, and adapt seamlessly to a myriad of NLP applications. With their prowess in feature extraction, harnessed through techniques like Bag of Words (BoW) and Term Frequency-Inverse Document Frequency (TF-IDF), combined with the power of transfer learning, machine learning models have become indispensable tools in the arsenal of text analysis. These models are the driving force behind numerous applications, from sentiment analysis and text classification to machine translation and more, enabling the extraction of invaluable insights from text data across diverse domains and industries. In this comprehensive exploration, we delve into the development, assessment, and optimization of various machine learning models, employing both BoW and TF-IDF approaches, to unravel the intricate nuances of text-based data and pave the way for automation and meaningful interpretation in the realm of natural language processing.

## **Objectives**
Our project has three primary objectives:
1. To develop a sentiment analysis tool capable of discerning the sentiment (positive, negative, or neutral) conveyed within tweets.
2. To enhance the accuracy and efficiency of the sentiment analysis model through the utilization of advanced machine learning techniques.
3. To provide an accessible user interface (UI) that allows users to interact with the sentiment analysis tool, offering valuable insights from Twitter data.

## **Tools Used**
1. **Data Analysis & Modeling**: **Python** Pandas, Numpy, Sci-kit Learn, NLTK (Natutal Language Toolkit), Matplotlib, Seaborn, CATBoost, XGBoost, LightGBM, Keras, re(Regular Expressions), Pickle
2. **Model Deployment**: Flask
3. **User Interface**: HTML

![download](https://github.com/preemaldsouzaa/Twitter_Sentiment_Analysis/assets/117831091/c94e2b7f-25c0-485d-a220-b816e7689fe2)

## **Data Preprocessing**
![1_CbzCcP3XFtYVJmWowZLugQ](https://github.com/preemaldsouzaa/Twitter_Sentiment_Analysis/assets/117831091/eb182905-5739-4259-9593-6e9b34ec7421)

1. Data Collection: Twitter data, including tweet text, user information, timestamps, and metadata, is collected using the Twitter API or pre-collected datasets.

2. Cleaning and Noise Reduction: Hyperlinks, mentions, special characters, and emojis are removed to enhance data quality.

3. Lowercasing: Text is converted to lowercase to standardize it and simplify analysis.

4. Tokenization: Text is split into individual words or tokens for further processing.

5. Stopword Removal: Common, non-informative words (stopwords) like "and" and "the" are removed.

6. Lemmatization or Stemming: Words are reduced to their base or root form to improve text analysis.

7. Data Transformation: Text data is converted into numerical representations suitable for machine learning. Two widely used techniques, Bag of Words (BoW) and Term Frequency-Inverse Document Frequency (TF-IDF), were employed for feature extraction. BoW represents text as a collection of word frequencies, while TF-IDF assigns weights to words based on their importance in a document and across a corpus.

## **Exploratory Data Analysis (EDA)**

EDA is a crucial phase for gaining insights into the dataset before model development. Here are some key EDA steps:

1. Visualizing the distribution of sentiment labels.
2. Understanding sentiment class distribution.
3. Analyzing the most common words for each sentiment category.
4. Examining the distribution of tweet lengths.
5. Visualizing the distribution of sentiment polarity scores.
   
By performing EDA, we gain a deeper understanding of the data, uncover trends, and identify potential challenges that may affect model development and deployment.

## **Model Development and Evaluation**

We implemented and evaluated a range of machine learning models using both BoW and TF-IDF representations. The models considered included:
1. Naive Bayes
2. Logistic Regression
3. Random Forest
4. Support Vector Classifier (SVC)
5. Gradient Boosting Classifier
6. Decision Tree Classifier

For each model, we utilized techniques such as random under-sampling to address class imbalance and evaluated their performance using various metrics, including accuracy, precision, recall, F1-score, and mean absolute error (MAE).

**Hyperparameter Tuning:**
To optimize model performance further, we conducted hyperparameter tuning using GridSearchCV for the following models:
***Naive Bayes, Logistic Regression, Random Forest, SVC and Decision Tree***
Hyperparameter tuning helped fine-tune model parameters for optimal performance, and the selected best-performing models were included in the evaluation.

**Ensembled Models:**
Although Logistic Regression was the primary choice, we explored ensemble models, including Ada Boost, XGBoost, Cat Boost, and LightGBM, to ensure a well-rounded evaluation. 
These models achieved competitive results, but Logistic Regression's interpretability and simplicity ultimately led to its selection.

## **Model Selection**
After an exhaustive evaluation process, Logistic Regression emerged as the preferred model for sentiment analysis due to its exceptional performance. With an accuracy of 70.4% and several practical advantages, including interpretability, simplicity, and resource efficiency, Logistic Regression aligned well with project objectives.

## **Model Deployment on Flask**
The final Logistic Regression model was saved to a file for further deployment, ensuring that our sentiment analysis solution can be seamlessly integrated into a user interface or application.

To make our sentiment analysis tool accessible to users, we deploy our chosen model using Flask, a Python web framework. This step involves creating a user-friendly interface where users can input Twitter text, and our model will provide sentiment predictions. 

Testing our Model:
![twitter_sentiment3](https://github.com/preemaldsouzaa/Twitter_Sentiment_Analysis/assets/117831091/5b709310-0fdf-450d-9536-412ffedec297)
![twitter_sentiment1](https://github.com/preemaldsouzaa/Twitter_Sentiment_Analysis/assets/117831091/c3f27ac8-8857-4d5f-b737-aba993f090a0)
![Screenshot 2023-08-22 161502](https://github.com/preemaldsouzaa/Twitter_Sentiment_Analysis/assets/117831091/a3c89d03-65cd-4b2a-9fbd-67cb51b25169)

With this README, we aim to provide a comprehensive overview of our project, from its objectives and tools to its key phases of data preprocessing, EDA, model development, and deployment, offering a clear and informative guide to our sentiment analysis project on Twitter data.
