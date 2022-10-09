import pandas as pd
import jieba
from wordcloud import WordCloud


def fenci(tempstr):
    wordlist = jieba.cut(tempstr)
    result = ' '.join(wordlist)
    return result


if __name__ == '__main__':
    data = pd.read_csv('D:\\Programming\\crawler_comment\\Comments.csv').astype(str)
    comment = data['comment'].values.tolist()
    string = ''
    for i in range(len(comment)):
        string += fenci(comment[i])
    stopwords = {'豆瓣', '说', '本', '书', '本书', '一本', '想', '写', '阅读', '建议', '看', 'comment', '都', '不', '没有', '不是'}
    content = [line.strip() for line in open('hit_stopwords.txt', 'r', encoding='utf-8').readlines()]
    stopwords.update(content)
    w = WordCloud(font_path="msyh.ttc",       # 微软雅黑
                  width=1600,
                  height=800,
                  background_color="white",   # 白色背景
                  max_font_size=150,          # 最大字体
                  max_words=1000,             # 最大词数
                  stopwords=stopwords)
    w.generate(string)
    image = w.to_image()
    w.to_file('ciyun.png')
    image.show()
