# -*- coding: utf-8 -*-
"""
chemdataextractor.reader.elsevier.py
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Readers for documents from Elsevier.

:author Edward Beard (ejb207@cam.ac.uk)
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
import logging

from ..scrape.clean import clean
from .markup import HtmlReader
from ..doc.text import Caption
from ..doc.figure import Figure



log = logging.getLogger(__name__)


class ElsevierHtmlReader(HtmlReader):
    """Reader for HTML documents from Elsevier."""

    cleaners = [clean]

    root_css = 'body'
    table_css = 'dl[class~=table]'
    table_caption_css = 'dl[class~=table] div[class=caption]'
    table_head_row_css = 'table thead tr'
    table_body_row_css = 'table tbody tr'
    table_footnote_css = 'dl[class~=tblFootnote]'
    figure_css = 'dl[class~=figure]'
    figure_img_css = 'img[src]'
    figure_caption_css = ' .caption'

    def _parse_figure(self, el, refs, specials):
        caps = self._css(self.figure_caption_css, el)
        caption = self._parse_text(caps[0], refs=refs, specials=specials, element_cls=Caption)[0] if caps else Caption('')
        img = self._css(self.figure_img_css, el)
        img_url = img[0].attrib['src'] if img else ''
        if img_url is not None:
            img_id = img_url[-7:-4]
            img_url = img_url[:-4] + '_lrg' + img_url[-4:]
            print(id)
        fig = Figure(caption, url=img_url, id=img_id)
        return [fig]

    def detect(self, fstring, fname=None):
        """ Identifies Elsevier articles from string"""
        if fname and not (fname.endswith('.html') or fname.endswith('.htm')):
            return False
        if b'xmlns:bk="http://www.elsevier.com/xml/bk/dtd"' in fstring:
            return True
        return False
