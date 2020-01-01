import statistics

DATA_DIR = "../data"
INFO_FILENAME = "_info-data-discrete.txt"


def main():
    system_tst = System("australian_TST")
    system_trn = System("australian_TRN")
    system_tst.load_data()
    system_trn.load_data()


class System:

    def __init__(self, name):
        self.name = name
        self.objects = []

    def load_data(self):
        for line in open(DATA_DIR + "/" + self.name + ".txt"):
            self.objects.append(SystemObject(line.strip()))


class SystemObject:

    def __init__(self, text_line):
        text_values = text_line.split(" ")
        numbers = [float(v) for v in text_values]
        self.values = numbers[:-1]
        self.decision = numbers[-1]


if __name__ == '__main__':
    main()
