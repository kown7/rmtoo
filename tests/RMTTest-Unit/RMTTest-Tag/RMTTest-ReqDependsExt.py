"""rmtoo
Free and Open Source Requirements Management Tool

Unit test for DependsExt

(c) 2021 Kristoffer Nordström; for licensing details see COPYING
SPDX-License-Identifier: GPL-3.0-or-later

"""
from ReqTag import create_parameters
import rmtoo.inputs.ReqDependsExt


class RMTTestReqDependsExt(object):

    def rmttest_positive_01(self):
        "Requirement Tag DependsExt - no tag given"
        config, req = create_parameters()

        rt = rmtoo.inputs.ReqDependsExt.ReqDependsExt(config)
        name, value = rt.rewrite("", req)
        assert name == "Depends ext"
        assert value is None

    def rmttest_positive_02(self):
        "Requirement Tag DependsExt - One thing set"
        config, req = create_parameters()
        req = {"Depends ext": "SYS-REQ-001-deadbeef"}

        rt = rmtoo.inputs.ReqDependsExt.ReqDependsExt(config)
        name, value = rt.rewrite(None, req)
        assert "Depends ext" == name
        assert "SYS-REQ-001-deadbeef" == value
