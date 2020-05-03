import xlrd
import os


from table.Vmate import Vmate
from table.Vmlite import Vmlite
from table.Report import Report


def _read_xls_file(filePath):
    data = xlrd.open_workbook(filePath)
    tables = data.sheets()
    return tables


def _generate_vms(filePath):
    vms = []
    tables = _read_xls_file(filePath)
    for table in tables:
        headers = table.row_values(0)
        content = []
        for i in range(table.nrows):
            if i > 0:
                content.append(table.row_values(i))
        vms.append(_ensure_file_obj(filePath)(headers, table.name, content))
    return vms


def _ensure_file_obj(filePath):
    if os.path.dirname(filePath).endswith('vmlite'):
        return Vmlite
    elif os.path.dirname(filePath).endswith('vmate'):
        return Vmate
    elif os.path.dirname(filePath).endswith('report'):
        return Report
    else:
        print('not support file name')


def _generate_vm(path):
    vms = []
    files = os.listdir(path)
    for f in files:
        if f.endswith('.xls'):
            vms.extend(_generate_vms(os.path.join(path, f)))
    return vms


def _read_current_report(filepath):
    _read_xls_file(filepath)
    _generate_vms(filepath)

def generate_vmlite():
    return _generate_vm('data\\vmlite')


def generate_vmate():
    return _generate_vm('data\\vmate')


def _generate_report(path):
    files = os.listdir(path)
    f = files[0]
    return _generate_vms(os.path.join(path, f))

def genera_vmlite_report():
    return _generate_report('data\\vmlite\\currentreport')


if __name__ == "__main__":
    vms = generate_vmlite()
    # for vm in vms:
    #     print(vm.generate_data())
    reports = genera_vmlite_report()
    for report in reports:
        print(report.header)
    vms = generate_vmate()
