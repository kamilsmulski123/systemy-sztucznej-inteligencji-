DATA_DIR = "../data"
INFO_FILENAME = "_info-data-discrete.txt"


def main():
    load_metadata()


def load_metadata():
    path = DATA_DIR + "/" + INFO_FILENAME
    with open(path) as file:
        lines = file.readlines()

    for line in lines:
        metadata = SystemMetadata(line.split()[0], line.split()[1], line.split()[2])
        metadata.print()


class SystemMetadata:
    def __init__(self, name, nr_attr, nr_val):
        self.name = name
        self.number_of_attributes = nr_attr
        self.number_of_values = nr_val

    def print(self):
        print(self.name, self.number_of_attributes, self.number_of_values)


if __name__ == '__main__':
    main()
