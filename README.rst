ChemDataExtractor-CSR
=====================


.. image:: http://img.shields.io/pypi/l/ChemDataExtractor.svg?style=flat-square
    :target: https://github.com/edbeard/chemdataextractor-csr/blob/master/LICENSE


ChemDataExtractor-CSR is an extension of the `ChemDataExtractor`_ repository with the functionality to identify candidate chemical scheamtic diagram images automatically.

Installation
------------

To install ChemDataExtractor, clone the repository with::

    git clone https://github.com/edbeard/chemdataextractor-csr.git

and run::

    python setup.py install

Then download the necessary machine learning models with::

    cde data download


Documentation
-------------

This code is intended to be used with the `ChemSchematicResolver`_ software toolkit for the automatic extraction of chemical schematic diagrams. Full details on installation and integration with ChemDataExtractor-CSR can be found at [dummy].

Full documentation on the general use of ChemDataExtractor is available at http://chemdataextractor.org/docs


License
-------

ChemDataExtractor is licensed under the `MIT license`_, a permissive, business-friendly license for open source
software.


.. _`ChemSchematicResolver`: dummy
.. _`MIT license`: https://github.com/mcs07/ChemDataExtractor/blob/master/LICENSE
.. _`ChemDataExtractor`: https://github.com/CambridgeMolecularEngineering/chemdataextractor
