from table.Table import Table


class Vm(Table):

    def __init__(self, header, sheetname, content=[]):
        super(Vm, self).__init__(header, sheetname, content)

    def generate_data(self):
        result = {}
        for key in self._key_words():
            index = self.header.index(key)
            sum = 0
            for con in self.content:
                sum += con[index]
            result[key] = sum
        return result

    def fb_keywords(self):
        keywords = []
        pass

    def company_keywords(self):
        pass