# -*- coding: utf-8 -*-
"""
chemdataextractor.parse.microscopy
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Parser for identifying different kinds of microscopy images

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
from .elements import W, I, R, Optional
from .common import hyph


logging.basicConfig(level=logging.WARNING)
log = logging.getLogger(__name__)

# Transmission Electron Microscopy (TEM)
tem = (Optional(I('Transmission')) + I('electron') + R('^micro(graph(s)?|scopy)$'))
tem_strict = (Optional(I('Transmission')) + I('electron') + R('^micro(graph(s)?)$'))
tem_acronym = W('TEM')
tem_phrase = (tem_strict | tem_acronym | tem)('tem')

# Scanning Electron Microscopy (SEM)
sem = (I('scanning') + I('electron') + R('^micro(graph(s)?|scopy)$'))
se = (I('secondary') + I('electron')) | W('SE')  # Sub-types of SEM imaging
bse = ((I('backscattered') | (I('back') + I('scattered'))) + I('electron')) | W('BSE')
sem_acronym = W('SEM')
sem_phrase = (sem | sem_acronym | se | bse)('sem')

# High angle annular dark field scanning transmission electron microscopy (HAADF STEM)
haadf_stem_acronym = W('HAADF') + Optional(hyph + W('STEM'))
haadf_stem_phrase = haadf_stem_acronym('haadf_stem')

# High Resolution Transmission Electron Microscopy (HRTEM)
hrtem = (I('high') + Optional(hyph) + I('resolution') | W('HR')) + tem_phrase
hrtem_acronym = W('HRTEM')
hrtem_phrase = (hrtem | hrtem_acronym)('hrtem')

# Crogenic Electron Microscopy (CryoEM)
cryoem = I('cryogenic') + (I('electron') + I('microscopy') | tem_phrase | sem_phrase)
cryoem_acronym = R('^Cryo[\-‐‑⁃‒–—―−－⁻]?[ST]?EM$') | I('Cryo') + Optional(hyph) + (R('^[ST]?EM$') | W('ET'))
cryoem_phrase = (cryoem | cryoem_acronym)('cryoem')


class TemParser(BaseParser):
    """Parser for Transmission Electron Microscopy (TEM) instances

    Usage::
        tt = Sentence(input).tagged_tokens
        TemParser.parse(tt)

    .. note::
        Usually called as part of a list of parsers in doc.text.py objects

    """
    root = tem_phrase

    def interpret(self, result, start, end):
        m = 'tem'
        c = Compound()
        c.microscopy.append(m)
        yield c


class SemParser(BaseParser):
    """Parser for Scanning Electron Microscopy (SEM) instances

    Usage::
        tt = Sentence(input).tagged_tokens
        SemParser.parse(tt)

    .. note::
        Usually called as part of a list of parsers in doc.text.py objects
    """
    root = sem_phrase

    def interpret(self, result, start, end):
        m = 'sem'
        c = Compound()
        c.microscopy.append(m)
        yield c


class HaadfStemParser(BaseParser):
    """Parser for High angle annular dark field scanning transmission electron microscopy (HAADF STEM) instances

    Usage::
        tt = Sentence(input).tagged_tokens
        HaadfStemParser.parse(tt)

    .. note::
        Usually called as part of a list of parsers in doc.text.py objects
    """

    root = haadf_stem_phrase

    def interpret(self, result, start, end):
        m = 'haadf_stem'
        c = Compound()
        c.microscopy.append(m)
        yield c

class HrtemParser(BaseParser):
    """Parser for High Resolution Transmission Electron Microscopy (HRTEM) instances

    Usage::
        tt = Sentence(input).tagged_tokens
        HrtemParser.parse(tt)

    .. note::
        Usually called as part of a list of parsers in doc.text.py objects
    """
    root = hrtem_phrase

    def interpret(self, result, start, end):
        m = 'hrtem'
        c = Compound()
        c.microscopy.append(m)
        yield c


class CryoemParser(BaseParser):
    """Parser for Crogenic Electron Microscopy (CryoEM) instances

    Usage::
        tt = Sentence(input).tagged_tokens
        CryoemParser.parse(tt)

    .. note::
        Usually called as part of a list of parsers in doc.text.py objects
    """
    root = cryoem_phrase

    def interpret(self, result, start, end):
        m = 'cryoem'
        c = Compound()
        c.microscopy.append(m)
        yield c


