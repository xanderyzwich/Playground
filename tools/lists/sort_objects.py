if __name__ == '__main__':
    entries = []
    with open('sort_objects.csv', 'r') as file_in:
        for line in file_in:
            name, value = line.split(',')
            entries.append((name, float(value)))
    for key, value in sorted(entries, key=lambda x: x[1], reverse=True):
        print(key, value)
