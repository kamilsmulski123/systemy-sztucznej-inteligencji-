DATA_DIR = "../data"
INFO_FILENAME = "_info-data-discrete.txt"


def main():
    load_metadata()


def load_metadata():
    path = DATA_DIR + "/" + INFO_FILENAME
    with open(path) as file:
        lines = file.readlines()

    for line in lines:
        system = System(line.split()[0], line.split()[1], line.split()[2])
        system.load_data()
        print("--------------------------------------------")
        system.print_info()


class System:
    def __init__(self, name, nr_attr, nr_val):
        print(f"Creating system {name}!")
        self.name = name
        self.number_of_attributes = int(nr_attr)
        self.number_of_values = nr_val
        self.data = []
        self.columns = []
        for i in range(self.number_of_attributes):
            self.columns.append([])

    def print_info(self):
        pass

    def load_data(self):
        with open(DATA_DIR + "/" + self.name + ".txt") as file:
            for line in file:
                self.data.append(line.strip().split(" "))

        for i in range(len(self.data)):
            for j in range(len(self.data[i])):
                self.columns[j].append(self.data[i][j])


class DecisionClass:
    def __init__(self, name, type):
        self.name = name
        self.type = type
        self.values = []

    def load_values(self, data, i):
        pass


if __name__ == '__main__':
    main()
