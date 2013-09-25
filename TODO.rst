*********
TODO.rst
*********

In no particular order,

Goals:
======
* Connect COD
* establish links with other databases such as drugbank.
* Add COD to the set of tools for exploring biologically active compounds.
* Implement a PCOD/TOCD/COD mirror using a non-relational distributable DB (say, MongoDB) as a standalone system.
    1. MongoDB has multi-master replication out-of-the-box.
    2. SciDB can also be considered.
* Establish a two-way communication of this mirror with COD databases.

Strategic Goals for COD databases:
===================================
* fully distributed
* fault and disruption tolerant system of *equal peers*
* run without any central server.

