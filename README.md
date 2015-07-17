openvasrun
==========

*** Project purpose changed 7/17/15 and continuing work on it ***

Description
-----------
This Python script creates targets and tasks for each IP address listed in an input file.

A future version of it will kick off the tasks up to a maximum number of concurrent runs.

Features
--------
* This script can load very large numbers of IP addresses for scanning into Openvas.

Warning
--------
* As is, the code is pretty inflexible.  For example, it currently only runs 'Full and Fast'
scan configuration.  Feel free to change it as needed.
* I only tested this on one system against a limited network segment with about 40 targets.
* It runs in a second or two with 40 targets, but I can't say how performance would be on 
  1,000+ to tens of thousands hosts.
* You will see some annoying debug messages.  I'll turn those off eventually.
* Sorry, but it doesn't yet have the task execution part in it yet.  Hopefully soon!

Usage
-----
1. Place file in any directory.

2. In the same directory, create a file called target_addresses.txt which should contain a list of IP addresses for which target records and task records are to be created.

3. Delete all target records and tasks which may conflict, such as any task or a target with an IP within the target_addresses.txt file.

4. run this command:   python ./openvasrun.py 



### Options
None

Requirements
------------
Linux OS / Python / OpenVas

Versions tested:

Linux: 3.14-kali1-686-pae

Python: 2.73

OpenVAS Manager 5.0.2

OMP Command Line Interface 1.3.0

OpenVAS Scanner 4.0.2

Copyright and license
---------------------
openvasrun is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

openvasrpt is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  

See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with nmapformat. 
If not, see http://www.gnu.org/licenses/.

Contact
-------
* Andy Marks < ajmarcs at yahoo d0t com >
