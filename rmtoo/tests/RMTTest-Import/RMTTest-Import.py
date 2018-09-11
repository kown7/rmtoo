# (c) 2018 Kristoffer Nordstroem, see COPYING
import os
import pytest

from rmtoo.lib.Import import Import
from rmtoo.imports.xls import XlsImport
from rmtoo.tests.lib.Utils import create_tmp_dir, delete_tmp_dir
from rmtoo.lib.Encoding import Encoding

LDIR = Encoding.to_unicode(os.path.dirname(os.path.abspath(__file__)))


class RMTTestImport:
    '''Test-Class to import the modified artifacts again'''

    def_cfg_imp_dest = {'topics': {'ts_common': {
        'sources': [['dummydriver', {'requirements_dirs': LDIR}]]}}}

    def rmttest_invalid_config_parser(self):
        '''Just figure out where it blows up'''
        with pytest.raises(AssertionError):
            Import(None)

    def rmttest_config_parser_wo_cfg(self):
        '''Assert the default configuration is loaded, ignore the import
        destination directory configuration'''
        cfg = {'import': {}, "dummy": "the universe is mind-bogglingly big"}
        cfg.update(self.def_cfg_imp_dest)
        importer = Import(cfg)
        assert not importer._config
        assert not importer._import_obj

    def rmttest_config_parser_input_dir(self):
        importer = Import(self.def_cfg_imp_dest)
        assert importer._input_dir['requirements_dirs'] == LDIR
        assert importer._input_dir['topics_dirs'] is None

    def rmttest_config_parser(self):
        '''Assert the default configuration is loaded, ignore the import
        destination directory configuration'''
        cfg = {"import": {"xls": {
            'import_filename': "asdf.xls"}}}
        cfg.update(self.def_cfg_imp_dest)
        importer = Import(cfg)
        assert len(importer._import_obj) == 1
        assert isinstance(importer._import_obj[0], XlsImport)

    def rmttest_config_run_with_default_cfg(self):
        tmpdir = create_tmp_dir()

        cfg = {"import": {"xls": {
            'import_filename': os.path.join(LDIR, "test-reqs.xlsx")}}}
        cfg.update(self.def_cfg_imp_dest)
        cfg['topics']['ts_common']['sources'][
            0][1]['requirements_dirs'] = [Encoding.to_unicode(tmpdir)]
        importer = Import(cfg)
        importer.process_all()

        assert os.path.isfile(os.path.join(tmpdir, 'AutomaticGeneration.req'))
        assert os.path.isfile(os.path.join(tmpdir, 'Completed.req'))

        delete_tmp_dir(tmpdir)