
def eng_to_pig(input_string):
    suffix = 'ay'
    consonants = 'bcdfghjklmnpqrstvwxyz'
    tokens = input_string.split()
    pig_tokens = []
    for token in tokens:
        pig_token = ''
        if token[0].lower() in consonants:
            pig_token = token[1::] + token[0] + suffix
        else:
            pig_token = token + suffix
        if token[0].lower() == token[0]:
            pig_tokens.append(pig_token)
        else:
            pig_tokens.append(pig_token[0].upper() + pig_token[1::].lower())

    return ' '.join(pig_tokens)

def pig_latin_to_english(string):
    suffix = 'ay'
    split = string.split(' ')
    outstring = ' '.join([word[-3].lower() + word[:-3].lower() for word in split])
    outstring = outstring[0].upper() + outstring[1:]
    return outstring


if __name__ == '__main__':
    test_string = "The quick brown fox"
    test_string_pig = eng_to_pig(test_string)
    print(test_string_pig)
    print(pig_latin_to_english(test_string_pig))
    test_string = "my milkshake brings all the boys to the yard"
    test_string_pig = eng_to_pig(test_string)
    print(test_string_pig)
    print(pig_latin_to_english(test_string_pig))
