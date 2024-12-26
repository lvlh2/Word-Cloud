#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File: word_cloud.py
@Time: 2024/12/26 19:01:52
@Author: lvlh2
"""


import os
from collections import Counter
from pathlib import Path

import jieba
import matplotlib.pyplot as plt
from wordcloud import WordCloud


def main():
    os.chdir(Path(__file__).parent)

    pic = plt.imread('mask.png')

    # The mask of the word cloud should be an `int` array.
    pic = pic.astype('int')

    mask = pic[:, :, -1] == 0
    for i in range(3):
        pic[:, :, i][mask] = 255
        pic[:, :, i][~mask] = 0

    with open('哈工大停用词表.txt', 'r', encoding='utf-8') as f:
        stop_words = [line.strip() for line in f]

    with open('comments.txt', 'r', encoding='utf-8') as f:
        words = [word for word in jieba.cut(f.read()) if word not in stop_words]

    word_freq = Counter(words)

    wc = WordCloud(
        font_path='simhei.ttf',
        background_color='white',
        mask=pic,
        scale=3,
        contour_color='#000000',
        contour_width=2,
        random_state=0,
        max_font_size=80,
    )
    wc.generate_from_frequencies(word_freq)

    fig, ax = plt.subplots()
    ax.imshow(wc, interpolation='bilinear')
    ax.set_axis_off()
    fig.tight_layout()

    fig.savefig('ayachi_nene.png', dpi=300)


if __name__ == '__main__':
    main()
