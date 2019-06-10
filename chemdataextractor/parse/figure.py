# -*- coding: utf-8 -*-
"""
chemdataextractor.parse.figure
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Parser for identifying figures from captions

:author: Ed Beard
:copyright: Copyright 2016 by Matt Swain.
:license: MIT, see LICENSE file for more details.
"""


from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
import logging

from ..model import Compound
from .base import BaseParser
from .elements import W, I, R, Optional, SkipTo


logging.basicConfig(level=logging.WARNING)
log = logging.getLogger(__name__)

diag_phrase = (Optional(I('molecular') | I('chemical') | I('electronic')) + R('^[sS]tructure(s)?$') + (I('of') | I('for'))) #+ label_name_cem)


class ChemSchemDiagParser(BaseParser):
    """Parser for schematic chemical diagrams

    Usage::
        tt = Sentence(input).tagged_tokens
        TemParser.parse(tt)

    .. note::
        Usually called as part of a list of parsers in doc.text.py objects

    """
    root = diag_phrase

    def interpret(self, result, start, end):
        m = 'csd'
        c = Compound()
        c.figure.append(m)
        yield c