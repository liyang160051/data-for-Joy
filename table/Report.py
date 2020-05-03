from table.Table import Table

class Report(Table):

    def __init__(self, header, sheetname, content=[]):
        super(Report, self).__init__(header, sheetname, content)