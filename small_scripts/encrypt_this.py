def encrypt_this(text):
    result = []
    for word in text.split():
        if len(word) >= 3:
            word = str(ord(word[0])) + word[-1] +word[2:-1] + word[1]
            result.append(word)
        elif len(word) == 2:
            word = str(ord(word[0])) + word[1]
            result.append(word)
        else:
            result.append(str(ord(word)))
    result = " ".join(result)
    print(result)


encrypt_this("A wise old owl lived in an oak")
