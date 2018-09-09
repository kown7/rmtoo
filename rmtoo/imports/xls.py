'''Import xls spreadsheets again

Suits love Excel.

'''
import os
import codecs
import openpyxl
from collections import OrderedDict

from rmtoo.lib.logging import tracer
from rmtoo.imports.abc import AbcImports

class XlsImport(AbcImports):
    '''Import an xls-sheet created in the output plugins'''

    default_config = {'import_filename': None,
                      'requirement_ws': 'Requirements'}

    def __init__(self, self_cfg, import_dest):
        tracer.info("called")
        self._cfg = dict(self.default_config)
        self._cfg.update(self_cfg)
        assert os.path.isdir(import_dest['requirements_dirs'])
        self._dest = import_dest
        self._wb = None
        tracer.debug("Finished.")

    def run(self):
        filename = self._cfg['import_filename']
        if os.path.isfile(filename):
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
            filepath = os.path.join(self._dest['requirements_dirs'], entry['ID'])
            with codecs.open(filepath, "w", "utf-8") as fhdl:
                for key, value in entry.items():
                    fhdl.write(": ".join([key, str(value)]) + os.linesep)
