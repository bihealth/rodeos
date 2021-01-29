.. _use_case_facility:

========================
Facility Staff Use Cases
========================

This section describes the use cases for the facility staff.
As an example, the case of a sequencing facility is used where data generation equals performing a sequencing run.
This step can be adjusted appropriately for other data generation unit types.

------------------------------
Group Management for Customers
------------------------------

In this use case, facility staff members want to manage their customers in groups in iRODS.
For new customers they want to create a new group or for retired customers they want to remove groups.
At any other time they want to add/remove users to/from groups.

Prerequisites
=============

- An account must have been properly setup for the user by the RODEOS / iRODS administrator.
  This includes allowing access to privilege for the administration of groups.
- The user must know the prefix for the groups that they can manage (e.g., ``gen-cha::cust::``).
- The user must have setup iRODS iCommands correctly and have configured ``~/.irods/irods_environment.json`` properly.
- The user must have the RODEOS facility staff helper scripts installed.

Steps
=====

- Authenticate with the iRODS server using ``iinit``.
- Use the :ref:`facility_helper_scripts` to manage the groups.

.. _use_case_project_coll:

-----------------------------
Create New Project Collection
-----------------------------

In this use case, a facility staff member creates a new project collection ("collection" is the iRODS term for a folder in the iRODS storage system).
Such a project collection serves as the location for resulting data to share with the customer.
This collection will have read permissions set for the customer group/user recursively and permission inheritance is enabled.
This way, customer users can download the data once it has been provided.

Prerequisites
=============

- A group has been setup for the customers if access needs to be given based on more than one user.

Steps
=====

Use Metalnx to

- create a new folder in the ``projects`` collection of the facility
- make sure that ``inheritance`` is enabled for the collection and use ``Apply recursively`` to apply this to all existing sub folders
- configure permission and add a new ACL for the customer group or user with the ``READ`` permission, make sure to select ``Apply to subcollections and files`` such that existing and data placed in the directory afterwards gets the correct permissions setup

----------------------
Perform Sequencing Run
----------------------

In this use case, facility staff members start a sequencing run into the landing zone provided by RODEOS.

Prerequisites
=============

- The user for the sequencer and ingest process must exist.
- Ingest must have been setup appropriately.

Steps
=====

- Connect network drive to the network share for the sequencer if necessary.
- Write data to this network share.
- Wait until data generation is complete.
- The output folder will be moved into the shadow landing zone folder afterwards.

---------------------------
Perform Sequence Conversion
---------------------------

In this use case, facility staff members start the conversion process from base calls to sequences (``bcl2fastq``) that is also sometimes referred to as "demultiplexing".

Prerequisites
=============

- Digestiflow must have been setup correctly for the sequencer for which demultiplexing should be performed.
- Sequencing should have finished.

Steps
=====

- Start demultiplexing as documented in the Digestiflow documentation.
- Wait for demultiplexing to finish.
- The resulting data will appear in the ``FASTQ`` collection in iRODS.
- The meta data ``rodeos::ingest::status`` will be set to ``complete`` once done.

.. _use_facility_deliver_conversion_results:

--------------------------
Deliver Conversion Results
--------------------------

In this use case, facility staff wants to provide sequencing results to customers.
These could be sequences in FASTQ format and/or archives from raw BCL data such as tarball files created by Digestiflow.

Prerequisites
=============

- Ideally, a project collection has been created for file delivery to the customer.
- Permissions have been created appropriately as described in :ref:`use_case_project_coll`.

Steps
=====

Use Metalnx to:

- create an output collection in the project collection, e.g., named like the flowcell
- go to the folder with the digestiflow demux results
- mark the files and/or folders to move
- move them into the output directory
- in the case that additional data is required for delivery (e.g., manually created QC reports)
    - the facility staff generates the reports, and
    - copies them into the project folder
- notify the customer about the arrival of new data and instructions how to access the data

.. _use_facility_deliver_raw_data:

-----------------------
Provide Raw Data Access
-----------------------

In this use case, facility staff wants to provide direct access to raw data.

Prerequisites
=============

- None.

Caveats
=======

- It is best practice to have only one location from which data is shared.
- Raw data should probably not be shared even read-only.
- For BCL raw data, providing archives as created by Digestiflow are more efficiently shared than the tens of thousands of files in a run folder.

Steps
=====

- Use Metalnx to set the appropriate permissions on the raw data folder.
- Share the path to this folder with the customer together with instructions on how to access the data.

--------------------------
External Customer Delivery
--------------------------

In this use case, facility staff wants to deliver data to external customers.

Prerequisites
=============

- The customer must be provided with an identity in the host organization's user account directory (e.g. ActiveDirectory).
  The account can be limited but at least a user name and password must exist.
  The rationale is that for the transfer of human data which will be necessary in the general case, it will be required that the receiving party is a natural human being whose identity is verified, e.g., by the human resource department.

Steps & Caveats
===============

Once the customer has an identity in the host organization's user account directory, the delivery process is very similar to the use cases :ref:`use_facility_deliver_conversion_results` and :ref:`use_facility_deliver_raw_data` apply.
However, facility staff will have to mark the result iRODS collection (using iRODS meta data through the graphical Metalnx) to be delivered through a particular server that is also reachable from the outside.

Status
======

This use case has been registered but not implemented yet.
It is expected to be implemented at a later milestone.

Until then, other delivery means have to be used with preexisting means.
