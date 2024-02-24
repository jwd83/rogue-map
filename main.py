import mapmaker
import pygame
import numpy as np


def main():
    max_map_dimension = 20

    block_size = 360 / max_map_dimension / 2
    dead_ends = [1, 2, 4, 8]

    level_map = mapmaker.make_floor(
        minimum_rooms=int(input("How many rooms? ")),
        desired_dead_ends=int(input("How many dead ends? (0 for random): ")),
        size=max_map_dimension,
    )
    print("Map generated")

    pygame.init()

    screen = pygame.display.set_mode((640, 360))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

            # check for escape key
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    return

        screen.fill((0, 0, 0))

        for x in range(level_map.shape[0]):
            for y in range(level_map.shape[1]):
                if level_map[x, y] != 0:

                    color = (255, 0, 0)

                    # color dead ends green
                    if level_map[x, y] in dead_ends:
                        color = (0, 255, 0)

                    # color 4 way spokes room purple
                    if level_map[x, y] & 15 == 15:
                        color = (255, 0, 255)

                    # color starting room blue
                    if level_map[x, y] & 16:
                        color = (0, 0, 255)

                    pygame.draw.rect(
                        screen,
                        color,
                        (
                            x * block_size * 2 + 1,
                            y * block_size * 2 + 1,
                            block_size,
                            block_size,
                        ),
                    )

                    if level_map[x, y] & 1:
                        pygame.draw.rect(
                            screen,
                            color,
                            (
                                x * block_size * 2 + block_size / 2 + 1,
                                y * block_size * 2 + 1 - block_size,
                                1,
                                block_size,
                            ),
                        )

                    if level_map[x, y] & 2:
                        pygame.draw.rect(
                            screen,
                            color,
                            (
                                x * block_size * 2 + block_size + 1,
                                y * block_size * 2 + block_size / 2 + 1,
                                block_size,
                                1,
                            ),
                        )

                    if level_map[x, y] & 4:
                        pygame.draw.rect(
                            screen,
                            color,
                            (
                                x * block_size * 2 + block_size / 2 + 1,
                                y * block_size * 2 + block_size + 1,
                                1,
                                block_size,
                            ),
                        )

        pygame.display.flip()


if __name__ == "__main__":
    main()
