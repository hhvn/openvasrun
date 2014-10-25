openvasrpt
==========

*** Project on hold as of 10/25/14 *** 

Description
-----------
This Python script converts Openvas XML full reports into a vulnerability summary report delimited text file. This eases vulnerability analyis during the search for exploits

Features
--------
* This project provides an example of XML file parsing with another Python package I highly recommend called Untangle.

Usage
-----
1. Install untangle, an XML parser for Python.  The package can be found at https://github.com/stchris/untangle .

2. Download the Python script to /tmp.

3. Make a directory called ov in tmp.

4. From Openvas, generate one or more XML Full Reports and place all of them in in /tmp/ov .

5. Type the following command:   python ovrpts.py

6. The results will exist in ovrpt.py : The results of all XML files will be imported into a delimited text file.

### Options
None

Requirements
------------
Linux OS / Python / untangle

Versions tested:

Linux: 3.14-kali1-686-pae

Python: 2.73

untangle: 1.1.0

Untangle's authors are Christian Stefanescu <chris@0chris.com>, and contributions from <flo@terrorpop.de> . I highly recommend it's usage if you intend to parse XML in a Python script but have never done so before.


Copyright and license
---------------------
openvasrpt is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

openvasrpt is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  

See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with nmapformat. 
If not, see http://www.gnu.org/licenses/.

Contact
-------
* Andy Marks < ajmarcs at yahoo d0t com >
