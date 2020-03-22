import numpy as np
import PIL.Image


PATTERN_WIDTH = 27
PATTERN_N_COLORS = 3


def read_patter_from_file(file_name) -> np.array:
    img = PIL.Image.open(file_name)
    img = PATTERN_N_COLORS - np.array(img)[:, :PATTERN_WIDTH]
    return img


def print_pattern(img: np.array):
    for row in img:
        print(str(list(row)))


def main():
    file_name = '../res/pattern.png'
    img = read_patter_from_file(file_name)
    print_pattern(img)


if __name__ == '__main__':
    main()
