import pandas as pd
import numpy as np 
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import TruncatedSVD
from sklearn.preprocessing import Normalizer
N = 100
df = pd.read_csv('data/Reviews.csv')
listText = df['Text']
newdf = df.iloc[:N]
newListText = newdf['Text']

"""
This function task a list of text a fit a model that will be used to creat a term-document matrix.
"""
def createtfIdfModel(listOfText):
    tfIdfVectorizer = TfidfVectorizer()
    bowVectorizer = CountVectorizer(stop_words='english')
    tfIdfVectorizer.fit(listOfText)
    bowVectorizer.fit(listOfText)
    with open("model/tfIdfVectorizer", "+wb") as f:
        pickle.dump(tfIdfVectorizer, f, pickle.HIGHEST_PROTOCOL)
    f.close()
    with open("model/bowVectorizer", "+wb") as f:
        pickle.dump(bowVectorizer, f, pickle.HIGHEST_PROTOCOL)
    f.close()

"""
This function takes a list of text, a text id in the list of text and a given word
It returns the importance of the word in the given text 
"""
def wordImportance(listText,textId, word):
    with open("model/tfIdfVectorizer", "rb") as f:
        tfIdfVectorizer = pickle.load(f)
    f.close()
    X = tfIdfVectorizer.transform(listText)
    print(X[1, tfIdfVectorizer.vocabulary_[word]])

def singularDecomposition(listText):
    with open("model/bowVectorizer", "rb") as f:
        bowVectorizer = pickle.load(f)
    f.close()
    X = bowVectorizer.fit_transform(newListText)
    
    # algorithm: arpack for smaller datasets 
    lsa = TruncatedSVD(n_components=2, algorithm="randomized")
    dtm_lsa = lsa.fit_transform(X)
    dtm_lsa = Normalizer().fit_transform(dtm_lsa)
    
    pd.DataFrame(dtm_lsa, index=newListText, columns= ['component1', 'component2'] ).to_csv('output/lsa.csv', encoding='utf-8')

    
    # memory issue 
    similarity = np.asarray(np.asmatrix(dtm_lsa) * np.asmatrix(dtm_lsa).T)
    pd.DataFrame(similarity,index=newListText, columns=newListText).to_csv('output/similarity.csv', encoding='utf-8')

    print('end lsa')
    
if __name__=='__main__':
    
    #Training our model: This should be done ones 
    #createtfIdfModel(listText)
    
    # example : wordImportance(listText,1, 'error')
    # wordImportance(listText,1, 'error')

    # Singular Value  Decomposition
    singularDecomposition(listText)
    
