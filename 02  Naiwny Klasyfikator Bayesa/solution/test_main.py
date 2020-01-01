from tempfile import NamedTemporaryFile

from main import System

tst_content = [
    (2, 4, 2, 1, 4),
    (1, 2, 1, 1, 2),
    (9, 7, 10, 7, 4),
    (4, 4, 10, 10, 2)
]

trn_content = [
    (1, 3, 1, 1, 2),
    (10, 3, 2, 1, 2),
    (2, 3, 1, 1, 2),
    (10, 9, 7, 1, 4),
    (3, 5, 2, 2, 4),
    (2, 3, 1, 1, 4),
]

tst_file = NamedTemporaryFile()
trn_file = NamedTemporaryFile()

with open(tst_file.name, "w") as file:
    file.writelines([
        "2 4 2 1 4 \n",
        "1 2 1 1 2 \n",
        "9 7 10 7 4 \n",
        "4 4 10 10 2 \n",
    ])

with open(trn_file.name, "w") as file:
    file.writelines([
        "1 3 1 1 2 \n",
        "10 3 2 1 2 \n",
        "2 3 1 1 2 \n",
        "10 9 7 1 4 \n",
        "3 5 2 2 4 \n",
        "2 3 1 1 4 \n",
    ])

tst = System("tst", tst_file.name)
trn = System("trn", trn_file.name)

tst.load_data()
trn.load_data()

print(tst.decision_classes)
print(trn.decision_classes)