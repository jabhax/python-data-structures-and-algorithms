class MakeSomeThing:
    def prepare(self): pass
    def do_first(self): pass
    def do_something(self): pass
    def do_last(self): pass

    def make(self):
        self.prepare()
        self.do_first()
        self.do_something()
        self.do_last()
        print()

class Meal(MakeSomeThing):
    def prepare(self): print('Prepare Meal')
    def do_first(self): print('Cook Meal')
    def do_something(self): print('Eat Meal')
    def do_last(self): print('Save Leftover Meal')

class Car(MakeSomeThing):
    def prepare(self): print('Prepare Car Parts')
    def do_first(self): print('Attach Car Parts')
    def do_something(self): print('Start Car')
    def do_last(self): print('Drive')

class SomethingElse(MakeSomeThing):
    def prepare(self): print('Prepare Something Else')
    def do_first(self): print('Do this first')
    def do_something(self): print('Do Something here')
    def do_last(self): print('Do this last')


def main():
    makeMeal = Meal()
    makeMeal.make()

    makeCar = Car()
    makeCar.make()

    makeSomethingElse = SomethingElse()
    makeSomethingElse.make()


if __name__ == '__main__':
    main()
