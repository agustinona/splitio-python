from typing import final
from wordcloud import WordCloud, STOPWORDS
import pandas as pd
import matplotlib.pyplot as plt
from operator import itemgetter

# source file should be csv export from zendesk
filePath = "~/Downloads/export-2021-05-31-1738-1576017-3600054272116e62.csv"

# Read data file
data = pd.read_csv(filePath)

subjectWords = ""
myStopWords = [
    "the",
    "a",
    "an",
    "in",
    "is",
    "into",
    "and",
    "issue",
    "error",
    "with",
    "for",
    "on",
    "to",
    "re",
    "re:",
    "of",
    "help",
    "question",
    "hi",
    "splitio",
    "that",
    "we",
    "have",
    "are",
    "about",
    "not",
    "i",
    "fwd",
    "fwd:",
    "...",
    "hi,",
    "-",
    "our",
    "my",
    "using",
    "when",
    "from",
    "i'm",
    "hello",
]

# iterate through data
for i in data.Subject:
    i = str(i)
    separate = i.split()
    for j in range(len(separate)):
        separate[j] = separate[j].lower()
    subjectWords += " ".join(separate) + " "

# count word frequency
subjectWordsArr = subjectWords.split()
uniqueWords = set(subjectWordsArr)
for word in myStopWords:
    uniqueWords.discard(word)
subjectWordsFreq = []
for word in uniqueWords:
    subjectWordsFreq.append([word, subjectWordsArr.count(word)])

# print most repeated words
amountOfEntriesToShow = 20
subjectWordsFreq = sorted(subjectWordsFreq, key=itemgetter(1), reverse=True)
dashSep = "-" * 30
print("Top " + str(amountOfEntriesToShow) + " words:")
print("{:<20s}{:<4s}".format("Word", "Freq"))
print(dashSep)
for entry in subjectWordsFreq[0:amountOfEntriesToShow]:
    print("{:<20s}{:>4d}".format(entry[0], entry[1]))

# create wordcloud
finalWordcloud = WordCloud(
    width=800,
    height=800,
    background_color="black",
    stopwords=myStopWords,
    min_font_size=10,
).generate(subjectWords)

# display wordcloud
plt.figure(figsize=(10, 10), facecolor=None)
plt.imshow(finalWordcloud)
plt.axis("off")
plt.tight_layout(pad=0)

plt.show()
