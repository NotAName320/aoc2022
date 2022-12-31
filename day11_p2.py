class Monkey():
    def __init__(self, items, operation, test, if_true, if_false):
        self.items = items
        self.operation = operation
        self.test = test
        self.if_true = if_true
        self.if_false = if_false
        self.num_inspected = 0

    def add_items(self, items):  # remember to always follow correct practice with object attributes!
        self.items += items

    def process(self, supermod):
        throw_true, throw_false = [], []
        for i in range(len(self.items)):
            self.items[i] = self.operation(self.items[i]) % supermod

            if self.items[i] % self.test == 0:
                throw_true.append(self.items[i])
            else:
                throw_false.append(self.items[i])

            self.num_inspected += 1

        self.items = []
        return throw_true, throw_false


def build_operation(operation_string):
    return eval('lambda old: ' + operation_string)


def main():
    file_lines = open('day11_input.txt', 'r').readlines()

    monkeys = []

    for i in range(0, len(file_lines), 7):
        items = [int(x.strip(',')) for x in file_lines[i + 1].strip().split()[2:]]  # lol
        operation = build_operation(file_lines[i + 2].strip().split(' ', 3)[3])  # lol again
        test = int(file_lines[i + 3].strip().split()[3])  # lol a third time
        if_true, if_false = int(file_lines[i + 4].strip().split()[5]), int(file_lines[i + 5].strip().split()[5])  # lol a fourth and fifth time
        monkeys.append(Monkey(items, operation, test, if_true, if_false))

    supermod = 1
    for monkey in monkeys:
        supermod *= monkey.test  # shoutout /u/silentwolf_01 on reddit

    for i in range(10000):
        for monkey in monkeys:
            throw_true, throw_false = monkey.process(supermod)

            # throw packages to monkeys based on this monkey's attributes
            monkeys[monkey.if_true].add_items(throw_true)
            monkeys[monkey.if_false].add_items(throw_false)

    list_nums_inspected = [x.num_inspected for x in monkeys]
    list_nums_inspected.sort(reverse=True)

    print(list_nums_inspected[0] * list_nums_inspected[1])


if __name__ == '__main__':
    main()
