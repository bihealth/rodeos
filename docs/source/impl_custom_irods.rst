.. _impl_custom_irods:

===================
iRODS Customization
===================

This section describes the iRODS customizations that have been installed / implemented.

--------------
Rule Adoptions
--------------

- By default, no home directory is created for newly created users.
  This is a deviation from the standard iRODS behaviour.

-------------
Microservices
-------------

The software `irods-sudo-microservices <https://github.com/UtrechtUniversity/irods-sudo-microservices>`__ has been installed on the iRODS provider (catalogue) server.
This allows to implement rules with privilege escalation.

------------
AVU Prefixes
------------

Generally, the RODOES system uses the prefix ``rodeos::`` for AVU (attribute value unit) triples.

The RODEOS Ingest subsystem uses the prefix ``rodeos::ingest`` for meta data annotation and state management.

To allow facility members to manage groups of customers, AVU triples with the attribute name ``rodeos::sudo::group-prefix`` are created.
Such users can then invoke the ``msiSudoUserAdd()`` microservice to manipulate groups whose name starts with the given prefix.
Of course, good care has to be taken for such prefixes to be unique, generally group names are ``${UNIT}::${CUSTOMER}`` with short identifiers of the unit and the customer group.

-----
Rules
-----

The following rules have been implemented for the ``irods-sudo-microservices`` package.

acPreSudoGroupAdd
    Allow users to add groups with the name that starts with the value of any value of the ``rodeos::sudo::group-prefix`` attribute.
acPreSudoGroupRemove
    Allow users to remove groups with the name that starts with the value of any value of the ``rodeos::sudo::group-prefix`` attribute.
acPreSudoGroupMemberAdd
    Allow users to add members to groups with the name that starts with the value of any value of the ``rodeos::sudo::group-prefix`` attribute.
acPreSudoGroupMemberRemove
    Allow users to remove members from groups with the name that starts with the value of any value of the ``rodeos::sudo::group-prefix`` attribute.

--------------
Custom Scripts
--------------


.. _facility_helper_scripts:

RODEOS Facility Helper Scripts
==============================

RODEOS ships with a number of Bash scripts that help facility staff in the management of users:

rodeos-cli-group-list
    Lists existing groups that the current user can manager.
rodeos-cli-group-create GROUP_NAME
    Create a new group with the given name.
rodeos-cli-group-remove GROUP_NAME
    Delete group with the given name.
rodeos-cli-group-member-add GROUP_NAME USER_NAME
    Add a user with the given name to the given group.
rodeos-cli-group-member-remove GROUP_NAME USER_NAME
    Remove a member from a group.
