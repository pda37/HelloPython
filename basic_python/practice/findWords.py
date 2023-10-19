# from string import maketrans

def findWords(words):
    ans = []
    table = str.maketrans('qwertyuiopQWERTYUIOPasdfghjklASDFGHJKLzxcvbnmZXCVBNM', '1111111111111111111122222222222222222233333333333333')
    for i in range(len(words)):
        if len(set(words[i].translate(table))) == 1:
            ans.append(words[i])
    return ans


print(findWords(["Hello", "Alaska", "Dad", "Peace"]))