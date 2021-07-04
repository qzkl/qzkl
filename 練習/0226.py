import sys
import string
import itertools
import time
start = time.time()

word1 = 'READ'  
word2 = 'WRITE'
word3 = 'TALK'
word4 = 'SKILL'

words = ''.join([word1,word2,word3,word4])
char_set = set(words)
length = len(char_set)
if length > 10 :
    sys.exit('too many characters')

count = 0
for number in itertools.permutations('0123456789',length) :
    number_strings = ''.join(number)
    fig1 = word1.translate(str.maketrans(''.join(char_set),number_strings))
    fig2 = word2.translate(str.maketrans(''.join(char_set),number_strings))
    fig3 = word3.translate(str.maketrans(''.join(char_set),number_strings))
    fig4 = word4.translate(str.maketrans(''.join(char_set),number_strings))

    if fig1[0] == '0' or fig2[0] == '0' or fig3[0] == '0' or fig4[0] == '0' :
        continue

    if int(fig1) + int(fig2) + int(fig3) == int(fig4) :
        print (fig1, '+', fig2, '+', fig3, '==', fig4)
        count += 1

print (count)

elapsed_time = time.time() - start
print(elapsed_time)