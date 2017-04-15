'''
 rmtoo
   Free and Open Source Requirements Management Tool

  Blackbox rmtoo test

 (c) 2010-2012,2017 by flonatel GmbH & Co. KG

 For licensing details see COPYING
'''

import os

from rmtoo.lib.RmtooMain import main
from rmtoo.tests.lib.BBHelper import prepare_result_is_dir, \
    cleanup_std_log, delete_result_is_dir, extract_container_files, \
    check_file_results

mdir = "tests/RMTTest_Blackbox/RMTTest_BB010"


class RMTTest_BB010:

    def rmttest_pos_001(self):
        "BB Basic with some requirements - used for the slides"

        def myexit(n):
            pass

        os.environ["basedir"] = mdir
        mout, merr = prepare_result_is_dir()
        main(["-j", "file://" + mdir + "/input/Config.json"],
             mout, merr, exitfun=myexit)
        extract_container_files(["reqspricing.ods", ])
        cleanup_std_log(mout, merr)
        check_file_results(mdir)
        delete_result_is_dir()
