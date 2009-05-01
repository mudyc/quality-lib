
===============
Quality library
===============

:author: Matti Katila


*Quality library* is a tool to publish interlinked documents for
software products. The tool itself is a slight extension to docutils
and thus utilizes reStructuredText heavily.

The intent of quality library is to raise quality of open source
software, ease the use and adoption of open source software, help on
usability and make world a better place. I'm not keen to use the word
'quality'. It does have too many definitions; at least one for
everyone. My personal definition for quality is ``something, that can
be measured``. And something that is easy to measure is
documentation. Usually there exists none. Or if there's a one it's not
the one I would be looking for. Thus, this project should be able to
raise quality by providing tools to make library, a set of documents
around your software. 

The quality library encourages to produce at least two documents for
two different kind of users. These two kind of users are the end user
and a developer.

The point of quality library is to provide links between documents.
At some point I'll hope we could also link to the source code but
let's make a step at time.::

     End user           Developer

     User manual <----> Architecture <--later--> source code

Links from user manual to architecture are provided simply to help end
user adapt to the conceptual model. This is achieved when the user can
study what actually happens under the hood. This helps on visibility
of the product - an essential attribute consider by Norman [norman]_.

The existence of user manual makes it easier to design the
software. If things need to be considered from end user's point of
view it also helps to produce better usability for the software. This
should be done before design, actually.

We can go even further. We can add bug database to the system::

     End user           Developer

     User manual <----> Architecture <--later--> source code
             ^            ^
             |            |
             v            v
              Bug database 

This is done by adding "report a bug or misinformation or an
improvement" links after each section in the user manual or
architecture specification or some other document. Aslo we can add
backlinks, i.e. an information from where is this section linked from.

::

  gh-pages/
    index.rst
    documents/
      tutorial.rst
      user_manual.rst
      architecture_spec.rst
    screenshots/
    bugs/
   



References
------------

* [norman] Donald Norman, "The Design of Everyday Things", 1988.
