__author__ = 'Shadow'


class CoreTelemetry(object):
    def __init__(self, filepath):
        self._filepath = filepath
        self._file = open(self._filepath, "rb")

    def __exit__(self, type, value, traceback):
        self._file.close()

    def show(self):
        raise NotImplementedError()

    def read_head(self):
        raise NotImplementedError()