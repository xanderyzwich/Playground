def function_name(one, two,  three, four):
    return one + two + three + four

if __name__ == '__main__':
    args_dict = {
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4
    }
    print(function_name(**args_dict))
