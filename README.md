openvasrun
==========

Description
-----------
This Python script creates targets and tasks for each IP address listed in an input file.
(Tested and working in a simple 40-target environment.)  It then kicks off tasks, 
eventually completing all that have been loaded.

The primary benefit is throttling: Openvas tasks up to a maximum number of concurrent runs
will be started.  As some complete, more will start up to the max_concurrent_scans 
variable, set to 3 by default.  Edit the program to change it.  In the future, it will be
added as an optional argument.

Features
--------
* This script can scan a very large number of IP addresses with Openvas.  No more need to to kick them off one at a time.
* The number of concurrent scans executed can be set;  the default is 3.

Warnings and Caveats
--------
* As is, the code is pretty inflexible, meaning I don't have robust error handling, maximum automation, or the use of arguments yet.  For example, it currently only runs 'Full and Fast'
scan configuration.  Feel free to change it in your copy of the source code as needed.
* Make sure you don't duplicate IP addresses in the file.
* I only tested this on one system against a limited network segment with about 40 targets.

Usage
-----
0. Make sure Openvas is operational.  Set up the omp.config in your home directory.  Be sure to include username and password.

1. Place the openvasrun.py file in any directory.

2. In the same directory, create a file called target_addresses.txt (default name) which should contain a list of IP addresses for which target records and task records are to be created.

3. Delete all target records and tasks which may conflict, such as any task or a target with an IP within the target_addresses.txt file.

4. run this command:   python ./openvasrun.py 

### Options

python openvasrun.py -h
usage: openvasrun.py [-h] [-i FILE] [-s [SLEEP]] [-c [CONCURRENT]] [-d]

optional arguments:

  -h, --help            show this help message and exit

  -i FILE, --inputfile FILE

Input file with IP addresses, one per line. Default

name is target_addresses.txt

  -s [SLEEP], --sleep [SLEEP]

Amount of time in seconds to sleep between status

checks

  -c [CONCURRENT], --concurrent [CONCURRENT]

Maximum number of concurrent processes allowed

  -d, --debug           Show debug messages


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
