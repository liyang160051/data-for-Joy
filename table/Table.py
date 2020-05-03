class Table(object):

    def __init__(self, header, sheetname, content=[]):
        self._header = header
        self._sheetname = sheetname
        self._content = content

    def generate_data(self):
        raise Exception("the method must be implemeted")


    @property
    def header(self):
        return self._header

    @property
    def content(self):
        return self._content

    @property
    def sheetname(self):
        return self._sheetname