from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB

emails = ["free prize", "urgent verify bank", "hello friend"]
labels = [1, 1, 0]

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(emails)

model = MultinomialNB()
model.fit(X, labels)

def ml_predict(text):
    X_test = vectorizer.transform([text])
    return int(model.predict_proba(X_test)[0][1] * 100)