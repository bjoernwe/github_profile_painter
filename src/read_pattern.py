import numpy as np
import PIL.Image


def main():
    file_name = '../res/pattern.png'
    img = PIL.Image.open(file_name)
    print(3-np.array(img))


if __name__ == '__main__':
    main()
