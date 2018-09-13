#!/usr/bin/env
"""
Requires: 3.6+
Created: 11/02/2018
Author: @BrendanMoore42

Text to Cloud converts a subtitle movie file to a word cloud.

Subtitles are stored in .srt format, and contain a good
approximation of the movie's script.

Images must be in jpeg format, preferably black and white.
Srt's can be acquired by searching https://www.yifysubtitles.com

Cloud parameters can be changed in the make_cloud() function to add
words, change colors, contours etc.

Will output a .txt file without srt instructions and a png image into
the same directory.

Run from command line, example: James Bond - Goldfinger

    $ python txt_to_cloud.py goldfinger.srt jamesbond.jpg

If error, change encoding as 4th argument:

    $ python txt_to_cloud.py goldfinger.srt jamesbond.jpg cp1252
"""
import re, sys
from PIL import Image
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
from collections import Counter
from wordcloud import WordCloud, STOPWORDS

# if wordcloud stopwords isn't effective, use sklearn stopwords
# or add to random_stopwords
# from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS

# import stop words
stopwords = STOPWORDS

# the following check and clean srt specific lines
def is_time_stamp(l):
    if l[:2].isnumeric() and l[2] == ':':
        return True
    return False


def has_letters(line):
    if re.search('[a-zA-Z]', line):
        return True
    return False


def has_no_text(line):
    l = line.strip()
    if not len(l):
        return True
    if l.isnumeric():
        return True
    if is_time_stamp(l):
        return True
    if l[0] == '(' and l[-1] == ')':
        return True
    if not has_letters(line):
        return True
    return False


def is_lowercase_letter_or_comma(letter):
    if letter.isalpha() and letter.lower() == letter:
        return True
    if letter == ',':
        return True
    return False

# removes non-text lines, combines broken lines
def clean_up(lines):
    # add 'text' to list so the dataframe has a column name
    new_lines = ['text\n']
    for line in lines[1:]:
        if has_no_text(line):
            continue
        elif len(new_lines) and is_lowercase_letter_or_comma(line[0]):
            #combine with previous line
            new_lines[-1] = new_lines[-1].strip() + ' ' + line
        else:
            #append line
            new_lines.append(line)
    return new_lines


# convert srt to txt file in directory, stores txt as variable
def srt_to_txt(srt_file, encoding):
    with open(srt_file, encoding=encoding, errors='replace') as f:
        lines = f.readlines()
        new_lines = clean_up(lines)
    new_file_name = srt_file[:-4] + '.txt'
    with open(new_file_name, 'w') as f:
        # add 'text' to list so the dataframe has a column name
        f.write('text\n')
        for line in new_lines:
            f.write(line)
    # for variable use in the main function and not to write to disk again
    return new_lines

# puts .txt file into a dataframe, returns df
def to_df(text):
    df = pd.read_csv(pd.compat.StringIO("\n".join(text)), sep=";")
    #remove puncutation
    df['text'] = df['text'].str.replace('[^\w\s]', '')
    return df

# counts the number of words and and creates dictionary for use in make_cloud()
def get_words(df, col='text'):
    new_results_list = []

    # count words for word cloud
    results = Counter()
    words_to_results = df['text'].str.lower().str.split().apply(results.update)

    # sort words
    new_results = results.most_common()

    # ADD WORDS YOU DON'T WANT HERE, if they come up
    random_stopwords = ['rt', '&amp;', '-', '.', '→',
                        'v', '&', '|', '-&gt;', 'totn',
                        "it's", '^cs', "b's", '^ji', '^bb',
                        '--&gt;', 'font', 'color808080banefont',
                        'color808080waynefont', 'color808080',
                        '1font'] #for example

    # clean results list
    for i in range(len(new_results)):
        if new_results[i][0] in stopwords:
            continue
        if new_results[i][0] in random_stopwords:
            continue
        else:
            new_results_list.append(new_results[i])

    # send to wordcloud
    clean_cloud = dict(new_results_list)
    return clean_cloud


def make_cloud(text, image, bac_colour='white', cont_color='white', 
col_map='autumn'):
    """
    text: dictionary key:value pair, count:word, sorted by highest
    image: .jpg file, solid fill greater than 1024x768,
            typically an inverse of a logo
    bac_colour: sets image background colour, will fill behind words,
                white is cleanest.
    cont_color: colours the contour around the image,
                set to 'white' by default.
    col_map: matplotlib gradient, search
             https://matplotlib.org/users/colormaps.html
             for available options
    """
    # import image
    logo_mask = np.array(Image.open(f'{image}'))
    file_name = image[:-4] + '.png'

    # generate a wordcloud to image
    stopwords = STOPWORDS
    wc = WordCloud(background_color=bac_colour,
                   max_words=140, mask=logo_mask,
                   contour_width=0, contour_color=cont_color,
                   colormap=col_map)
    wc.generate_from_frequencies(text)
    plt.figure(figsize=(25, 25))
    plt.imshow(wc, interpolation='bilinear')
    plt.axis("off")
    plt.savefig(file_name)
    plt.show();

# main function
def main(args):
    """
    args[1] = srt file to convert
    args[2] = image to mask as cloud
    args[3] = encoding, default utf-8, else change to 'cp1252'
    """
    # create file names to use in functions
    srt_file = args[1]
    img_file = args[2]
    # if error occurs, type cp1252 as the last argument to convert
    encoding = 'utf-8' if len(args) < 4 else args[3]
    # create .txt file from .srt file
    txt = srt_to_txt(srt_file, encoding)
    # create dataframe to hold text
    df = to_df(txt)
    # count words and order by frequency
    words_to_cloud = get_words(df)
    # send to cloud, save and output image
    make_cloud(words_to_cloud, img_file)

if __name__ == '__main__':
    # run from command line
    main(sys.argv)
