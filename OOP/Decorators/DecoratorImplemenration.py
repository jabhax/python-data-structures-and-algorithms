# Design Patterns

import ShopDecorator


def main():
    item = ShopDecorator.ConcreteItem()
    print(item)
    a = ShopDecorator.PartA(item)
    print(a)
    b = ShopDecorator.PartB(item)
    print(b)
    c = ShopDecorator.PartC(item)
    print(c)


if __name__ == '__main__':
    main()
