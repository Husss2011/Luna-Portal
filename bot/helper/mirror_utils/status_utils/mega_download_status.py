#!/usr/bin/env python3
from mega import MegaApi

from bot.helper.ext_utils.bot_utils import (MirrorStatus,
                                            get_readable_file_size,
                                            get_readable_time)

engine_ = f"MegaSDK"

class MegaDownloadStatus:

    def __init__(self, obj, listener):
        self.__listener = listener
        self.__obj = obj
        self.message = self.__listener.message
        self.startTime = self.__listener.extra_details['startTime']
        self.mode = self.__listener.extra_details['mode']
        self.source = self.__listener.extra_details['source']
        self.engine = engine_

    def name(self):
        return self.__obj.name

    def progress_raw(self):
        try:
            return round(self.__obj.downloaded_bytes / self.__obj.size * 100, 2)
        except:
            return 0.0

    def progress(self):
        return f"{self.progress_raw()}%"

    def status(self):
        return MirrorStatus.STATUS_DOWNLOADING

    def processed_bytes(self):
        return get_readable_file_size(self.__obj.downloaded_bytes)

    def eta(self):
        try:
            seconds = (self.__obj.size - self.__obj.downloaded_bytes) / self.__obj.speed
            return f'{get_readable_time(seconds)}'
        except ZeroDivisionError:
            return '-'

    def size(self):
        return get_readable_file_size(self.__obj.size)

    def speed(self):
        return f'{get_readable_file_size(self.__obj.speed)}/s'

    def gid(self):
        return self.__obj.gid

    def download(self):
        return self.__obj
