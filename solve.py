import sys

print('sys.argv[1]      : ', sys.argv[1])
print('sys.argv[2]      : ', sys.argv[2])

common_char=''
for word1 in sys.argv[1]:
    for word2 in sys.argv[2]:
        pass 
        if word1 == word2 :
            if word1 in common_char:
                continue
            common_char += word1

print(common_char)