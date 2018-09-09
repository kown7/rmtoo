# (c) 2018 Kristoffer Nordstroem, see COPYING
import os
import re
import pytest
try:
    from unittest.mock import Mock  # py33 ff.
except ImportError:
    from mock import Mock  # py27

from rmtoo.lib.Import import Import
from rmtoo.imports.xls import XlsImport
from rmtoo.tests.lib.Utils import create_tmp_dir, delete_tmp_dir

LDIR = os.path.dirname(os.path.abspath(__file__))


class RMTTestXlsImport:
    '''Test-Class to import the xls artifact'''

    config = {'import_filename': os.path.join(LDIR, 'test-reqs.xlsx'),
              'requirement_ws': 'Requirements'}

    def rmttest_invalid_config_parser(self):
        '''Just figure out where it blows up'''
        dest_dir = {'requirements_dirs': '/tmp/__nodir'}
        with pytest.raises(AssertionError):
            importer = XlsImport({}, dest_dir)

    def rmttest_config_run_with_default_cfg(self):
        tmpdir = create_tmp_dir()
        dest_dir = {'requirements_dirs': tmpdir}
        importer = XlsImport(self.config, dest_dir)
        importer.run()

        assert os.path.isfile(os.path.join(tmpdir, 'AutomaticGeneration'))
        completed_filename = os.path.join(tmpdir, 'Completed')
        assert os.path.isfile(completed_filename)

        id_occ = [re.findall(r'^ID:',line)
                  for line in open(completed_filename)]
        for i in id_occ:
            assert not i

        delete_tmp_dir(tmpdir)
