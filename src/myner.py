import spacy
nlp = spacy.load("en")
mytext = "But Google of Larry Page is starting from behind. The company made a late push\ninto hardware, and Apple’s Siri"

def myNer(text):
    doc = nlp(text)
    for entity in doc.ents:
        print(entity.text, ' - ', entity.label_)

myNer(mytext)
