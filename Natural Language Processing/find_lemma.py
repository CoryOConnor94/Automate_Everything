import nltk
from nltk.stem import WordNetLemmatizer

# nltk.download('wordnet')

x = 'was'
y = 'is'

lemmatizer = WordNetLemmatizer()

# lemma = lemmatizer.lemmatize(x, 'v')
# lemma_two = lemmatizer.lemmatize(x, 'v')
#
# print(lemma)
# print(lemma_two)

lemma = lemmatizer.lemmatize('vegetable')
lemma_two = lemmatizer.lemmatize('vegetables')

is_same = lemma == lemma_two
print(is_same)



