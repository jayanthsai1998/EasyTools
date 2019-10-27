
Easy Tools
==============


Python's ``itertools`` library is a gem - you can compose elegant solutions
for a variety of problems with the functions it provides. In ``easy-tools``
we collect additional building blocks, recipes, and routines for working with
Python iterables.

----


Getting started
===============

To get started, install the library with `pip <https://pip.pypa.io/en/stable/>`_:

.. code-block:: shell

    pip install easy-tools

The recipes (modules/functions) included in this package are: 
<table >
    <tr>
        <td align="center" > <strong> Arrays </strong> </td>
    </tr>
    <tr>
        <td align="center"> doublet_occurrence </td>
    </tr>
    <tr>
        <td align="center">triplet_occurrence </td>
    </tr>
    <tr>
        <td align="center"> equilibrium_point</td>
    </tr>
    <tr>   
        <td align="center"> non_divisible_subset_len </td>
    </tr>
    <tr>
        <td align="center"> leaders_to_left</td></tr>
    <tr>
        <td align="center"> divisible_pairs </td></tr>
    <tr>
        <td align="center"> leaders_to_right</td>
    </tr>
    <tr>
        <td align="center">largest_number_possible </td>
    </tr>
   
</table>


For example,

.. code-block:: python

    >>> from easy_tools import largest_number_possible
    >>> iterable = [98, 9, 26]
    >>> largest_number_possible(iterable)
    99826




You can use help function to get the detailed description of a function.

.. code-block:: python

    >>> help(function_name)

Development
===========

``easy-tools`` is maintained by `@jayanth <https://github.com/jayanthsai1998>`_.
If you have a problem or suggestion, please file a bug or pull request in this
repository. Happy Pythoning!
