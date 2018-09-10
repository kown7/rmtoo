'''Import xls spreadsheets again

Suits love Excel.

'''
from __future__ import unicode_literals
import os
import codecs
import openpyxl
from collections import OrderedDict

from rmtoo.lib.logging import tracer
from rmtoo.lib.RMTException import RMTException
from rmtoo.lib.configuration.Cfg import Cfg
from rmtoo.imports.abcimports import AbcImports


class XlsImport(AbcImports):
    '''Import an xls-sheet created in the output plugins'''

    default_config = {'import_filename': None,
                      'requirement_ws': 'Requirements'}

    def __init__(self, self_cfg, import_dest):
        tracer.info("called")
        self.useable = False
        self._cfg = dict(self.default_config)
        self._cfg.update(self_cfg)

        import_dest_cfg = Cfg(import_dest)
        try:
            req_dirs = import_dest_cfg.get_rvalue(u'requirements_dirs')
            if req_dirs[0] and os.path.isdir(req_dirs[0]):
                self.useable = True
                self._dest = import_dest
        except RMTException:
            self.useable = False
        self._wb = None
        tracer.debug("Finished.")

    def run(self):
        if self.useable:
            filename = self._cfg['import_filename']
            if filename and os.path.isfile(filename):
                self.import_file(filename)

    def import_file(self, filename):
        self._wb = openpyxl.load_workbook(filename)
        headers, entries = self._extract_dict()
        self._write_to_files(entries)

    def _extract_dict(self):
        headers = None
        entries = []
        wb = self._wb[self._cfg['requirement_ws']]
        for row in wb:
            if row[0].value == "ID":
                headers = [cell.value for cell in row]
            elif headers and row[0].value:
                req = OrderedDict([(headers[i], cell.value)
                                   for i, cell in enumerate(row)])
                entries.append(req)
        return headers, entries

    def _write_to_files(self, entries):
        for entry in entries:
            filepath = os.path.join(self._dest['requirements_dirs'],
                                    entry['ID'])
            with codecs.open(filepath, "w", "utf-8") as fhdl:
                for key, value in entry.items():
                    if key == 'ID':
                        pass
                    else:
                        content = "\n  ".join(str(value).splitlines())
                        fhdl.write(": ".join([key, content]) + os.linesep)
