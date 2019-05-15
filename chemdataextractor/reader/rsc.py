# -*- coding: utf-8 -*-
"""
chemdataextractor.reader.rsc
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Readers for documents from the RSC.

:copyright: Copyright 2016 by Matt Swain.
:license: MIT, see LICENSE file for more details.
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
import logging

from ..doc.text import Footnote, Caption
from ..doc.figure import Figure
from ..doc.table import Table
from ..scrape.pub.rsc import replace_rsc_img_chars
from ..scrape.clean import clean
from .markup import HtmlReader


log = logging.getLogger(__name__)


class RscHtmlReader(HtmlReader):
    """Reader for HTML documents from the RSC."""

    cleaners = [clean, replace_rsc_img_chars]

    root_css = '#wrapper'
    title_css = 'h1, .title_heading'
    heading_css = 'h2, h3, h4, h5, h6, .a_heading, .b_heading, .c_heading, .c_heading_indent, .d_heading, .d_heading_indent'
    citation_css = 'span[id^="cit"]'
    table_css = 'table[class*="tgroup"]' #'div[class="rtable__wrapper"]'
    table_caption_css = '.table_caption'# span[id^="tab"]'
    table_head_row_css = 'thead tr'
    table_body_row_css = 'tbody tr'
    table_footnote_css = 'tfoot tr th .sup_inf'
    figure_css = '.image_table'
    figure_image_css = 'img[src]'
    figure_caption_css = '.graphic_title'
    figure_id_css = 'span[id]'
    ignore_css = '.table_caption + table, .left_head, sup span.sup_ref, small sup a, a[href^="#fn"], .PMedLink'

    def _parse_table_footnotes(self, fns, refs, specials):
        """Override to account for awkward RSC table footnotes."""
        footnotes = []
        for fn in fns:
            footnote = self._parse_text(fn, refs=refs, specials=specials, element_cls=Footnote)[0]
            footnote += Footnote('', id=fn.getprevious().get('id'))
            footnotes.append(footnote)
        return footnotes

    def _parse_figure(self, el, refs, specials):
        caps = self._css(self.figure_caption_css, el)
        caption = self._parse_text(caps[0], refs=refs, specials=specials, element_cls=Caption)[0] if caps else Caption('')
        img = self._css(self.figure_img_css, el)
        img_url = img[0].attrib['src'] if img else ''
        if 'http://pubs.rsc.org' not in img_url:
            img_url='http://pubs.rsc.org' + img_url
        id = self._css(self.figure_id_css, el)
        img_id = id[0].attrib['id'] if id else ''
        fig = Figure(caption, url=img_url, id=img_id)
        return [fig]

    def _find_table(self, root):
        tab_els = self._css(self.table_css, root)
        cap_els = self._css(self.table_caption_css, root)
        if len(tab_els) == len(cap_els):
            return list(zip(tab_els, cap_els))

    def _parse_table(self, el, refs, specials):

        if len(el) == 2:
            tab_el, cap_el = el[0], el[1]
            caption = self._parse_text(cap_el, refs=refs, specials=specials, element_cls=Caption)[0] if cap_el else Caption('')
        else:
            tab_el = el
            caption = Caption('')
        hrows = self._parse_table_rows(self._css(self.table_head_row_css, tab_el), refs=refs, specials=specials)
        rows = self._parse_table_rows(self._css(self.table_body_row_css, tab_el), refs=refs, specials=specials)
        footnotes = self._parse_table_footnotes(self._css(self.table_footnote_css, tab_el), refs=refs, specials=specials)
        tab = Table(caption, headings=hrows, rows=rows, footnotes=footnotes, id=tab_el.get('id', None))
        return [tab]

    def detect(self, fstring, fname=None):
        """"""
        if fname and not (fname.endswith('.html') or fname.endswith('.htm')):
            return False
        if b'meta name="citation_doi" content="10.1039' in fstring:
            return True
        return False
