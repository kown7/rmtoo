# (c) 2018 Kristoffer Nordstroem, see COPYING

from rmtoo.outputs.xls import XlsHandler as xh

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
        filename = os.path.join(self.__tmpdir, "reqs.xlsx")
        self.oconfig["output_filename"] = filename
        self.xlsh = XlsHandler(filename, self,oconfig)

    def rmttest_positive_01(self):
        pass
