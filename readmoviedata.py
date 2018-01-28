# -*- coding=utf-8 -*-'''

import jieba    #分词包
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import numpy


cleaned_comments = ''
for line in open("file\michao.txt",'r',encoding= 'UTF-8'):
    cleaned_comments = cleaned_comments+line

segment = jieba._lcut(cleaned_comments)
word_count = pd.DataFrame({'segment':segment})
stop_words = pd.read_csv("stopwords.txt",index_col=False,quoting=3, sep="\t", names=['stopword'],encoding='utf-8')
word_count = word_count[~word_count.segment.isin(stop_words.stopword)]
# 统计词频
words_stat = word_count.groupby(by=['segment'])['segment'].agg({"size"})
words_stat = words_stat.reset_index().sort_values(by=["size"], ascending=False)
word_count = word_count.groupby(['segment']).size()
# print(word_count.sort_values(ascending=False))

# 用词云进行显示
wordcloud = WordCloud(font_path="simhei.ttf", background_color="white", max_font_size=80)  # 指定字体类型、字体大小和字体颜色
word_frequence = {x[0]: x[1] for x in words_stat.head(1000).values}

word_frequence_list = []
for key in word_frequence:
    temp = (key, word_frequence[key])
    word_frequence_list.append(temp)

wordcloud = wordcloud.fit_words(dict(word_frequence_list))
plt.imsave('file\img.jpg', wordcloud)

plt.imshow(wordcloud,interpolation='bilinear')