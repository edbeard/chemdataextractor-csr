ChemDataExtractor-CSR
=====================


.. image:: http://img.shields.io/pypi/l/ChemDataExtractor.svg?style=flat-square
    :target: https://github.com/edbeard/chemdataextractor-csr/blob/master/LICENSE


ChemDataExtractor-CSR is an extension of `ChemDataExtractor`_ with the functionality to identify candidate chemical schematic diagram images automatically.

Installation
############

Option 1: **conda** package manager
-----------------------------------

Installation via conda is highly recommended. Simply run::

    conda install -c edbeard chemdataextractor-csr
    
Option 2: From source
---------------------

Otherwise, please try installing from source.

Clone the repository with::

    git clone https://github.com/edbeard/chemdataextractor-csr.git

and run::

    python setup.py install

Then download the necessary machine learning models with::

    cde data download


Documentation
-------------

This code is intended to be used with the `ChemSchematicResolver`_ software toolkit for the automatic extraction of chemical schematic diagrams. Full details on installation and integration with ChemDataExtractor-CSR can be found in the `documentation`_.

Full documentation on the general use of ChemDataExtractor is available at http://chemdataextractor.org/docs


License
-------

ChemDataExtractor is licensed under the `MIT license`_, a permissive, business-friendly license for open source
software.


.. _`ChemSchematicResolver`: http://www.chemschematicresolver.org
.. _`MIT license`: https://github.com/edbeard/ChemDataExtractor-CSR/blob/master/LICENSE
.. _`ChemDataExtractor`: http://www.chemdataextractor.org
.. _`documentation`: http://www.chemschematicresolver.org/docs
