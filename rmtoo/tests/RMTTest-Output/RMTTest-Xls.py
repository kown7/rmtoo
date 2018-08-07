# (c) 2018 Kristoffer Nordstroem, see COPYING

import os

from rmtoo.outputs.xls import XlsHandler as xh
from rmtoo.tests.lib.Utils import create_tmp_dir, delete_tmp_dir

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
        self.xlsh = xh(self._filename, self.oconfig)

    def rmttest_adding_req(self):
        self.xlsh.write()
