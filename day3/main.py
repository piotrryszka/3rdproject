
import csv
import json
import random


def f_read(t_dict):

    with open("TabelaPilkarska.csv", encoding="utf-8") as file:
        t_csv = csv.DictReader(file)
        for r in t_csv:
            t_dict.append(r)
    return t_dict


def f_write(t_dict):
    with open("TabelaPilkarskaUpdated.json", "w", encoding="utf-8") as file2:
        file2.write(json.dumps(t_dict, indent=4))


if __name__ == "__main__":

    slownik = []

    slownik = f_read(slownik)

    print(slownik)

    for i in slownik:
        try:
            j = int(i["Pkt"])
            j += random.randint(0,3)
            i["Pkt"] = str(j)
        except ValueError:
            print(f"W polu [Pkt] dla [MiejscewTabeli] {i} znajduję się blędna wartość! która nie jest liczbą, dlatego tabela nie może być posortowana wg aktualnej pkt")


    f_write(slownik)
