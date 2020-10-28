.. _slurmjob:

:gitlab_url: https://gitlab.com/isaac-cfwong/slurmpter

--------
SlurmJob
--------

:ref:`SlurmJob API <job-api>`

Constructor of ``SlurmJob``:

.. code-block:: python

    SlurmJob(name,
             executable,
             error=None,
             output=None,
             submit=None,
             nodes=None,
             ntasks_per_node=None,
             cpus_per_task=None,
             mem_per_node=None,
             extra_sbatch_options=None,
             extra_srun_options=['ntasks=1', 'exclusive'],
             extra_lines=None,
             modules=None,
             slurm=None,
             arguments=None,
             verbose=0)

The constructor provides the basic arguments that are commonly needed to be added into the slurm script.

- ``nodes``: Request that a minimum of minnodes nodes be allocated to this job.

- ``ntasks_per_node``: Request that ntasks be invoked on each node.

- ``cpus_per_task``: Request that ncpus be allocated per process.

- ``mem_per_node``: Specify the real memory required per node.

- ``modules``: A list of modules to load.

Other arguments can be added through ``extra_sbatch_options`` and ``extra_srun_options``. For more details, please check the documentation of Slurm: `sbatch <https://slurm.schedmd.com/sbatch.html>`_ and `srun <https://slurm.schedmd.com/srun.html>`_. The skeleton of the submit file is as follows:

.. code-block:: bash

    #!/bin/bash
    #SBATCH --job-name=<name>
    #SBATCH --output=<submit>/<name>.output
    #SBATCH --error=<submit>/<name>.error

    ```
    ## Speify nodes, ntasks_per_node, cpus_per_task, mem_per_node if provided.
    #SBATCH --<nodes,ntasks_per_node,cpus_per_task,mem_per_node>=<>
    ```

    ```
    ## Extra sbatch options if extra_sbatch_options if provided.
    #SBATCH --<extra_sbatch_option_0>
    #SBATCH --<extra_sbatch_option_1>
    ...
    ```

    ```
    ## Extra lines to be added if extra_lines is provided.
    <extra_lines_0>
    <extra_lines_1>
    ...
    ```

    ```
    ## Load modules if modules is provided.
    module load <module_0>
    module load <module_1>
    ...
    ```

    srun --<extra_srun_option_0> --<extra_srun_options_1> ... <executable> <argument_0> &
    srun --<extra_srun_option_0> --<extra_srun_options_1> ... <executable> <argument_1> &
    ...
    wait
