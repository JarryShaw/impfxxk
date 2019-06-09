======================================
impfxxk -- Import for Humans 💅🏻
======================================

This is to be a project on modifying ``sys.meta_path`` and
making Python ``import`` statement as smooth as possible.

Inspiration
===========

This idea was originally inspired from the |bro|_ language,
where it uses ``@load`` statement what ``import`` doses in
Python, except that the ``@load`` statement takes a
relative path as its specifier. For example:

.. code:: bro

    @load ./sample_local.bro
    @load ../sample_parent.bro
    @load ../sample/child.bro

with the project structure as following:

.. code:: text

    root
    |-- foo
    |   |-- this_script.bro
    |   |-- sample_local.bro
    |   |-- sample
    |       |-- child.bro
    |-- sample_parent.bro

which means, the ``@load`` statement is always relative to
where it comes from, rather than a *working directory*
or *package root* as in Python.

Thus, we intend to make the Python ``import`` statement
works just like ``@load``. This is the back story of the
``impfxxk`` project.

Expectation
===========

When your project is as such:

.. code:: text

    root
    |-- foo
    |   |-- this_script.py
    |   |-- sample_local.py
    |   |-- sample
    |       |-- child.py
    |-- sample_parent.py

Normally, you will want to do:

.. code:: python

    import .sample_local
    import .sample.child
    import ..sample_parent

there can be some issues when the Python interpreter tries
to figure out what is what when you are not running it at
``/root/foo/``, where the relative paths are ought to be.

However, with ``impfxxk``, you can simply add a statement
(it's not decided yet) before your original ``import``
statements, just like |future| does; and your code will
work just as you wish.

.. |bro| replace:: Bro/Zeek
.. _bro: https://www.zeek.org

.. |future| replace:: ``__future__``
.. _future: https://docs.python.org/3/library/__future__.html
