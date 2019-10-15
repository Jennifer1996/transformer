train1 = "iwslt2016/de-en/train.tags.de-en.de"
#源码
_prepro = lambda x:  [line.strip() for line in open(x, 'r').read().split("\n") \
                      if not line.startswith("<")]
#练习
_a = lambda x:  [line.strip() for line in open(x,'r').read().split("\n") \
              if not line.startswith("<")]

#总结：学会了使用匿名函数载入文件的方法，这样写效率高，简洁优美
train1 = _a(train1)
print(len(train1))


import re

eval1 = "iwslt2016/de-en/IWSLT16.TED.tst2013.de-en.de.xml"
eval2 = "iwslt2016/de-en/IWSLT16.TED.tst2013.de-en.en.xml"
#源码
_prepro = lambda x: [re.sub("<[^>]+>", "", line).strip() \
                     for line in open(x, 'r').read().split("\n") \
                     if line.startswith("<seg id")]

#练习：注意这里正则表达式的书写
""
_b = lambda x: [re.sub('<[^>]+>',"",line).strip()\
                for line in open(x,'r').read().split('\n')\
                if line.startswith('<seg id')]
prepro_eval1, prepro_eval2 = _b(eval1), _b(eval2)
print(len(prepro_eval1))
print(len(prepro_eval2))
print(prepro_eval2)
assert len(prepro_eval1) == len(prepro_eval2), "Check if eval source and target files match."

str = '<seg id="1"> Als ich 11 Jahre alt war, wurde ich eines Morgens von den Klängen heller Freude geweckt. </seg>'
print(re.sub("<"))