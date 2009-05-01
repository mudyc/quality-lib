
==================================
User Manual of the Quality Library
==================================


Install instructions
=====================

apt-get install python

Starting execution
===================


Synopsis
--------

   qdoc.py DESTINATION SOURCE...

Options
-------

   DESTINATION
      The destination directory where generated documents are stored.

   SOURCE
      The source files in reStructuredText format.

Example
-------

::

   python qdoc.py gen/ documentation/*.rst


Linking Syntax
==============

Keep it simple and use ref directive now.



That is described in more detail in here_.


_here: ref:architecture/static-structure/components

.. ref::src/foo.py/get_doo

