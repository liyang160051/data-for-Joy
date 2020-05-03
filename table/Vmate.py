from table.vm.Vm import Vm


class Vmate(Vm):

    def __index__(self, header, sheetname, content):
        super(Vmate, self).__init__(header, sheetname, content)

    def _key_words(self):
        return [u'展示次数', u'点击量（全部）', u'花费金额 (USD)', u'成效 [点击后 7 天]']