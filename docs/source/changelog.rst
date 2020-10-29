.. _changelog:

:gitlab_url: https://gitlab.com/isaac-cfwong/slurmpter

*********
Changelog
*********

All notable changes to this project will be documented in this page.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

[0.1.0] - 2020-10-29
--------------------

**Added**

- Added classes ``Slurm`` and ``SlurmJob`` which use the ``PyCondor`` as the backend to
  handle a workflow of jobs to build and submit Slurm submit files.
