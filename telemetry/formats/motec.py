__author__ = 'Shadow'
from ..core.telemetry import CoreTelemetry
from struct import *
import re
class Telemetry(CoreTelemetry):
    _properties = {
        'maxline': 1000000,
        'startitems': 0x78601,
        'ITEMCOUNT': 6,
        'MAXITEM': 18,
    }

    _offset = {
        'device_type': [74, 8],
        'date': [94, 32],
        'time': [126, 32],
        'driver': [158, 64],
        'vehicle_id': [222, 64],
        'engine_id': [286, 64],
        'venue': [350, 64],
        'short_comment': [1572, 64]
    }

    _data = {
        'device_type': '',
        'date': '',
        'time': '',
        'driver': '',
        'vehicle_id': '',
        'engine_id': '',
        'venue': '',
        'short_comment':  ''
    }

    def show(self):
        print('MOTEC format')

    def print_block(self, name):
        print(name+': '+self._data[name])

    def read_block(self, name):
        self._file.seek(self._offset[name][0])
        self._data[name] = self._file.read(self._offset[name][1]).decode(encoding='cp1251').strip(chr(00)+' ')

    def read_head(self):
        self.read_block('device_type')
        self.read_block('date')
        self.read_block('time')
        self.read_block('driver')
        self.read_block('vehicle_id')
        self.read_block('engine_id')
        self.read_block('venue')
        self.read_block('short_comment')
        # Debug
        self.print_block('device_type')
        self.print_block('date')
        self.print_block('time')
        self.print_block('driver')
        self.print_block('vehicle_id')
        self.print_block('engine_id')
        self.print_block('venue')
        self.print_block('short_comment')

    def check_file_format(self):
        return self._file.read(1) == b'@'

    #data = re.split(';', bt.decode(encoding='cp1251'))
    #print(data)
    #print('MOTEC format')

