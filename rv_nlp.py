# rv_nlp.py
"""
Program outputs the top n words (by occurence) from a text file, in descending order, excluding words found in common file
"""
# setup
#   Python 3.6
#   pip install textblob
#   pip install pandas
#
# Assumptions:
#   the input files are in the same directory as the program
#  
# required arguments:
#   1 text file containing english text
#   2 text file containing words to exclude (stop-words)
#   3 number of results (top-n)
#
# running:
# python rv_nlp.py alice_in_wonderland.txt common.txt 5

# python standard library
from pathlib import Path
from operator import itemgetter
import sys

# extrenal pip-installed libraries
from textblob import TextBlob
import pandas as pd

def main(args):
    # load the files
    blob = TextBlob(Path(args[0]).read_text())
    stop_words = TextBlob(Path(args[1]).read_text())
    n = int(args[2])


    # create word tuples (word, count)
    word_tuples = blob.word_counts.items()

    # remove stop_words from the word_tuples list
    word_tuples = [item for item in word_tuples if item[0] not in stop_words]

    # sort word_tuples in descending order by count
    sorted_words = sorted(word_tuples, key=itemgetter(1), reverse=True)

    # isolate the top n words
    top_n = sorted_words[0:n]

    # use pandas dataframe to display output
    df = pd.DataFrame(top_n, columns=['word','count'])
    df = df.reindex(columns=['count','word'])

    print(df.to_string(index=False))

if __name__ == "__main__":
    # validate inputs
    if(len(sys.argv) == 4 and Path(sys.argv[1]).exists() and Path(sys.argv[2]).exists() and sys.argv[3].isnumeric()):
            main(sys.argv[1:])
    else: print('3 arguments required -> python rv_npl.py text-file.txt common-file.txt int')