import pandas as pd
import jieba.analyse
from wordcloud import WordCloud


def fenci(tempstr):
    wordlist = jieba.analyse.extract_tags(tempstr)
    result = ' '.join(wordlist)
    return result


if __name__ == '__main__':
    try:
        name = input('请输入书名生成词云：')
        data = pd.read_csv('D:\\Programming\\crawler_comment\\Comments.csv').astype(str)
        comment = data[data['bookname'] == name]['comment'].values.tolist()
        string = ''
        for i in range(len(comment)):
            string += fenci(comment[i])
        stopwords = {'豆瓣', '书', '本书', '一本', '想', '说', '写', '读', '读完', '读过', '看', 'comment', '真的', '觉得', '其实'}
        content = [line.strip() for line in open('cn_stopwords.txt', 'r', encoding='utf-8').readlines()]
        stopwords.update(content)
        w = WordCloud(font_path="msyh.ttc",  # 微软雅黑
                      width=1600,
                      height=800,
                      background_color="white",  # 白色背景
                      max_font_size=300,  # 最大字体
                      max_words=100,  # 最大词数
                      stopwords=stopwords)
        w.generate(string)
        image = w.to_image()
        w.to_file(name + '.png')
        image.show()
    except ValueError:
        print('此书不位于豆瓣读书TOP100中！')

