
class Proxy:
    def __init__(self, subject):
        self._subject = subject
        self._proxystate = None

class Image:
    def __init__(self, filename):
        self._filename = filename

    def load_image_from_disk(self):
        print(f'Loading {self._filename}')

    def display_image(self):
        print(f'Display {self._filename}')


class ProxyImage(Proxy):
    def display_image(self):
        if self._proxystate is None:
            self._subject.load_image_from_disk()
            self._proxystate = 1
        print(f'Display {self._subject._filename}')


def main():
    images = [ProxyImage(Image('photo_1')), ProxyImage(Image('photo_2'))]
    load_n_times = 6
    print(f'Attempting to lead each images {load_n_times} times...')
    for i in range(load_n_times):
        img_index = i % len(images)
        print(f'Attempt {int(i/2)+1} on Image{img_index+1}:', end=' ')
        images[img_index].display_image()


if __name__ == '__main__':
    main()
