import nltk
from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()

# nltk.download('punkt_tab')

sentence = 'vegetables are types of plants'
sentence_tokens = nltk.word_tokenize(sentence)

# nltk.download('averaged_perceptron_tagger_eng')
pos_tags = nltk.pos_tag(sentence_tokens)
# print(pos_tags)

sentence_lemmas = []
for token, pos_tag in zip(sentence_tokens, pos_tags):
    if pos_tag[1][0].lower() in ['n', 'v', 'a', 'r']:
        lemma = lemmatizer.lemmatize(token, pos_tag[1][0].lower())
        sentence_lemmas.append(lemma)

print(sentence_lemmas)