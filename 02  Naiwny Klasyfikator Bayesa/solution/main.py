from collections import defaultdict

DATA_DIR = "../data"
INFO_FILENAME = "_info-data-discrete.txt"


def main():
    system_tst = System("australian_TST", DATA_DIR + "/australian_TST.txt")
    system_trn = System("australian_TRN", DATA_DIR + "/australian_TRN.txt")
    classifier = NaiveBayesClassifier(system_tst, system_trn)
    classifier.compute()


class System:

    def __init__(self, name, path):
        self.name = name
        self.path = path
        self.objects = []
        self.decision_classes = defaultdict(list)

    def load_data(self):
        for line in open(self.path):
            system_object = SystemObject(line.strip())
            self.objects.append(system_object)
            self.decision_classes[system_object.decision].append(system_object)


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
