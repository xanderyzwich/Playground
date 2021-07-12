from re import sub as re_sub
from sys import argv as sys_argv

def palindrome_check(input_string):
    check_string = sanitize_string(input_string)
    return check_string == check_string[::-1]

def sanitize_string(input_string):
    keep_characters = 'abcdefghijklmnopqrstuvwxyz'
    return re.sub(r'[^\w'+keep_characters+']', '', input_string.lower())


if __name__ == "__main__":
    palindromes_positive = ['Race Car', 'racecar', 'anna', 'ciVIc', 'kayak', 'LEVeL', 'MADAM', 'mom', 'noOn', 'raDaR',
                            'Redder', 'REfer', 'RePaPeR', 'RotatOr', 'rOtOr', 'SAgaS', 'soloS', 'STatS', 'teNEt', 'WoW',
                            "Don't nod", "I did, did I?", "My gym", "Red rum, sir, is murder", "Step on no pets",
                            "Top spot", "Was it a cat I saw?", "Eva can I see bees in a cave?", "No lemon, no melon"]
    palindromes_negative = ['Corey', 'Lawrence', 'RJ', 'Coriano', 'JC', 'Parhaml', 'Walker']
    for palindrome in palindromes_positive + palindromes_negative:
        print(palindrome, palindrome_check(palindrome))


