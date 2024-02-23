import numpy as np


def count_rooms(floor_map: np.ndarray) -> int:

    return len(floor_map.nonzero()[0])


def make_floor(desired_rooms=10):
    # create a 20 x 20 matrix of zeros to hold our floor map
    size = 20

    x = int(size / 2)
    y = int(size / 2)

    floor_map = np.zeros((size, size), dtype=int)

    while count_rooms(floor_map) < desired_rooms:
        # randomly choose a direction to move
        direction = np.random.choice(["up", "down", "left", "right"])

        if direction == "up" and y > 0:
            floor_map[x, y] |= 1
            y -= 1
            floor_map[x, y] |= 4
        elif direction == "right" and x < size - 1:
            floor_map[x, y] |= 2
            x += 1
            floor_map[x, y] |= 8
        elif direction == "down" and y < size - 1:
            floor_map[x, y] |= 4
            y += 1
            floor_map[x, y] |= 1
        elif direction == "left" and x > 0:
            floor_map[x, y] |= 8
            x -= 1
            floor_map[x, y] |= 2

    return floor_map


def main():
    while True:
        print(make_floor(int(input("How many rooms?"))))


if __name__ == "__main__":

    main()