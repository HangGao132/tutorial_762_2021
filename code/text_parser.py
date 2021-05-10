"""
Using the Python core modules to parse text.

WARNING: For study purpose only. If the same code has been used in any part of 
the assignment, it will be considered as plagiarism.
"""
from collections import Counter
import string
import re

# Text from the machine learning page in Wikipedia
text = """machine Machine learning (ML) is the study of computer algorithms that improve 
automatically through experience and by the use of data. It is seen as a part of
 artificial intelligence. Machine learning algorithms build a model based on 
 sample data, known as "training data", in order to make predictions or 
 decisions without being explicitly programmed to do so. Machine learning 
 algorithms are used in a wide variety of applications, such as in medicine, 
 email filtering, and computer vision, where it is difficult or unfeasible to 
 develop conventional algorithms to perform the needed tasks."""

# List of stop words; Including empty and space just in case we count them as tokens
stop_words = ['', ' ', 'i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', 
'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', 
'her', 'hers', 'herself', 'it', 'its', 'itself', 'they', 'them', 'their', 'theirs', 
'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', 'these', 'those', 
'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 
'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 
'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 
'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 
'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 
'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 
'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 
'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 
's', 't', 'can', 'will', 'just', 'don', 'should', 'now']

def main():
    # Replace all punctuations with space
    regex = re.compile('[%s]'%re.escape(string.punctuation))
    out = regex.sub(' ', text)
    # Replace multiple space and end of line (EOL)
    out = re.sub('\s+|\n', ' ', out)

    tokens = out.lower().split(' ')

    counter = Counter()
    for word in tokens:
        if not word in stop_words:
           counter[word] = counter[word] + 1

    print(counter)


if __name__ == "__main__":
    main()
