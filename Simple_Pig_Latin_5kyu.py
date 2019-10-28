def pig_it(text):
    res_word = ""
    list_of_words_w = text.split(" ", len(text))
    list_of_words = []
    for i in range(len(list_of_words_w)):
        if list_of_words_w[i] not in ["!", ".", "?"]:
            list_of_words.append(list_of_words_w[i])
    for i in range(len(list_of_words)):
        for j in range(1, len(list_of_words[i])):
            res_word += list_of_words[i][j]
        res_word += list_of_words[i][0]
        res_word += "ay "
    for word in list_of_words_w:
        if word in ["!", ".", "?"]:
            res_word += word
            return res_word 
    return res_word[:-1]
