import re
with open("0004.txt", 'r', encoding='utf-8') as fd:
		coca_word_list = fd.read()

#只匹配字母，符号数字不匹配
word_list = re.findall('[a-zA-Z]+', coca_word_list)

num_dic = {}
for w in word_list:
    if w in num_dic:
        num_dic[w] = num_dic.get(w) + 1
    else:
        num_dic.setdefault(w, 1)

print(num_dic)

