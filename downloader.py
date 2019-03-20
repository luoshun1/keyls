# import requests
# from contextlib import closing

class ProgressBar(object):
    def __init__(self, title, count = 0.0, run_status = None,
                    fin_status = None, total = 100.0,
                    unit = '', sep = '/', chunk_size = 1.0):
        self.info = "[%s] %s %.2f %s %s %.2f %s"
        self.title = title
        self.total = total
        self.count = count
        self.chunk_size = chunk_size
        self.status = run_status or ""
        self.fin_status = fin_status or " " * len(self.status)
        self.unit = unit
        self.seq = sep

    def __get_info(self):
        _info = self.info % (self.title, self.status, self.count/self.chunk_size, self)
