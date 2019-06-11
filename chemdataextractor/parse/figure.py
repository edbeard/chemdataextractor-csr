# -*- coding: utf-8 -*-
"""
chemdataextractor.parse.figure
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Parser for identifying particular figure categories

:author: Ed Beard
:copyright: Copyright 2016 by Matt Swain.
:license: MIT, see LICENSE file for more details.
"""


from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
import logging

from .base import BaseParser
from .base import BaseParser
from .elements import W, I, R, Optional, SkipTo, First, Not, Start, Group
from .cem import label_name_cem
from .microscopy import tem_phrase, sem_phrase
from ..model import Compound, ChemSchematicDiagram
from .common import hyph
from ..utils import first


logging.basicConfig(level=logging.WARNING)
log = logging.getLogger(__name__)

disallowed = (W('ORTEP') | I('ellipsoid') | I('pymol') | I('crystal') | (I('space') + I('filling')) | tem_phrase | sem_phrase )('disallowed')

diag_phrase = ((I('molecular') | I('chemical') | I('electronic')) + R('^[sS]tructure(s)?$') + (I('of') | I('for')))('diag_phrase')


total = (Group(disallowed + SkipTo(diag_phrase) + diag_phrase | diag_phrase + SkipTo(disallowed) + disallowed))('total')

not_logic = Group((Not(disallowed) + diag_phrase) | diag_phrase + Not(disallowed))('total')


class ChemSchemDiagParser(BaseParser):
    """Parser for identifying schematic chemical diagrams

    """
    root = diag_phrase

    def interpret(self, result, start, end):
        c = Compound()

        # Extracts results that don't have a disallowed value in the scope of the current sentence
        if not first(result.xpath('./disallowed/text()')):
            c.figure.append(ChemSchematicDiagram(exists=True, disallowed=False))
        else:
            c.figure.append(ChemSchematicDiagram(exists=True, disallowed=True))
        yield c


class ChemSchemDiagDisallowedParser(BaseParser):
    """Parser for identifying false positives for schematic chemical diagrams

    """
    root = disallowed

    def interpret(self, result, start, end):
        c = Compound()
        c.figure.append(ChemSchematicDiagram(exists=True, disallowed=True))
        yield c


