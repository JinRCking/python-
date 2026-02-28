import jieba
excludes={}
txt=open("三国演义.txt","r",encoding='utf-8').read()
'''open("三国演义.txt", "r", encoding='utf-8')：以只读模式打开名为《三国演义》的文本文件，文件编码为 UTF-8。
.read()：读取文件的全部内容，并将其作为一个字符串返回。'''
words=jieba.lcut(txt)
counts={}
for word in words:
    if len(word)==1:
        continue
    else:
        counts[word]=counts.get(word,0)+1
for word in excludes:
    del(counts[word])
items=list(counts.items())
items.sort(key=lambda x:x[1],reverse=True)
for i in range(15):
    word,count=items[i]
    print("{0:<10}{1:>5}".format(word,count))