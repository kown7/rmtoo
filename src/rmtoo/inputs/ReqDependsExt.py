"""`Depends ext` attribute/tag

rmtoo Free and Open Source Requirements Management Tool
(c) 2021 Kristoffer Nordström; for licensing details see COPYING
SPDX-License-Identifier: GPL-3.0-or-later

"""
from rmtoo.lib.ReqTagGeneric import ReqTagGeneric
from rmtoo.lib.InputModuleTypes import InputModuleTypes


class ReqDependsExt(ReqTagGeneric):
    """`Depends ext` attribute

    This is a free-text input. It is not constrained like `Solved
    by`. There's no way to verify links to other documents. A
    different tool is required to inline, i.e. convert this to a
    `Solved by` tag (`InputModuleTypes.reqdeps`).

    """

    def __init__(self, config):
        ReqTagGeneric.__init__(
            self, config, "Depends ext",
            set([InputModuleTypes.reqtag]))

    def rewrite(self, _, req):
        '''This attribute is optional.'''
        return self.handle_optional_tag(req)
