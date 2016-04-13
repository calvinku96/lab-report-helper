Tutorial
========

Suppose we need to make a lab report on an experiment on the inverse square law.
You have a set of data: distance vs power.

.. code-block:: latex

    # isl.txt
    0.1     100
    0.2     25
    0.3     11.1
    0.4     6.25
    0.5     4
    0.6     2.778
    0.7     2.04
    0.8     1.56
    0.9     1.23
    1.0     1

Initialization
--------------

First assign a folder for the report

.. code-block:: bash

    $ mkdir project
    $ cd project

and then do

.. code-block:: bash

    $ make-lab-report

This will create some files as follows

.. code-block:: bash

    data/
        .keep
    pickle/
        .keep
    plots/
        .keep
    python/
        constant.py
        __init__.py
        process.py
        variables.py
        .keep
    tables/
        .keep
    manage.py
    settings.json

The ``.keep`` files is for version control systems to keep the folders ``data``,
``pickle``, ``plots``, and ``tables`` as it is assumed to be present and
will throw an error if those folder is not present.

In this folder, you can also keep the report files

.. code-block:: bash

    touch report.tex # your lab LaTeX/doc/docx/etc file


Inserting experiment data
-------------------------

There are built in parser for the data which will be *pickled* (or *hickled*)
so that it can be easily extracted. First, we need to tell ``labreporthelper``
what data you will use. In ``python/process.py``, you will see

.. code-block:: python

    """
    Main Module. All operations are put here
    """
    from labreporthelper.dataset import DataSets
    
    
    class Experiment(DataSets):
        """
        Data Processing, Plots, LaTeX Macros, and Tables
        """
        data = {}
    
        def operations(self):
            """
            Main operations
            """

All data files needed to be listed as a dictionary.

.. code-block:: python
    :emphasize-lines: 14

    """
    Main Module. All operations are put here
    """

    from labreporthelper.dataset import DataSets
    from labreporthelper.datafile import DataFile


    class Experiment(DataSets):
        """
        Data Processing, Plots, LaTeX Macros, and Tables
        """
        data = {
            "isl": DataFile("isl", ext="txt"),
        }

        def operations(self):
            """
            Main operations
            """

.. note::

    Here, the class ``DataFile`` wraps the function ``numpy.loadtxt``.
    See :py:class:`labreporthelper.datafile.DataFile`

Put your data in ``data/isl.txt`` and run in your project folder

.. code-block:: bash

    ./manage.py parse-data

This will search the data dictionary and put all the data to the ``pickle``
folder in ``pickle`` format. So you will see

.. code-block:: bash
    :emphasize-lines: 3,6

    data/
        .keep
        isl.txt
    pickle/
        .keep
        isl.pickle
    plots/
        .keep
    python/
        constant.py
        __init__.py
        process.py
        variables.py
        .keep
    tables/
        .keep
    manage.py
    settings.json

Make Plots
----------
We will then want to create the plot of the data

.. code-block:: python
    :emphasize-lines: 7-10,25-49

    """
    Main Module. All operations are put here
    """

    from labreporthelper.dataset import DataSets
    from labreporthelper.datafile import DataFile
    # wrapper for scipy.curve_fit
    from labreporthelper.bestfit.curvefit import CurveFit
    # wrapper for numpy.polyfit
    from labreporthelper.bestfit.polyfit import PolyFit


    class Experiment(DataSets):
        """
        Data Processing, Plots, LaTeX Macros, and Tables
        """
        data = {
            "isl": DataFile("isl", ext="txt"),
        }

        def operations(self):
            """
            Main operations
            """
            # unpickle data and assign to data_isl
            data_isl = self.data["isl"].get_internal_data()
            # plot y vs x
            bestfit_isl = CurveFit(
                x=data_isl[:, 0], y=data_isl[:, 1],
                func=lambda x,a: a / x**2, num_vars=1
            )
            self.plot_2d_single(
                data_isl[:, 0], data_isl[:, 1],
                "isl_plot", xlabel=r'$x\,(m)', ylabel='Power',
                bestfit=bestfit_isl
            )

            # plot y vs 1/x^2
            x_inverse_squared = data_isl[:, 0]**(-2)
            bestfit_isl2 = PolyFit(
                x=x_inverse_squared, y=data_isl[:, 1],
            )
            # all labels are put to .format() and so LaTeX {...} must
            # be converted to {{...}}
            self.plot_2d_single(
                x_inverse_squared, data_isl[:, 1],
                "isl_plot2", xlabel=r'$x^{{-2}}\,(m^{{-2}})$',
                ylabel='Power', bestfit=bestfit_isl2
            )
.. seealso::
    
    :py:class:`labreporthelper.bestfit.bestfit`,
    :py:class:`labreporthelper.bestfit.curvefit`,
    :py:class:`labreporthelper.bestfit.polyfit`

Run

.. code-block:: bash

    ./manage.py do-operations

to get the plot. We will then have

.. code-block:: bash
    :emphasize-lines: 9,10

    data/
        .keep
        isl.txt
    pickle/
        .keep
        isl.pickle
    plots/
        .keep
        isl_plot.pdf
        isl_plot2.pdf
    python/
        constant.py
        __init__.py
        process.py
        variables.py
        .keep
    tables/
        .keep
    manage.py
    settings.json

The plots then can be put to the report
(eg. using ``\includegraphics`` in LaTeX)

Use ``DataSets.make_compute_file()`` for calculated variables
-------------------------------------------------------------

This can only be used for reports in LaTeX. This creates a ``compute.tex``
file in the project folder. In this example, we can do

.. code-block:: python
    :emphasize-lines: 50-53

    """
    Main Module. All operations are put here
    """

    from labreporthelper.dataset import DataSets
    from labreporthelper.datafile import DataFile
    # wrapper for scipy.curve_fit
    from labreporthelper.bestfit.curvefit import CurveFit
    # wrapper for numpy.polyfit
    from labreporthelper.bestfit.polyfit import PolyFit


    class Experiment(DataSets):
        """
        Data Processing, Plots, LaTeX Macros, and Tables
        """
        data = {
            "isl": DataFile("isl", ext="txt"),
        }

        def operations(self):
            """
            Main operations
            """
            # unpickle data and assign to data_isl
            data_isl = self.data["isl"].get_internal_data()
            # plot y vs x
            bestfit_isl = CurveFit(
                x=data_isl[:, 0], y=data_isl[:, 1],
                func=lambda x,a: a / x**2, num_vars=1
            )
            self.plot_2d_single(
                data_isl[:, 0], data_isl[:, 1],
                "isl_plot", xlabel=r'$x\,(m)', ylabel='Power',
                bestfit=bestfit_isl
            )

            # plot y vs 1/x^2
            x_inverse_squared = data_isl[:, 0]**(-2)
            bestfit_isl2 = PolyFit(
                x=x_inverse_squared, y=data_isl[:, 1],
            )
            # all labels are put to .format() and so LaTeX {...} must
            # be converted to {{...}}
            self.plot_2d_single(
                x_inverse_squared, data_isl[:, 1],
                "isl_plot2", xlabel=r'$x^{{-2}}\,(m^{{-2}})$',
                ylabel='Power', bestfit=bestfit_isl2
            )
            self.vardict["bestfitIslFitArgs"] = bestfit_isl.get_fit_args()[0]
            self.vardict["bestfitIslRmse"] = bestfit_isl.get_rmse()
            self.vardictformat["bestfitIslRmse"] = "{:.4e}"
            self.make_compute_file()

.. seealso:: :py:meth:`labreporthelper.dataset.DataSets.make_compute_file`

The project root directory will have a file ``compute.tex``

.. code-block:: bash
    :emphasize-lines: 19

    data/
        .keep
        isl.txt
    pickle/
        .keep
        isl.pickle
    plots/
        .keep
        isl_plot.pdf
        isl_plot2.pdf
    python/
        constant.py
        __init__.py
        process.py
        variables.py
        .keep
    tables/
        .keep
    compute.tex
    manage.py
    settings.json

with the contents of ``compute.tex`` being

.. code-block:: bash

    $ cat compute.tex
    \newcommand{\bestfitIslFitArgs}{1.000e00}
    \newcommand{\bestfitIslRmse}{3.8682e-03}
    $ 

To get scientific notation in latex, use

.. code-block:: latex

    \usepackage{siunitx}
    % report
    \num{\bestfitIslFitArgs}
    % rest of the report

.. warning::
    Be careful of name clashes in macros. Here, the ``\newcommand``
    will error out if there is any macro name clashes

Use ``DataSets.make_tex_table()`` to make tables for calculated variables
-------------------------------------------------------------------------

We can also create a table for the data in ``isl.txt`` using the
``DataSets.make_tex_table()`` method.

.. code-block:: python

    """
    Main Module. All operations are put here
    """

    from labreporthelper.dataset import DataSets
    from labreporthelper.datafile import DataFile
    # wrapper for scipy.curve_fit
    from labreporthelper.bestfit.curvefit import CurveFit
    # wrapper for numpy.polyfit
    from labreporthelper.bestfit.polyfit import PolyFit


    class Experiment(DataSets):
        """
        Data Processing, Plots, LaTeX Macros, and Tables
        """
        data = {
            "isl": DataFile("isl", ext="txt"),
        }

        def operations(self):
            """
            Main operations
            """
            # unpickle data and assign to data_isl
            data_isl = self.data["isl"].get_internal_data()
            # plot y vs x
            bestfit_isl = CurveFit(
                x=data_isl[:, 0], y=data_isl[:, 1],
                func=lambda x,a: a / x**2, num_vars=1
            )
            self.plot_2d_single(
                data_isl[:, 0], data_isl[:, 1],
                "isl_plot", xlabel=r'$x\,(m)', ylabel='Power',
                bestfit=bestfit_isl
            )

            # plot y vs 1/x^2
            x_inverse_squared = data_isl[:, 0]**(-2)
            bestfit_isl2 = PolyFit(
                x=x_inverse_squared, y=data_isl[:, 1],
            )
            # all labels are put to .format() and so LaTeX {...} must
            # be converted to {{...}}
            self.plot_2d_single(
                x_inverse_squared, data_isl[:, 1],
                "isl_plot2", xlabel=r'$x^{{-2}}\,(m^{{-2}})$',
                ylabel='Power', bestfit=bestfit_isl2
            )
            self.vardict["bestfitIslFitArgs"] = bestfit_isl.get_fit_args()[0]
            self.vardict["bestfitIslRmse"] = bestfit_isl.get_rmse()
            self.vardictformat["bestfitIslRmse"] = "{:.4e}"
            self.make_tex_table(
                zip(data_isl[:, 0], x_inverse_squared, data_isl[:, 1]),
                "isl_table"
            )
            self.make_compute_file() # always put this at the end of the method

.. seealso:: :py:meth:`labreporthelper.dataset.DataSets.make_compute_file`

Then running ``./manage.py do-operations`` gives

.. code-block:: bash
    :emphasize-lines: 18

    data/
        .keep
        isl.txt
    pickle/
        .keep
        isl.pickle
    plots/
        .keep
        isl_plot.pdf
        isl_plot2.pdf
    python/
        constant.py
        __init__.py
        process.py
        variables.py
        .keep
    tables/
        isl_table.tex
        .keep
    compute.tex
    manage.py
    settings.json

with the contents of ``isl_table.tex`` being

.. code-block:: bash

    $ cat tables/isl_table.tex
    $\num{0.1}$&$\num{100}$&$\num{100}$\\
    $\num{0.2}$&$\num{25}$&$\num{25}$\\
    $\num{0.3}$&$\num{11.1111}$&$\num{11.1}$\\
    $\num{0.4}$&$\num{6.25}$&$\num{6.25}$\\
    $\num{0.5}$&$\num{4}$&$\num{4}$\\
    $\num{0.6}$&$\num{2.77778}$&$\num{2.778}$\\
    $\num{0.7}$&$\num{2.04082}$&$\num{2.04}$\\
    $\num{0.8}$&$\num{1.5625}$&$\num{1.56}$\\
    $\num{0.9}$&$\num{1.23457}$&$\num{1.23}$\\
    $\num{1}$&$\num{1}$&$\num{1}$\\

To add to the report simply add the following to the main report ``.tex`` file

.. code-block:: latex

    \begin{tabular}{|l|l|l|}
      \hline
      $x$&$x^{-1}$&Power\\
      \hline
      \input{tables/isl_table}
      \hline
    \end{tabular}

To where you want to add the table.
