"""
Tools for making cycling adjustments
"""


def get_time(speed, distance):
    # mph = m / h
    # h * mph = mi
    # h = mi / mph
    return distance / speed


if __name__ == '__main__':
    lap_distance = 4.4  # miles
    average_speed = 12  # mph
    minutes = get_time(average_speed, lap_distance) % 1 * 60
    minutes, seconds = minutes // 1, (minutes % 1) * 60 // 1

    print(f'A {lap_distance} mile lap at {average_speed} mph take {minutes} minutes and {seconds} seconds')
