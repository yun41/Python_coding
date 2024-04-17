import re
string_word = input('여러 단어로 이루어진 글을 입력하세요: ')

string_Word = re.split("[:|,| |.|]",string_word)
while '' in string_Word:
    string_Word.remove('')
string_Word.sort()
print(string_Word)