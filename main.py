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

# create the wordcloud object
wordcloud = WordCloud(colormap='binary', background_color="white", max_words=10000, collocations=False, mask=mask, font_path="times new roman.ttf").generate(text)

print(f'{BC.OKGREEN}✓{BC.RESET} Generating wordcloud')

# display the generated image
plt.figure(figsize=(15, 8))
plt.axis("off")

plt.imshow(wordcloud, interpolation='bilinear')

# save the image
wordcloud.to_file("wordcloud.png")

print(f'{BC.OKGREEN}✓{BC.RESET} Saving wordcloud.png')