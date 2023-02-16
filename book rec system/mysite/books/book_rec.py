# Book Recommendation System
# Leverages content-based filtering machine learning methods to recommend books

# Necessary libraries
import numpy as np
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer

def search_book(title):
  # Store the data
  df = pd.read_csv('books.csv', encoding='unicode_escape', on_bad_lines='skip')

  columns = ['title', 'authors']

  def combine_features(data):
    features = []
    for i in range(0, data.shape[0]):
      features.append(str(data['title'][i])+ " "+str(data['authors'][i]))
    return features

  df['combined_features'] = combine_features(df)

  cm = CountVectorizer().fit_transform(df['combined_features'])

  cs = cosine_similarity(cm)

  book_id = df[df.title == title]['bookID'].values

  scores = list(enumerate((cs[book_id])[0]))


  #Sort the list of similar books in descending order
  sorted_scores = sorted(scores, key= lambda x:x[1], reverse= True)
  sorted_scores = sorted_scores[1:]
  #Show the sorted scores
  j = 0
  seen = [title]
  books = []
  for item in sorted_scores:
      book_title = df.loc[item[0], 'title']
      if book_title in seen:
          continue
      seen.append(book_title)
      books.append(book_title)
      j += 1
      if j >= 5:
          break
  return books

  

