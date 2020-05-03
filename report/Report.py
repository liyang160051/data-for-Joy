class Report(object):

    def __init__(self, header, sheetname, content=[]):
        self._header = header
        self._sheetname = sheetname
        self._content = content