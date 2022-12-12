import os
import glob
import datetime

class AcknowledgedFile:
    def __init__(self, fpath, scheme=None, gen=None):
        if not os.path.isfile(fpath):
            raise ValueError(f"Trying to describe non existing file at {fpath}")
        self.reg_dt = datetime.now()
        self.rel_path = fpath
        self.scheme = scheme
        self.generator = gen
        self.calc_md5()

    def __repr__(self):
        return f"File Details {self.rel_path}, Registred at: {self.reg_dt.strftime('%d.%m.%y %X')}\n md5: {self.md5}"

    def set_mask(self, mask:str):
        self.mask = mask

    def calc_md5(self):
        self.md5 = hashlib.md5(open(self.rel_path, 'rb').read()).hexdigest()

    def calc_crc(self):
        self.sha256 = hashlib.sha256(open(self.rel_path, 'rb').read()).hexdigest()

    @staticmethod
    def calc_md5_of(fpath):
        if not os.path.isfile(fpath):
            raise ExpectedFileException("Expected file at {fpath}")
        return hashlib.md5(open(fpath, 'rb').read()).hexdigest()

class Directory_watcher:
    """Следитель за состояниям файлов на коленке.
    Класс, котороый передается какому-то шеделеру (скрипт в кроне, либо если кровавый прод RabbitMQ.
    Шедулер дергает ран по расписанию.)"""

    def __init__(self, path_2_watch, config=None, action_to_perform=None):
        """
        :param path_2_watch: directory that should be wathced for changes
        :param action_to_perform:  function to be called on all new files
        """
        if not os.path.isdir(abs_path):
            raise ExpectedFileException(f"Expected dir at {abspath}. Aborting creation")

        self.acknowledged_files_index = {} #only names:hashes, should be resorted from time to time.
        self.acknowledged_files =[] #file details as instances of AcknowledgedFile
        self.fn_2_call = action_to_perform
        self.cfg = config
        self.abs_path = os.path.realpath(path_2_watch)

    def watch(self):
        for file in glob.glob(self.abs_path+'**'):
            if file in self.acknowledged_files_index.keys():
                md5 = AcknowledgedFile.calc_md5_of(file)
                if md5 == self.acknowledged_files_index.get(file):
                    continue
                else:
                    self.update(file)
            else:
                self.add(file)

    def add(self, file_p):
        gen = None
        if self.fn_2_call:
            try:
                gen = self.fn_2_call(file_p)
            except CustomException as ex:
                raise CustomException(f"Function {fn_2_call} failed on {file_p}.\n Original ex: {str(ex)}", ex)

        akn_f = AcknowledgedFile(cfg=self.cfg, fpath=file_p)
        self.acknowledged_files.append(akn_f)
        self.acknowledged_files_index.update({file_p:akn_f.md5})

    def remove(self, file_p):
        self.acknowledged_files_index.pop(file_p)
        for  idx, akn_f in enumerate(self.acknowledged_files):
            if akn_f.rel_path == file_p:
                removed = self.acknowledged_files.pop(idx)
                return removed
        print(f"{file_p} not found!")
        return None

    def update(self, file_p):
        self.remove(file_p)
        self.add(file_p)


class CustomException(Exception):
    pass

class ExpectedFileException(CustomException):
    pass

class FnException(CustomException):
    pass

