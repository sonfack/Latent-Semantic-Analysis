from src.menu import main_menu
import pandas as pd
import numpy as np 
import pickle
import os
import sys
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import TruncatedSVD
from sklearn.preprocessing import Normalizer
N = 100

newdf = df.iloc[:N]
newListText = newdf['Text']


    
if __name__=='__main__':
    main_menu()
    
