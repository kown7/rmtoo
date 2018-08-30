# (c) 2018 Kristoffer Nordstroem, see COPYING

import os
from datetime import datetime
import openpyxl
import pytest

from rmtoo.outputs.xls import XlsHandler as xh
from rmtoo.lib.Requirement import Requirement
from rmtoo.tests.lib.Utils import create_tmp_dir, delete_tmp_dir
from rmtoo.tests.lib.TestConfig import TestConfig

LDIR = os.path.dirname(os.path.abspath(__file__))


def create_req(req_id):
    req_txt_items = {}
    inv_date = datetime.strptime('1970-01-01', "%Y-%m-%d").date()
    req_values = {
        'Priority': 'development',
        'Owner': '007',
        'Invented on': inv_date.isoformat(),
        'Invented by': 'James',
        'Status': 'not done',
        'Class': 'requirement',
        'Description': "we test it's here"
    }
    for key, value in req_values.items():
        req_txt_items[key] = DummyTxtString(value)
    req_txt_items['Invented on'] = inv_date
    req = Requirement(u"", req_id, None, None, TestConfig())
    req.values.update(req_txt_items)
    return req


class DummyTxtString:
    def __init__(self, txt_str):
        self.txt_string = txt_str

    def get_content(self):
        return self.txt_string

    def get_output_string(self):
        return self.txt_string


class RMTTestOutputXls:
    "Test-Class for the xlsx output class"

    @classmethod
    def teardown_class(self):
        if self.__tmpdir:
            delete_tmp_dir(self.__tmpdir)

    @classmethod
    def setup_class(self):
        self.__tmpdir = create_tmp_dir()
        self.oconfig = xh.default_config
        self._filename = os.path.join(self.__tmpdir, "reqs.xlsx")
        self.oconfig["output_filename"] = self._filename

    def rmttest_adding_req_header(self):
        self.xlsh = xh(self._filename, self.oconfig)
        self.xlsh.write()

        twb = openpyxl.load_workbook(filename=self._filename)
        rws = twb['Requirements']

        i = 0
        for tval in xh.default_config['req_attributes']:
            i += 1
            assert rws.cell(row=1, column=i).value == tval
        assert i == 8
        assert rws['B1'].value == "Name"
        # TODO rm file

    def rmttest_extract_dict_from_file(self):
        self.xlsh = xh(self._filename, self.oconfig)
        req_file = os.path.join(LDIR, 'DocManPage.req')
        req = create_req(u'DocManPage')
        req._file_path = req_file

        req_dict = self.xlsh._req_extract_dict(req)
        assert req_dict['Name'] == "Documentation Man Page"
        self.xlsh._check_required_fields(req_dict)

        with pytest.raises(AssertionError):
            faulty_dict = req_dict
            del faulty_dict['Description']
            self.xlsh._check_required_fields(faulty_dict)

        self.xlsh._add_new_headers(req_dict)
        assert 'Rationale' in self.xlsh._headers

    def rmttest_extract_dict_from_inexisting_file(self):
        self.xlsh = xh(self._filename, self.oconfig)
        req_file = os.path.join(LDIR, 'DocManPage_gone.req')
        req = create_req(u'DocManPage_gone')
        req._file_path = req_file
        with pytest.raises(FileNotFoundError):
            self.xlsh._req_extract_dict(req)

    def rmttest_adding_req(self):
        self.xlsh = xh(self._filename, self.oconfig)
        req_file = os.path.join(LDIR, 'DocManPage.req')

        # The requirements are identical but in name
        req_101 = create_req(u'SW-101')
        req_102 = create_req(u'SW-102')
        req_101._file_path = req_file
        req_102._file_path = req_file

        self.xlsh.add_req(req_101)
        self.xlsh.add_req(req_102)
        self.xlsh.write()

        twb = openpyxl.load_workbook(filename=self._filename,
                                     guess_types=True)
        rws = twb['Requirements']
        assert rws['A2'].value == "SW-101"
        assert rws['F2'].value == "development"
        assert rws['H2'].value.date().isoformat() == "1970-01-01"

        assert rws['A3'].value == "SW-102"
