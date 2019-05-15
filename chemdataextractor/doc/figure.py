# -*- coding: utf-8 -*-
"""
chemdataextractor.doc.figure
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Figure document elements.

"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
import logging

from .element import CaptionedElement


log = logging.getLogger(__name__)


class Figure(CaptionedElement):

    def __init__(self, caption, label=None, url=None, **kwargs):
        super(Figure, self).__init__(caption=caption, label=label, **kwargs)
        self.url = url if url is not None else ''

    @property
    def records(self):
        caption_records = self.caption.records
        # Filter contextual records, because they normally only apply to the data within the figure.
        caption_records = [c for c in caption_records if not c.is_contextual]
        return caption_records

    def _repr_html_(self):
        html_lines = ['<figure>', self.caption._repr_html_(), '</figure>']
        return '\n'.join(html_lines)

