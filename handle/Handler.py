

from table.Report import Report
from table.Vmate import Vmate
from table.Vmlite import Vmlite


class Handler(object):

    def __init__(self, reports=[], vms=[]):
        self._reports = reports
        self._vms = vms

    def handle(self):
        for v in self._vms:
            tmp = v.generate_data()

    def _handle_fb(self):
        pass

    def _fb_keywords(self):
        pass

    def handle_company(self):
        pass

    def _company_keywords(self):
        pass