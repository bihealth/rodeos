.. _use_case_customer:

==================
Customer Use Cases
==================

This section describes use cases for facility customers.

-----------------
iRODS Data Access
-----------------

In this use case, a customer downloads data that has been delivered to them by the facility staff (cf. :ref:`use_case_facility`) via the **iRODS iCommands**.

Prerequisites
=============

- The user must have the iRODS iCommands command line tools installed.
  These are only available for Linux and MacOS.
  Windows users should use the WebDAV protocol.
- The user has knowledge of the Linux/MacOS command line.
  Inexperienced users are recommended to use the WebDAV protocol with a graphical client.
- The user must be able to connect to the iRODS server.
  For the server operated by CUBI, the client must be in the Charite/MDC/BIH networks or have appropriate VPN access.

Steps
=====

- Perform the iRODS setup, in particular creating a proper ``~/.irods/irods_environment.json`` file.
- Successfully authenticate to the iRODS server with ``iinit``.
- Use ``irsync -rkv i:${SOURCE} ${DEST}`` to download the data from the ``${SOURCE}`` collection in iRODS as obtained from the data generation facility to the local destination ``${DEST}``.

----------------------------
Graphical WebDAV Data Access
----------------------------

In this use case, a customer downloads data that has been delivered to them by the facility staff (cf. :ref:`use_case_facility`) via the **WebDAV protocol using a graphical client**.

Prerequisites
=============

- The user must have a graphical client installed that can use the WebDAV protocol.
  Recommended free software is:

  - WinSCP for Windows
  - Cyberduck for Mac Os X
  - The usual file browsers for Linux.

- The user must be able to connect to the iRODS server.
  For the server operated by CUBI, the client must be in the Charite/MDC/BIH networks or have appropriate VPN access.

Steps
=====

- Connect to the RODEOS WebDAV server and login to the system.
- Go to the location ``${SOURCE}`` where the data for the user resides.
- Download the data through the graphical client's functionality (probably drag and drop).

-----------------------
LFTP WebDAV Data Access
-----------------------

In this use case, a customer downloads data that has been delivered to them by the facility staff (cf. :ref:`use_case_facility`) via the **WebDAV protocol using the command line client lftp**.

Prerequisites
=============

- The user has knowledge of the Linux/Mac command line.
  Inexperienced users are recommended to use the WebDAV protocol with a graphical client.
- The user must have lftp installed.
  The software is only available on Linux/MacOS so such an operating system is a prerequisite for installing lftp itself.
  Please install lftp with your Linux package manager or a tool like Homebrew for MacOS for installing lftp.
  If this poses a problem we recommend using one of the graphical WebDAV clients as described above.
- The user must be able to connect to the iRODS server.
  For the server operated by CUBI, the client must be in the Charite/MDC/BIH networks or have appropriate VPN access.

Steps
=====

- Connect to the WebDAV server using the user's account.
- Download the data from the ``${SOURCE}`` collection where the data for the user resides using ``mirror ${SOURCE} ${DEST}`` to the local destination directory ``${DEST}``.
