def char_frequency(sentence):
    if not sentence or not sentence.strip():
        return []
    
    sentence = sentence.lower().replace(" ", "")

    keyFreq = dict()
    for char in sentence :
        #get the value, if key does not exist, create it
        keyFreq[char] = keyFreq.get(char, 0) + 1

    result = sorted(keyFreq.items(), key=lambda item:(-item[1], item[0]))
    return result


if __name__ == "__main__" :
    print(char_frequency("Miss ippi"))