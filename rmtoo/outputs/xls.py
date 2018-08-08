'''
 rmtoo
   Free and Open Source Requirements Management Tool

 Output the content to a XLS sheet. Suits love Excel.

 (c) 2018 Kristoffer Nordstrom

 For licensing details see COPYING
'''
from __future__ import unicode_literals

import io
from datetime import date, datetime
import openpyxl
from six import iteritems

from rmtoo.lib.Constraints import Constraints
from rmtoo.lib.TestCases import collect
from rmtoo.lib.StdOutputParams import StdOutputParams
from rmtoo.lib.ExecutorTopicContinuum import ExecutorTopicContinuum
from rmtoo.lib.logging import tracer
from rmtoo.lib.CreateMakeDependencies import CreateMakeDependencies

class XlsHandler():
    '''Act as an abstraction layer between rmtoo-objects and OpenPyxl
    related things

    The default configuration is intended for users to copy and
    adapt. The filename is handled in the Xls' parent class.

    '''
    default_config = {
        "output_filename": "artifacts/requirements.xlsx",
        "req_attributes": [
            "Id", "Priority", "Owner", "Invented on",
            "Invented by", "Status"],
        "req_sheet": "Requirements",
        "topic_sheet": "Topics"
    }

    def __init__(self, filename, config=None):
        tracer.info("Creating XLS workbook: "
                    + filename)
        self.__filename = filename
        self._cfg = self.default_config
        for key, value in config.items():
            self._cfg[key] = value

        self._wb = openpyxl.Workbook()
        self._ws_req = self._wb.active
        self._ws_req.title = self._cfg['req_sheet']
        self._ws_topics = self._wb.create_sheet(
            self._cfg['topic_sheet'])
        self._ws_cfg = self._wb.create_sheet("Configuration")

        self._add_req_header()

    def _add_req_header(self):
        self.req_row = 1
        col = 1
        self._req_headers = self._cfg['req_attributes']
        for val in self._req_headers:
            self._ws_req.cell(column=col, row=self.req_row, value=val)
            col += 1
        self.req_row += 1

    def write(self):
        self._wb.save(filename=self.__filename)

    def add_req(self, req):
        col = 1
        for key in self._req_headers:
            if key == "Id":
                value = Xls.strescape(req.get_id())
            elif key == "Status":
                value = req.get_status().get_output_string()
            elif key == "Invented on":
                value = req.get_value(key)
            elif key == "Class":
                raise NotImplementedError(
                    "The class has no information __str__ equivalent")
            else:
                try:
                    value = req.get_value(key).get_content()
                except AttributeError:
                    value = req.get_value(key)
            self._ws_req.cell(column=col, row=self.req_row, value=value)

            col += 1
        self.req_row += 1

    def add_topic(self, req):
            pass

class Xls(StdOutputParams, ExecutorTopicContinuum,
          CreateMakeDependencies):

    def __init__(self, oconfig):
        '''Create an openpyxl output object.'''
        tracer.info("Called.")
        StdOutputParams.__init__(self, oconfig)
        CreateMakeDependencies.__init__(self)
        self.__ce3set = None
        self.__fd = None
        self._opiface = XlsHandler(self._output_filename, self._config)

    @staticmethod
    def strescape(string):
        '''Escapes a string: hexifies it.'''
        result = ""
        for fchar in string:
            if ord(fchar) >= 32 and ord(fchar) < 127:
                result += fchar
            else:
                result += "%02x" % ord(fchar)
        return result

    def topic_set_pre(self, _topics_set):
        pass

    def topic_set_post(self, topic_set):
        '''Clean up file.'''
        tracer.debug("Clean up file.")
        self._opiface.write()
        tracer.debug("Finished.")

    def topic_pre(self, topic):
        '''Output one topic.'''
        print(u"%% Output topic '%s'\n" % topic.name)

    def topic_post(self, _topic):
        '''Cleanup things for topic.'''
        pass

    def topic_name(self, name):
        pass

    def topic_text(self, text):
        pass

    def requirement_set_pre(self, rset):
        '''Prepare the requirements set output.'''
        self.__ce3set = rset.get_ce3set()
        self.__testcases = rset.get_testcases()

    def requirement_set_sort(self, list_to_sort):
        '''Sort by id.'''
        return sorted(list_to_sort, key=lambda r: r.get_id())

    def requirement(self, req):
        self._opiface.add_req(req)

    def cmad_topic_continuum_pre(self, _):
        pass
