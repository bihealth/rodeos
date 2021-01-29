=========================
RODEOS Main Documentation
=========================

The aim of the RODEOS (Raw Omics Data accEss and Organization System) system is to facilitate the management and access to Omics raw mass data (e.g., genomics or proteomics data).
The system itself is based on the `iRODS <https://irods.org>`__ ecosystem:

- iRODS for mass data storage and meta data management,
- Metalnx as a graphical user interface to iRODS, and
- Davrods for WebDAV based access to the data.

This is the main entry point for the documentation.
It describes the big picture and how the different components interact.
Where appropriate, it references to the (external) documentation of the particular components.

.. toctree::
    :maxdepth: 1
    :caption: Introduction

    intro_overview
    intro_related_software

.. toctree::
    :maxdepth: 1
    :caption: Implementation Details

    impl_ingest
    impl_sequencers
    impl_demux
    impl_reference
    impl_custom_irods

.. toctree::
    :maxdepth: 1
    :caption: Use Cases

    use_case_admin
    use_case_facility
    use_case_customer
