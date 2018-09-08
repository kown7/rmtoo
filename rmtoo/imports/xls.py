'''Import xls spreadsheets again

Suits love Excel.

'''
from rmtoo.lib.logging import tracer
from rmtoo.imports.abc import AbcImports

class XlsImport(AbcImports):
    def __init__(self, self_cfg):
        tracer.info("called")
        tracer.debug("Finished.")

    def run(self):
        import ipdb; ipdb.set_trace()
        pass
