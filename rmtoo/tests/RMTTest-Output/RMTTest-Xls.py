# (c) 2018 Kristoffer Nordstroem, see COPYING

import os
import openpyxl

from rmtoo.outputs.xls import XlsHandler as xh
from rmtoo.lib.Requirement import Requirement
from rmtoo.tests.lib.Utils import create_tmp_dir, delete_tmp_dir
from rmtoo.tests.lib.TestConfig import TestConfig

class DummyTxtString:
    def __init__(self, s):
        self.txt_string = s

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

        twb = openpyxl.load_workbook(filename = self._filename)
        rws = twb['Requirements']

        i = 0
        for tval in xh.default_config['req_attributes']:
            i += 1
            assert rws.cell(row=1, column=i).value == tval
        assert i == 7 # size of def config
        assert rws['A1'].value == "Id"
        # TODO rm file

    def rmttest_adding_req(self):
        def create_req(req_id):
            req_txt_items = {}
            req_values = {
                'Priority': 'development',
                'Owner': '007',
                'Invented on': '1970-01-01',
                'Invented by': 'James',
                'Status': 'not done',
                'Class': 'requirement'
            }
            req_json = "\n".join([key + ": " +value for key,value in
                                  req_values.items()])
            for key, value in req_values.items():
                req_txt_items[key] = DummyTxtString(value)
            req = Requirement(req_json, req_id, None, None, TestConfig())
            req.values = req_txt_items
            return req
        self.xlsh = xh(self._filename, self.oconfig)
        self.xlsh.add_req(create_req('SW-101'))
        self.xlsh.add_req(create_req('SW-102'))
        self.xlsh.write()

        twb = openpyxl.load_workbook(filename = self._filename,
                                     guess_types = True)
        rws = twb['Requirements']
        assert rws['A2'].value == "SW-101"
        assert rws['B2'].value == "development"
        assert rws['D2'].value.date().isoformat() == "1970-01-01"

        assert rws['A3'].value == "SW-102"
