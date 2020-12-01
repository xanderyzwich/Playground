if __name__ == '__main__':
    start_level, start_shards = 10, 0
    new_shards = 20

    current_level = start_level
    current_shards = start_shards
    unused_shards = new_shards

    while unused_shards > 0:
        while current_level >= current_shards and unused_shards > 0:
            current_shards += 1
            unused_shards -= 1

        if current_shards == current_level + 1:
            current_level += 1
            current_shards = 0

    print(f'Final Level : {current_level}')
    print(f'Final shards: {current_shards}')
