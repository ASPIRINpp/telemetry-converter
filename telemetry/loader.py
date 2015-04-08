__author__ = 'Shadow'

from .formats import *
from . import errors


class Loader(object):
    def load_file(self, type_, filepath_):
        raise NotImplementedError()


class TelemetryLoader(Loader):
    def load_file(self, type_, filepath_):
        if type_ in globals():
            m = globals()[type_]
        else:
            raise errors.LoaderError('Undefined format')
        return m.Telemetry(filepath_)
