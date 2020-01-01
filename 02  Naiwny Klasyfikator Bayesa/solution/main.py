import statistics

DATA_DIR = "../data"
INFO_FILENAME = "_info-data-discrete.txt"


def main():
    system_tst = System("australian_TST")
    system_trn = System("australian_TRN")
    classifier = NaiveBayesClassifier(system_tst, system_trn)
    classifier.compute()


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


class NaiveBayesClassifier:
    def __init__(self, tst, trn):
        self.tst = tst
        self.trn = trn

    def compute(self):
        self.load_data()

    def load_data(self):
        self.tst.load_data()
        self.trn.load_data()


if __name__ == '__main__':
    main()
