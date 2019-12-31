import statistics

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
        system.print_info()


class System:
    def __init__(self, name, nr_attr, nr_val):
        self.name = name
        self.number_of_attributes = int(nr_attr)
        self.number_of_values = nr_val
        self.data = []
        self.columns = []
        for i in range(self.number_of_attributes):
            self.columns.append([])
        self.attributes = []

    def print_info(self):
        print("---------------------")
        print(f"Information about system {self.name}")
        print(f"System contains {len(self.attributes)} attributes.")
        print(f"System contains {len(self.columns[0])} objects.")
        for attribute in self.attributes:
            attribute.print_info()

    def load_data(self):
        with open(DATA_DIR + "/" + self.name + ".txt") as file:
            for line in file:
                self.data.append(line.strip().split(" "))

        for i in range(len(self.data)):
            for j in range(len(self.data[i])):
                self.columns[j].append(self.data[i][j])

        with open(DATA_DIR + "/" + self.name + "-type.txt") as file:
            i = 0
            for line in file:
                name, type_value = line.split()
                attribute = SystemAttribute(name, type_value)
                attribute.load_values(self.columns[i])
                self.attributes.append(attribute)
                i += 1


class SystemAttribute:
    def __init__(self, name, type):
        self.name = name
        self.type = type
        self.values = []

    def load_values(self, data):
        self.values = data
        try:
            if self.type == "n":
                self.values = [float(i) for i in data]
        except Exception as e:
            self.type = "s"
            print(f"Incorrect type set for attribute {self.name}. {str(e)} Using type 's.")


    def print_info(self):
        for line in self.get_info():
            print(line)

    def get_info(self):
        info_lines = []
        info_lines.append(f"----Information about attribute {self.name}")
        info_lines.append(f"    Type: {self.type}")
        if self.type == "n":
            info_lines.append(f"    Minimal value: {min(self.values)}")
            info_lines.append(f"    Maximal value: {max(self.values)}")
        info_lines.append(f"    Number of uniq values: {len(set(self.values))}")
        info_lines.append(f"    List of uniq values: {set(self.values)}")
        if self.type == "n":
            info_lines.append(f"    Standard deviation: {statistics.stdev(self.values)}")
        return info_lines

if __name__ == '__main__':
    main()
