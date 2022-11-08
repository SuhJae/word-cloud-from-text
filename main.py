import matplotlib.pyplot as plt
from wordcloud import WordCloud
from PIL import Image
import numpy as np


class BC:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'


print(f'{BC.OKGREEN}✓{BC.RESET} Importing modules')

# read the word.txt file
text = open('word.txt').read()
print(f'{BC.OKGREEN}✓{BC.RESET} Reading word.txt')

mask = np.array(Image.open('mask.png'))

print(f'{BC.OKGREEN}✓{BC.RESET} Reading mask.png')

# stopwords
stopwords = ["CASSIUS", "BRUTUS", "ANTONY", "CAESAR", "Calpurnia", "Octavius", "Casca", "Portia", "Flavius", "Cicero",
             "Lepidus", "Murellus", "Decius", "MARULLUS", "LUCIUS", "ourselves", "out", "over", "own", "same", "shan't",
             "she", "she'd", "she'll", "she's", "should", "shouldn't", "so", "some", "such", "than", "that", "that's",
             "the", "their", "theirs", "them", "themselves", "then", "there", "there's", "these", "they", "they'd",
             "they'll", "they're", "they've", "this", "those", "through", "to", "too", "under", "until", "up", "very",
             "was", "wasn't", "we", "we'd", "we'll", "we're", "we've", "were", "weren't", "what", "what's", "when",
             "when's", "where", "where's", "which", "while", "who", "who's", "whom", "why", "why's", "with", "won't",
             "would", "wouldn't", "you", "you'd", "you'll", "you're", "you've", "your", "yours", "yourself",
             "yourselves", "", "a", "about", "above", "after", "again", "against", "all", "am", "an", "and", "any",
             "are", "aren't", "as", "at", "be", "because", "been", "before", "being", "below", "between", "both", "but",
             "by", "can't", "cannot", "could", "couldn't", "did", "didn't", "do", "does", "doesn't", "doing", "don't",
             "down", "during", "each", "few", "for", "from", "further", "had", "hadn't", "has", "hasn't", "have",
             "haven't", "having", "he", "he'd", "he'll", "he's", "her", "here", "here's", "hers", "herself", "him",
             "himself", "his", "how", "how's", "i", "i'd", "i'll", "i'm", "i've", "if", "in", "into", "is", "isn't",
             "it", "it's", "its", "itself", "let's", "me", "more", "most", "mustn't", "my", "myself", "no", "nor",
             "not", "of", "off", "on", "once", "only", "or", "other", "ought", "our", "ours", "will", "shall", "thou",
             "MESSALA", "now", "Enter", "Come", "Exit", "Let",
             "Cinna", "Ligarius", "Lucilius", " Titinius", " Voluminus", " Trebonius", " Claudius", " Pindarus", "Cimber", " Metullus", " Publius", " Pompey", " Artemeidorus", "Mark"
             ]

# create the wordcloud object
wordcloud = WordCloud(colormap='cool', background_color="black", max_words=10000, collocations=False, mask=mask, font_path="times new roman.ttf", stopwords=stopwords).generate(text)
# wordcloud = WordCloud(colormap='cool', background_color="black", collocations=False, font_path="times new roman.ttf", stopwords=stopwords, height=2000, width=4000, max_words=10000).generate(text)

print(f'{BC.OKGREEN}✓{BC.RESET} Generating wordcloud')

# display the generated image
plt.figure(figsize=(15, 8))
plt.axis("off")

plt.imshow(wordcloud, interpolation='bilinear')

# save the image
wordcloud.to_file("wordcloud.png")

print(f'{BC.OKGREEN}✓{BC.RESET} Saving wordcloud.png')
