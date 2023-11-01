Developer Documentation
-----------------------

Install requirement
^^^^^^^^^^^^^^^^^^^

.. code-block:: shell

    pip install -r requirements.txt
    pip install -r dev_requirements.txt
    pip install -r doc_requirements.txt

Makefile
^^^^^^^^

First check **Makefile**. It contains many useful commands to work with the project:

.. include:: ../Makefile

Get started
^^^^^^^^^^^

You can start with test and test coverage:

.. code-block:: shell

    make coverage
    make test

Check lint and test coverage before sending pull-request

.. code-block:: shell

    make lint

Build documentation
^^^^^^^^^^^^^^^^^^^

.. code-block:: shell

    make package_docs
    cd docs
    make clean html
    make html

Improve core function
^^^^^^^^^^^^^^^^^^^^^

The main point is to improve `find-similar` core algorithm.
To do that you can use special **laboratory**.
It's the powerful tool to work with `find-similar`
The **Laboratory** places in the `separate repository <https://github.com/findsimilar/laboratory>`_.
Please check the laboratory `README <https://github.com/findsimilar/laboratory>`_ to use it with `find-similar`