# import requests
# from contextlib import closing

class ProgressBar(object):
    def __init__(self, title, count = 0.0, run_status = None, fin_status = None, total = 100.0, unit = '', sep = '/', chunk_size = 1.0):
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
        _info = self.info % (self.title, self.status, self.count/self.chunk_size, self.unit, self.seq, self.total/self.chunk_size, self.unit)
        return _info

    def refresh(self, count = 1, status = None):
        self.count = count
        self.status = status or self.status
        end_str = "\r"
        if self.count >= self.total:
            end_str = "\n"
            self.status = status or self.fin_status
        print(self.__get_info(), end = end_str, )

if __name__ == "__main__":
    # url = 'http://www.demongan.com/source/game/二十四点.zip'
    # filename = "二十四点.zip"
    print('*' * 100)
    print('\t\t\t\t欢迎使用文件下载小助手')
    print('作者：keyls')
    print('*' * 100)
    