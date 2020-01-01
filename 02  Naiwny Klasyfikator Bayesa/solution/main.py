from collections import defaultdict

DATA_DIR = "../data"
INFO_FILENAME = "_info-data-discrete.txt"


def main():
    system_tst = System("australian_TST", DATA_DIR + "/australian_TST.txt")
    system_trn = System("australian_TRN", DATA_DIR + "/australian_TRN.txt")
    classifier = NaiveBayesClassifier(system_tst, system_trn)
    classifier.compute()
    classifier.dump_classified_system(DATA_DIR + "/dec_bayes.txt")


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
        self.classification = None


class NaiveBayesClassifier:
    def __init__(self, tst, trn):
        self.tst = tst
        self.trn = trn

    def compute(self):
        self.load_data()
        for obj in self.tst.objects:
            self.classify(obj)

    def load_data(self):
        self.tst.load_data()
        self.trn.load_data()

    def classify(self, obj):
        coefficients = {}
        for decision_class in self.trn.decision_classes:
            count_same_value = 0.0
            count_all = 0.0
            for i, value in enumerate(obj.values):
                for trn_obj in self.trn.decision_classes[decision_class]:
                    if trn_obj.values[i] == value:
                        count_same_value += 1
                    count_all += 1
            coefficients[decision_class] = count_same_value / count_all
        obj.classification = max(coefficients, key=coefficients.get)  # todo implement randomness

    def dump_classified_system(self, path):
        content = ""
        for obj in self.tst.objects:
            line = " ".join([str(v) for v in obj.values])
            line += " " + str(obj.classification)
            line += "\n"
            content += line
        with open(path, "w") as file:
            file.write(content)


if __name__ == '__main__':
    main()
