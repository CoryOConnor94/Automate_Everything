import nltk
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


text = 'Originally, vegetables were collected from the wild by hunter-gatherers. Vegetables can be eaten either raw or cooked'
question = 'What are vegetables?'


def lemma_sentence(sentence):
    lemmatizer = WordNetLemmatizer()
    sentence_tokens = nltk.word_tokenize(sentence.lower())
    pos_tags = nltk.pos_tag(sentence_tokens)

    sentence_lemmas = []
    for token, pos_tag in zip(sentence_tokens, pos_tags):
        if pos_tag[1][0].lower() in ['n', 'v', 'a', 'r']:
            lemma = lemmatizer.lemmatize(token, pos_tag[1][0].lower())
            sentence_lemmas.append(lemma)

    return sentence_lemmas

sentence_tokens = nltk.word_tokenize(text)
sentence_tokens.append(question)

tv = TfidfVectorizer(tokenizer=lemma_sentence)
tf = tv.fit_transform(sentence_tokens)
print(sentence_tokens)

values = cosine_similarity(tf[-1], tf)
print(values)

index = values.argsort()[0][-2]
print(index)

values_flat = values.flatten()
print(values_flat)

values_flat.sort()
print(values_flat)

coeff = values_flat[-2]
print(coeff)

if coeff > 0.3:
    print(sentence_tokens[index])