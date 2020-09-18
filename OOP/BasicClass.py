

class BasicClass:
    def instance_method(self):
        return 'Called instance Method', self

    @classmethod
    def class_method(cls):
        return 'Called class Method', cls

    @staticmethod
    def static_method():
        return 'Called static Method'


def main():
    basic_obj = BasicClass()
    # Instance method calls
    print(f'basic_obj.instance_method(): { basic_obj.instance_method() }')
    print(f'BasicClass.instance_method(basic_obj): { BasicClass.instance_method(basic_obj) }\n')
    # Class method calls
    print(f'basic_obj.class_method(): { basic_obj.class_method() }')
    print(f'BasicClass.class_method(): { BasicClass.class_method() }\n')
    # Static method calls
    print(f'basic_obj.static_method(): { basic_obj.static_method() }')
    print(f'BasicClass.static_method(): { BasicClass.static_method() }')


if __name__ == '__main__':
    main()
