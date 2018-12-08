import re
file_object = open("article.txt", "r")
wordcount = dict()
def word_count(file_name):
    for line in file_object:
        words = re.split(r'\W+',line.lower())
        for word in words:
            if word not in wordcount:
                wordcount[word] = 1
            else:
                wordcount[word] += 1
    

def word_stat(str1,num):
    word_count(str1)
    sorted_by_value = sorted(wordcount.items(), key=lambda kv: kv[1], reverse = True)
    return sorted_by_value[:num]


print(word_stat("article.txt",10))
file_object.close()

