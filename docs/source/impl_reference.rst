.. _impl_reference:

========================
Reference Implementation
========================

This section describes an example/reference implementation/installation of RODEOS as deployed by `Core Unit Bioinformatics (CUBI) <https://www.cubi.bihealth.org>`__ at Berlin Institute of Health.

--------------------------
Centralized Storage System
--------------------------

CUBI uses a centralized storage system based on Ceph and CephFS.
All data for the RODEOS system is stored below ``/rodeos``.

iRODS Server
    The iRODS server uses the server ``/rodeos/irods-vault`` for storing its data.
    It only has this path mounted such that it cannot access anything else from the central file system.
HPC System
    The HPC system has the path ``/rodeos/lz`` mounted and unix groups and permissions are used to provide the data generation units with appropriate access to their data.
    The iRODS data vault is only available to the iRODS server.

-------------
Landing Zones
-------------

For instruments such as sequencing devices, the landing zones are implemented as follows.

Landing Zones
    For each data generation unit ``${UNIT}`` and each instrument (or data generation process) ``${INST}``, a folder ``/rodeos/lz/${UNIT}/${INST}`` is created.
    These folders are exported via Windows SMB/CIFS network shares and mounted on the instrument driver computers.
    The instruments write into these directories.
Shadow directories
    Further, the folder ``/rodeos/lz/${UNIT}/${INST}-INGESTED`` exists for each group and instrument and serves as the shadow folder.
    This folder is not exposed to the instrument but made available to the data generation unit with appropriate unix permissions.

For data processing that runs on the HPC system, the data generation (through processing) is implemented as follows.
Both landing zones and shadow directories are also managed below the ``/rodeos/lz`` directory as above but they are not shared via the network.
Instead, there are dedicated Unix users for the data processing (that is separate from the instrument's Unix user) and Unix groups and permissions are used such that the processing user can write into the landing zone but cannot access the shadow folder.

-----------
Data Ingest
-----------

Data ingest is implemented using one dedicated ingest server that has ``/rodeos/lz`` mounted.
There is one dedicated Unix account for the ingestion of each data generation source, that has corresponding a iRODS account and is permanently authenticated as this account.
The ingest process runs as this Unix user and monitors the corresponding landing zone, ingests the data into iRODS, and moves the data from the landing zone into the shadow folder when done.

-----------
Digestiflow
-----------

Demultiplexing of genomics data is used using the Digestiflow system developed at CUBI.
Genomics facility staff uses the Digestiflow server as documented in the `Digestiflow documentation <https://digestiflow-server.readthedocs.org>`__.

Demultiplexing and ingest of data is done using a periodically running job on the HPC system.
Both jobs run as the same Unix user, one for each genomics facility.
There is one ``FASTQ`` landing zone (with corresponding shadow directory) for each facility and data is ingested as in the general case.

-------------
Data Delivery
-------------

Data delivery has been implemented as described in the use case section.
For delivery, it is assume that the genomics unit staff creates a dedicated collection for each project (the definition of a "project" depends on the genomics unit, e.g. a service order).
Data from one or more sequencing runs (either a whole or parts of a run) can be delivered by moving or copying it into that collection in RODEOS iRODS.

The delivery process is summarized as below.
Once the data is ready:

- genomics facility staff
    - moves the data into the project-based delivery folder
    - ensures that the destination user has the appropriate permissions to read the data
    - sends out an email with the information on how to access the data to the customer
- customer
    - receives the email with information
    - if necessary reads the documentation provided on a public server about the different access options
    - downloads the data using the provided iRODS commands or via WebDAV
