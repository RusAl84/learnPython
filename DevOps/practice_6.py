# Imports wich demonstrate how imports work
# import this
import os
# from os import path
# from os import path as pt
# from os import *

import random
# from config import Config
# from commonNS import CommonNS
import inspect
import string
import csv
import json
from urllib import request
from jinja2 import Template, Environment, FileSystemLoader

###############################################CSV101###################################################################
def test_csv():
    data = [
        (1, "A towel,", 1.0),
        (42, " it says, ", 2.0),
        (1337, "is about the most ", -1),
        (0, "massively useful thing ", 123),
        (-2, "an interstellar hitchhiker can have.", 3),
    ]

    # Write CSV file
    with open("test.csv", "wt") as fp:
        writer = csv.writer(fp, delimiter=",")
        # writer.writerow(["your", "header", "foo"])  # write header
        writer.writerows(data)

    # Read CSV file
    with open("test.csv") as fp:
        reader = csv.reader(fp, delimiter=",", quotechar='"')
        # next(reader, None)  # skip the headers
        data_read = [row for row in reader]
    print(data_read)


def minimal_csv_reader(fpath="./devops/input/color_web_safe.csv"):
    with open(fpath, "r") as file:
        # with open(fpath, "r") as fh:
        reader = csv.reader(file)
        for row in reader:
            print(row[0], " - ", row[1])


def random_char_seq(len):
    lst = string.ascii_letters
    return "".join(random.choice(lst) for _ in range(len))


def minimal_writer(
    fpath="./devops/input/color_web_safe.csv", amount=10, ch_len=16, verb=False
):
    with open(fpath, "wt") as wfh:
        writer = csv.writer(wfh)
        writer.writerow(("ID", "Random", "Date", "Unicode"))  # Just a tutple
        for idx in range(1, amount + 1):
            row = (
                idx,
                os.urandom(ch_len),
                "{:02d}.12.22".format(11 + idx),
                random_char_seq(ch_len),
            )
            writer.writerow(row)
    if verb:
        print(open(fpath, "rt").read())


def dialects_101():
    print(csv.list_dialects())
    csv.register_dialect(
        "escaped",
        escapechar="\\",
        doublequote=False,
        quoting=csv.QUOTE_NONE,
    )
    print(csv.list_dialects())


def dialect_next():
    csv.register_dialect(
        "singlequote",
        quotechar="'",
        quoting=csv.QUOTE_ALL,
    )
    TEMPLATE = """\
        Dialect: "{name}"

        delimiter   = {dl!r:<6}    skipinitialspace = {si!r}
        doublequote = {dq!r:<6}    quoting_modes_existed in python <= 3.6
        quotechar   = {qc!r:<6}    lineterminator   = {lt!r}
        escapechar  = {ec!r:<6}
    """
    for name in sorted(csv.list_dialects()):
        dialect = csv.get_dialect(name)

        print(
            TEMPLATE.format(
                name=name,
                dl=dialect.delimiter,
                si=dialect.skipinitialspace,
                dq=dialect.doublequote,
                qc=dialect.quotechar,
                lt=dialect.lineterminator,
                ec=dialect.escapechar,
            )
        )

        # такое себе, но если у writer`ов есть стдоут мод, будем его в этой лабе писать...
        writer = csv.writer(sys.stdout, dialect=dialect)
        writer.writerow(
            (
                "col1",
                1,
                "10/01/2010",
                "Special chars: \" ' {} to parse".format(dialect.delimiter),
            )
        )
        print()


def dict_style_csv(fpath="./devops/output/dict_wr_csv.csv"):
    fieldnames = ("Title 1", "Title 2", "Title 3", "Title 4")
    headers = {n: n for n in fieldnames}

    with open(fpath, "wt") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()

        for i in range(3):
            writer.writerow(
                {
                    "Title 1": i + 1,
                    "Title 2": chr(ord("a") + i),
                    "Title 3": "08/{:02d}/07".format(i + 1),
                    "Title 4": random_char_seq(5),
                }
            )

    print(open(fpath, "rt").read())


##############################Bonus CSV Trashy example csv->dict->jinja->HTML###########################################
def swatches_from_csv(fpath="./devops/input/color_web_safe.csv"):
    swatch_list = []

    with open(fpath, "rt") as fh:
        reader = csv.reader(fh)
        for idx, row in enumerate(reader):
            d = {}
            d["id"] = f"swatch{idx}"
            d.update({"hex": row[0], "rgb": row[1]})
            swatch_list.append(d)

    jinja_loader = FileSystemLoader("./input/templates/")
    env = Environment(loader=jinja_loader)
    template = env.get_template("swatches.html")
    output = template.render(swatchl=swatch_list)
    print(output)

    with open("./output/swatches.html", "wt") as wfh:
        wfh.write(output)


if __name__ == "__main__":
    # cfg = Config("00:00")
    # cfg.print_status_time()
    # print_secret_key()
    # print(f"Hello, from {__name__}!")

    # print(os.path.realpath('./'))
    # print(path.realpath('./'))
    # print(pt.realpath('/'))

    # Imports syspath hack #чтоб его показать надо pip uninstall сделать, потому что у вас пакет уже поставлен пипом.
    # sys.path.insert(1, os.path.join(sys.path[0], '..'))
    # import file_generator
    # print("modules")

    # cns =CommonNS()
    # # print(cns.current_fn_name())
    # # print(cns.current_caller_name())
    # d1= { 1:4444, 2:5555}
    # d2 = { 3:3333}
    # print(cns.merge_dicts(d1,d2))

    ##########################################  CSV  ###################################################################
    # test_csv()
    
    # minimal_csv_reader()
    # minimal_writer(verb=True)

    # dialects_101()
    # dialect_next()
    # dict_style_csv()
    # swatches_from_csv()
