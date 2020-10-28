.. _slurm:

:gitlab_url: https://gitlab.com/isaac-cfwong/slurmpter

-----
Slurm
-----

:ref:`Slurm API <slurm-api>`

Constructor of ``Slurm``:

.. code-block:: python

    Slurm(name, submit=None, extra_lines=None, verbose=0)

``extra_lines`` is a list of lines to be added into the submit file. The skeleton of the submit file is as follows:

.. code-block:: bash

    #!/bin/bash
    #SBATCH --job-name=<name>
    #SBATCH --output=<submit>/<name>.output
    #SBATCH --error=<submit>/<name>.error

    <extra_lines>

    jid0=($(sbatch <dependency if any> <job submit file>))
    jid1=($(sbatch <dependency if any> <job submit file>))
    ...
    ...
