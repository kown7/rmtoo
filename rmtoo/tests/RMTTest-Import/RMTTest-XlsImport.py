# (c) 2018 Kristoffer Nordstroem, see COPYING
from __future__ import unicode_literals
import os
import re
import codecs
import datetime

from rmtoo.lib.Requirement import Requirement
from rmtoo.imports.xls import XlsImport
from rmtoo.tests.lib.Utils import create_tmp_dir, delete_tmp_dir
from rmtoo.lib.Encoding import Encoding

LDIR = os.path.dirname(os.path.abspath(__file__))
LIPSUM = (
    "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod "
    "tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim "
    "veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea "
    "commodo consequat. Duis aute irure dolor in reprehenderit in voluptate "
    "velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint "
    "occaecat cupidatat non proident, sunt in culpa qui officia deserunt "
    "mollit anim id est laborum.")


class RMTTestXlsImport:
    '''Test-Class to import the xls artifact'''

    config = {u'import_filename': os.path.join(LDIR, 'test-reqs.xlsx'),
              u'requirement_ws': u'Requirements'}

    def rmttest_invalid_config_parser(self):
        '''Just figure out where it blows up'''
        dest_dir = {u'requirements_dirs': ['/tmp/__nodir']}
        importer = XlsImport({}, dest_dir)
        assert not importer.useable

    def rmttest_config_run_with_default_cfg(self):
        tmpdir = create_tmp_dir()
        dest_dir = {u'requirements_dirs': [Encoding.to_unicode(tmpdir)]}
        importer = XlsImport(self.config, dest_dir)
        assert importer.useable
        importer.run()

        assert os.path.isfile(os.path.join(tmpdir, 'AutomaticGeneration.req'))
        completed_filename = os.path.join(tmpdir, 'Completed.req')
        assert os.path.isfile(completed_filename)

        id_occ = [re.findall(r'^ID:', line)
                  for line in open(completed_filename)]
        for i in id_occ:
            assert not i

        delete_tmp_dir(tmpdir)

    def rmttest_treat_newlines_correctly(self):
        tmpdir = create_tmp_dir()
        dest_dir = {u'requirements_dirs': [Encoding.to_unicode(tmpdir)]}
        importer = XlsImport(self.config, dest_dir)
        importer.run()

        newlines_filename = os.path.join(tmpdir, 'TestNewlines.req')
        assert os.path.isfile(newlines_filename)
        with codecs.open(newlines_filename, encoding='utf-8') as nl_fh:
            req_content = nl_fh.read()
        nl_req = Requirement(req_content, 'TestNewlines.req',
                             newlines_filename, None, None)

        # Test Description
        parsed_desc = "\n".join(nl_req.record[2].
                                get_content_trimmed_with_nl())
        assert parsed_desc == LIPSUM + "\n\nASDF"

        parsed_note = "\n".join(nl_req.record[10].
                                get_content_trimmed_with_nl())
        assert parsed_note == "Lipsum\n\nHandle it well"

        parsed_invon = "\n".join(nl_req.record[7].
                                get_content_trimmed_with_nl())
        assert parsed_invon == "2010-03-06"

        delete_tmp_dir(tmpdir)
