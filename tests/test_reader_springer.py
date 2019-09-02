# -*- coding: utf-8 -*-
"""
test_reader_springer
~~~~~~~~~~~~~~~

Test SpringerMaterials reader.

"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
import io
import logging
import os
import unittest

from chemdataextractor import Document
from chemdataextractor.reader import SpringerHtmlReader


logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger(__name__)


class TestRscHtmlReader(unittest.TestCase):

    maxDiff = None

    def test_detect(self):
        """Test RscHtmlReader can detect an RSC document."""
        r = SpringerHtmlReader()
        fname = '1752-153X-5-55.html'
        f = io.open(os.path.join(os.path.dirname(__file__), 'data', 'springer', fname), 'rb')
        content = f.read()
        self.assertEqual(r.detect(content, fname=fname), True)

    def test_reader_imgs(self):
        """ Test that springer figures are extracted"""

        r = SpringerHtmlReader()
        fname = '1752-153X-5-55.html'
        f = io.open(os.path.join(os.path.dirname(__file__), 'data', 'springer', fname), 'rb')
        content = f.read()
        d = r.readstring(content)
        figs = d.figures
        self.assertEqual(len(figs), 8)

    def test_document_usage(self):
        """Test RscHtmlReader used via Document.from_file."""
        fname = '1752-153X-5-55.html'
        f = io.open(os.path.join(os.path.dirname(__file__), 'data', 'springer', fname), 'rb')
        d = Document.from_file(f, readers=[SpringerHtmlReader()])
        self.assertEqual(len(d.elements), 97)

