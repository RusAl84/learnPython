import datetime
import io
import os
import random
import shutil
import glob
import hashlib
from collections.abc import Callable
import re
import string
import zlib
import gzip
import binascii
import pickle
import json


COPY_PATH = "./DevOps/output/f1.txt"
DEF_ENC = "utf-8"
fpath = "./DevOps/input/f1.txt"


def contextless_open(fpath=fpath):
    fh = open(fpath, "r")
    data = fh.read()
    print(data[:100])
    fh.close()
    fh = open(fpath, "rt", encoding="utf-8")
    data = fh.read()
    print(data[:100])
    fh.close


def bytes2human(n: int, format="%(value).1f%(symbol)s") -> str:
    """int N Bytes -> str Unix Style Size
    bytes2human(100001221) -> '95.4M'
    """
    symbols = ("B", "K", "M", "G", "T", "P", "E", "Z", "Y")
    prefix = {}
    for i, s in enumerate(symbols[1:]):
        prefix[s] = 1 << (i + 1) * 10
    for symbol in reversed(symbols[1:]):
        if n >= prefix[symbol]:
            value = float(n) / prefix[symbol]
            return format % locals()
    return format % dict(symbol=symbols[0], value=n)


def with_open(fpath):
    with open(fpath, "rt", encoding="utf-8") as fh:
        for idx, line in enumerate(fh.readlines()):
            if idx > 2:
                break
            line_ending_less = line.strip("\n")
            print(f"{idx+1}:\t{line_ending_less}")
    print(
        "Вне блока file handler уже отдан GC, и следить за его закрытием и удалением не надо."
    )


def os_path_methods(fpath=fpath):
    print(
        f"File directory: {os.path.dirname(fpath)}\tFilename: {os.path.basename(fpath)}"
    )
    print(f"Absolute path: {os.path.realpath(fpath)}")
    print(f"Exists and file: {os.path.isfile(fpath)}")
    print(f"Definetly not exist: './sfsdfas.txt' {os.path.isfile('./sfsdfas.txt')}")
    print(f"Creation timestamp (secs from epoch): {os.path.getctime(fpath)}")
    size_in_B = os.path.getsize(fpath)
    print(f"Size in bytes: {size_in_B} B; -h size: {bytes2human(size_in_B)}")


def simple_text_file_operations(fpath=fpath):
    shutil.copyfile(fpath, COPY_PATH)
    with open(COPY_PATH, "wt", encoding="utf-8") as fh:
        fh.write("Wt флаг затирает содержимое файла.")
        fh.write(
            f"{os.linesep}write пишет в конец файла. Без перевода строки.{os.linesep}"
        )
        fh.writelines(
            [
                l + os.linesep
                for l in [
                    "Надо добавить разделитель строки",
                    "Для каждого элемента списка",
                ]
            ]
        )
        print(
            "Print'ом тоже можно писать в экземляры file, т.к. они resolve`нуться в io.TextWrapper",
            file=fh,
        )


def list_dir(fpath="./Devops/"):
    if not os.path.isdir(fpath):
        raise ValueError(f"Expected valid directory path. Got {fpath}")
    listed_files = []
    print(f"Listing {os.path.realpath(fpath)}...")
    # начните с простого листинга
    # потом докручивайте по одному до ls -alt
    # как права под виндой сделать я не знаю
    for fname in os.listdir(fpath):
        fullpath = os.path.realpath(fpath + os.sep + fname)
        size = os.path.getsize(fullpath)
        ctime = os.path.getctime(fullpath)
        dt = datetime.datetime.fromtimestamp(ctime)
        is_dir = "Dir" if os.path.isdir(fpath) else "File"
        print(f"{fname:12}\t{dt.strftime('%x %X')}\t{size}\t{is_dir}")


def globing(fpath=""):
    for fp in glob.glob(fpath, recursive=True):
        print(os.path.realpath(fp))


def small_files_routine(
    fpath="./devops/input/log.log",
    fn_for_line=print,
    enc="utf-8",
    trim=True,
    **kwargs,
):
    """
    :param fpath: str pathlike Путь до файла.
    :param fn_for_line: runnable  Ф-я применяемая к каждой строке, результат кладем в лист и возвращаем.
    :param enc: str кодировка
    :param trim: bool Срезать ли line break`и до передачу в ф-ю
    :return: list of results
    """
    res = []
    # io open, позволяет на ходу менять кодировки, и заменять/игнорировать ошибки,
    # если символ не удается декодировать.
    with io.open(fpath, encoding=enc, errors="replace") as fh:
        # пока размер в B, K, M  можно смело делать readlines...
        for line in fh.readlines():
            if trim:
                line = line.strip("\r\n")
            res_fn = fn_for_line(line, **kwargs)
            if res_fn:
                res.append(res_fn)
    return res


def file_handler_methods(fpath=fpath, cp_path=COPY_PATH):
    shutil.copyfile(fpath, cp_path)
    fh = open(cp_path, encoding="utf-8")
    print(f"Уставливает указатель на позицию: {fh.seek(0)}\n{fh.readline()}")
    print(f"Уставливает указатель на позицию: {fh.seek(222)}\n{fh.readline()}")
    print(f"Указатель переместился на {fh.tell()} позицию")
    fh.readline()
    print(f"Указатель переместился на {fh.tell()} позицию")
    print(
        f"Файловый дескриптор,инт.Если улетел во много, вы где-то не закрыли контекст/файл: {fh.fileno()}"
    )
    print(f"{fh.seekable()}")


######################################Archives#workflow#################################################################
def compresson101():
    data = "Hello. I am Dmitri Karamazov and the world is my father"
    lst = string.ascii_letters
    hard_to_compress = "".join(random.choice(lst) for _ in range(256))

    compressed_data = zlib.compress(data.encode(), 2)
    print(f"Original data: {data}")
    print(f"Compressed data: {binascii.hexlify(compressed_data)}")
    compressed_data = zlib.compress(hard_to_compress.encode(), 2)
    print(f"Random sequence: {hard_to_compress}")
    print(f"Compressed data: {binascii.hexlify(compressed_data)}")


def figure_out_compression_ratio(fpath=fpath, lvl=None):
    if not lvl:
        lvl = zlib.Z_BEST_COMPRESSION
    original_data = open(fpath, "rb").read()
    compressed_data = zlib.compress(original_data, lvl)

    compress_ratio = (float(len(original_data)) - float(len(compressed_data))) / float(
        len(original_data)
    )
    print("Compressed: %d%%" % (100.0 * compress_ratio))


def extract_2_file(src_path=fpath, target_path="./output"):
    if not os.path.isfile(src_path):
        raise FileNotFoundError(f"Expected archive file at {src_path}")
    if os.path.isdir(target_path):
        src_name = os.path.basename(src_path)
        if src_name.find(".gz") != -1:
            src_name = src_name[: src_name.find(".gz")]
        target_path = target_path + os.sep + src_name
    with gzip.open(src_path, "rb") as f_in:
        with open(target_path, "wb") as f_out:
            shutil.copyfileobj(f_in, f_out)


# what's inside...
def decompress_with_chunks(fpath, CHUNKSIZE=1024):
    data = zlib.decompressobj()
    my_file = open(fpath, "rb")
    buf = my_file.read(CHUNKSIZE)
    while buf:
        decompressed_data = data.decompress(buf)
        buf = my_file.read(CHUNKSIZE)

    decompressed_data += data.flush()
    return decompressed_data


#######################################Common formats#################################################################
class A:
    def __init__(self, l):
        self.l = l
        self.dt = datetime.datetime.now()

    def pop(self):
        return self.l.pop()


def pickle_exmaple():
    a = A([x for x in range(121, 191)])
    with open("./devops/output/a.pickle", "wb") as fhw:
        pickle.dump(a, fhw)
    with open("./devops/output/a.pickle", "rb") as fhr:
        b = pickle.load(fhr)
    for x in b.l:
        print(x)


def reverse_readline(path: str, buf_size=8192, split_char="\n", enc="utf-8"):
    """A generator that returns the lines of a file in reverse order"""
    ###Most of the time we work with insanly big files, seeking stuff from the end of the file
    if not os.path.isfile(path):
        raise ValueError(f"Expected file at {path}. Failed to fetch.")
    with open(path, encoding=enc) as fh:
        segment = None
        offset = 0
        fh.seek(0, os.SEEK_END)
        file_size = remaining_size = fh.tell()
        while remaining_size > 0:
            offset = min(file_size, offset + buf_size)
            fh.seek(file_size - offset)
            buffer = fh.read(min(remaining_size, buf_size))
            remaining_size -= buf_size
            lines = buffer.split(split_char)
            if segment is not None:
                # If the previous chunk starts right from the beginning of line
                # do not concat the segment to the last line of new chunk.
                # Instead, yield the segment first
                if buffer[-1] != split_char:
                    lines[-1] += segment
                else:
                    yield segment
            segment = lines[0]
            for index in range(len(lines) - 1, 0, -1):
                if lines[index]:
                    yield lines[index]
        if segment is not None:
            yield segment


########################################################################################################################
def unix_style_file_operations(path_glob: str, regExp_str: str, fn: Callable):
    res = []
    pattern = re.compile(regExp_str)
    for file in glob.glob(path_glob, recursive=True):
        if os.path.isfile(file):
            fname = os.path.realpath(file)
            with io.open(file, encoding="utf-8", errors="replace") as log_f_handle:
                try:
                    for line in log_f_handle.readlines():
                        for m in pattern.finditer(line):
                            d = m.groupdict()
                            if len(d.keys()) == 0:
                                continue
                            else:
                                print(f"Doing some buisness logic on {d}")
                            res.append(d)
                except UnicodeDecodeError as e:
                    print(f"Error with decoding {fname}")
                    print(str(e))
                    with open("./error.log", "at") as f_h:
                        f_h.writelines([fname, str(e), os.linesep])
    return res


def ex_pandas():
    import pandas as pd

    df = pd.read_excel("./devops/input/1.xlsx")
    l = df.values.tolist()

    print(df)
    # print(l[0][0])
    avr = 0
    for item in l:
        avr += int(item[1])
    avr /= len(l)
    avr = int(avr)
    print(avr)
    l.append(["Среднее значение", str(avr), ""])
    df = pd.DataFrame([l])
    df.columns = ["col1", "col2", "col3", "col4"]
    df.to_excel("./devops/input/2.xls")
    df.to_json("./devops/input/2.json")
    df.to_html("./devops/input/2.html")


###################################################JSON#################################################################
def json_101():
    data = [{"a": "A", "b": (2, 4), "c": 3.0}]
    print("DATA   :", data)

    data_string = json.dumps(data)
    print("ENCODED:", data_string)

    decoded = json.loads(data_string)
    print("DECODED:", decoded)

    print("ORIGINAL:", type(data[0]["b"]))
    print("DECODED :", type(decoded[0]["b"]))

    # тут выкосячивает лишний пробел, ибо не формат строка. мне уже лень чинить - устал.
    print("PRETTY_PRINT:\n", json.dumps(data[0], sort_keys=True, indent=2))


def json_and_dicts():
    data = [{"a": "A", "b": (2, 4), "c": 3.0, ("d",): "D tuple"}]

    print("First attempt")
    try:
        print(json.dumps(data))
    except TypeError as err:
        print("ERROR:", err)

    print()
    print("Second attempt")
    print(json.dumps(data, skipkeys=True))


class EncoderExample(json.JSONEncoder):
    def default(self, obj):
        print("default(", repr(obj), ")")
        # Convert objects to a dictionary of their representation
        d = {
            "__class__": obj.__class__.__name__,
            "__module__": obj.__module__,
        }
        d.update(obj.__dict__)
        return d


class ObjectToEncode:
    def __init__(self, argdata, *args, **kwargs):
        self.name = "Petr"
        self.surname = "Morozov"
        self.list_data = [x for x in range(1, 10)]
        self.dict_data = dict.fromkeys([x for x in range(1, 10)], 1)
        self.argdata = argdata
        self.process_kwargs(args)

    def __repr__(self):
        return (
            f" <ObjectToEncode> {self.surname=} {self.argdata=}\n"
            f"{self.dict_data=}\n{self.list_data=}"
        )

    def process_kwargs(self, *args, **kwargs):
        pass


def encode_custom_object(obj):
    encoder = EncoderExample()
    # default принтит, паралельно с енкодом
    print("Our obj __repr__")
    encoded_json = encoder.encode(obj)
    print("ENCODED:")
    restored = json.loads(encoded_json)
    print(json.dumps(restored, sort_keys=True, indent=2))
    print(f"TYPES: {type(obj)} {type(encoded_json)} {type(restored)}")
    # за декодеры объяснять не будем, потому что там таже проблема но в квадрате.
    # т.е. без рефлекта не объяснишь как он работает. Ну и понимать наследование надо.


if __name__ == "__main__":
    print("Files")
    # contextless_open()
    # os_path_methods(fpath=fpath)
    # with_open(fpath)
    # simple_text_file_operations()
    # list_dir()
    # globing("./devops/pr*")


    # small_files_routine()
    # С большими файлами так не прокатит:
    # res = small_files_routine()
    # print(res)

    # file_handler_methods()

    # sizes_l = [1024, 67_108_864, 10_069_547_520]
    # for size_in_B in sizes_l:
    #     print(f"Converting {size_in_B}B to human readable: {bytes2human(size_in_B)}")

    # In-to zlib
    # compresson101()
    # figure_out_compression_ratio()
    # figure_out_compression_ratio(fpath="./devops/input/log.log", lvl=None)
    # extract_2_file()

    # pickle_exmaple()

    # Работа с огромными файлами, чаще всего имеет смысл с конца. Заодно на генератор посмотрим:
    # Если вперед читать, идея таже токо там еще chunk_size вперед едет, и seek в конец нет.
    # Эквивалент tail -n 10
    # gen = reverse_readline(fpath)
    # for i in range(10):
    #     line = next(gen)
    #     print(f"{i}:\t{line}")
    # # # Добираем остаток
    # for line in gen:
    #     print(line)

    # bonus1 unix style glob + re = super grep
    # За регэкспы объяснять отдельно. И это одна из тех штук где бесполезно объяснять можно токо взять.
    unix_style_file_operations('./devops/*',r"^[ ]*(?P<import>(import |from ))(?P<package>[\w. ]*)", print)

    # ex_pandas()
