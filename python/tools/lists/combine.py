def combine_alternating(input_a, input_b):
    list_a, list_b = input_a[::-1], input_b[::-1]
    list_c = []
    for i in range(max(len(input_a), len(input_b))):
        if i < len(input_a):
            list_c.append(list_a.pop())
        if i < len(input_b):
            list_c.append(list_b.pop())
    return list_c

def combine_alternating_alternate(input_a, input_b):
    # return [y for x in itertools.zip_longest(input_a, input_b) for y in x if y is not None]
    return [y for x in itertools.zip_longest(input_a, input_b) for y in x if y]

if __name__ == "__main__":
    import itertools
    a, b = ['a', 'b', 'c', 'd', 'e'], ['1', '2', '3']

    print(combine_alternating(a, b))
    print(combine_alternating_alternate(a, b))
