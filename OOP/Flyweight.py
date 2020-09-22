# Design Patterns

'''
The Flyweight Pattern provides a way to decrease object count. It includes
features that help in improving application structure. The most important
feature of the Flyweight objects is immutabilty; they cannot be modified once
constructed. The pattern uses a HashMap to store reference objects.
'''

class ComplexGenes(object):
    def __init__(self): pass

    def genes(self, gene_code):
        return f'ComplexPattern{gene_code}TooHugeInSize'


class Families(object):
    _family = {}
    def __new__(cls, name, fid):
        try:
            id = cls._family[fid]
        except KeyError:
            id = object.__new__(cls)
            cls._family[fid] = id
        return id

    def set_gen_info(self, gen_info):
        cg = ComplexGenes()
        self._genetic_info = cg.genes(gen_info)

    def get_gen_info(self):
        return self._genetic_info


def main():
    data, families = (('a', 1, 'ATAG'), ('a', 2, 'AAGT'), ('b', 1, 'ATAG')), []
    for i in data:
        obj = Families(i[0], i[1])
        obj.set_gen_info(i[2])
        families.append(obj)

    for i in families:
        print(f'id: {str(id(i))}')
        print(f'{i.get_gen_info()}')


if __name__ == '__main__':
    main()
