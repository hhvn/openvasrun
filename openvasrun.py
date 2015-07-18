import subprocess
import os
import time
import errno
import array
import re
#
# Author: x1x
#
# Date: 07/17/15
#
# Description:  This is a simple program to kick off Openvas
# scans for each IP address in a particular file.  This script
# may greatly increase efficiency of penetration testing when
# very large numbers of hosts are involved.
#
# A child process will be kicked off for each host being
# scanned, and they will all run in parallel.  This script is
# intended to be throttled by a parameter, which specifies
# the maximum number of scans to be running at one time.
#
# At this time, 3 concurrent scans are allowed.  To change,
# search the program for max_concurrent_scans and change
# the code as you see fit.
#
# Requirements: Linux OS / Python / Openvas
#
# Instructions:
# 
# 0.  Ensure you have Openvas running.  It is necessary to
#     create a file called omp.config in your home directory
#     with omp (Openvas Management Service) settings, such as
#
#
# [Connection]
# host=127.0.0.1
# port=9390
# username=uuuuuu
# password=pppppp
#
# where uuuuu is a valid Openvas user (one that can log into
# Greenbone, for example), and pppppp is it's password.
# 
# It is not likely this program will work without that file 
# set up.
#
# 1. Create a directory.
# 2. Download openvasrun.py to the directory.
# 3. Create a text file called target_addresses.txt containing
# the IP addresses to be scanned, one IP per line.  It should 
# be in the same directory as nmapformat.py.  The IP addresses
# should be unique.  It is unknown what will occur if there 
# are duplicates.
# 4. Ensure the current directory is this newly created 
# directory by typing pwd.
# 5. Run the following command: sudo python openvasrun.py .
#
# Please email me with recommendations for improvements.  I
# tailored this program to my specific needs but want to 
# eventually make it as widely useful as possible.
#
# Feel free to modify the source code on your system, such as
# adding and removing flags from the nmap system call.  
#

def start_process(ip_address):
#
# The following code creates the target and task records and then kicks off the task for a single IP
# 
# The test IP address here to be changed to the variable:

   command_line = " omp --xml=\"<create_target><name>" + ip_address + "</name><hosts>" + ip_address + "</hosts></create_target>\""
   if debugf == 'yes':
      print command_line
   p = subprocess.Popen([command_line],
       shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)


   lines_iterator = iter(p.stdout.readline, b"")
   already_exists = 'No'
   for line in lines_iterator:
       if line.find('status="400"') > 0:
          already_exists = 'Yes'
          p = subprocess.Popen(['omp --get-targets'],
              shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

          lines_iterator = iter(p.stdout.readline, b"")
          for line in lines_iterator:
              if line.find(ip_address) > 0:   # The test IP address here to be changed to the variable.
#
# Attempt to create target failed: already exists: Now, grab the ID here from a list of all target records.
#
                 target_id = line[0:36]
       else:
#
# Target record create successful:  Grab the ID from the command line output:
#
          target_id = line[28:64]

#
# Create task here:
#
   command_line = " omp --xml=\"<create_task><name>" + ip_address + "</name><config id='daba56c8-73ec-11df-a475-002264764cea'/><target id='" + \
       target_id + "'/></create_task>\""

   if debugf == 'yes':
      print command_line
   p = subprocess.Popen([command_line],
       shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

   lines_iterator = iter(p.stdout.readline, b"")
   for line in lines_iterator:
       if debugf == 'yes':
          print line
       if line.find('create_task') > 0:
          task_id = line[26:62]
          if debugf == 'yes':
             print task_id

# Sample Output:
# <create_task_response id="4a2a53aa-5a80-4900-8128-cee5be30f44b" status_text="OK, resource created" status="201"></create_task_response>

#
# Kick off task here:
#
   command_line = " omp --xml=\"<start_task task_id='" + task_id + "'/>\""
   if debugf == 'yes':
      print command_line
   p = subprocess.Popen([command_line],
       shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

   lines_iterator = iter(p.stdout.readline, b"")
   already_exists = 'No'
   for line in lines_iterator:
       if debugf == 'yes':
          print line

#
# End End End ---->>> start_process <<<-----
#
###############################################################
#
#
def get_running_processes():
#
# Compute the number of running tasks and the number of tasks 
# to be started.
#
     command_line = "omp --get-tasks"
     if debugf == 'yes':
        print command_line
     p = subprocess.Popen([command_line],
         shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
     lines_iterator = iter(p.stdout.readline, b"")
     scans_running = 0
     for line in lines_iterator:
         if debugf == 'yes':
            print line
         if line.find('Running') > 0 or line.find('Requested') > 0:
            scans_running += 1
     return scans_running
#
# End End End ---->>> get_running_processes <<<-----
#
###############################################################
#
# Begin ---->>> Main program <<<-----
#
# The debugf flag essentially displays trace messages to aid in 
# troubleshooting.  It must be 'yes' to show the messages.
#
debugf = 'no'

# All processes are stored in process_array just after they are started.
# This allows for checking if it is still running. We count the number
# of processes in the following variable.                                      
#
max_concurrent_scans = 3
ip_array = []

file = open('target_addresses.txt', 'r')

for line in file:
   ip_array.append([str(line).rstrip()])

if max_concurrent_scans > len(ip_array):
   max_concurrent_scans = len(ip_array)

running_scans = 0
while running_scans > 0 or len(ip_array) > 0: 
   if running_scans < max_concurrent_scans:
      number_to_kickoff = max_concurrent_scans - running_scans
      if debugf == 'yes':
         print number_to_kickoff
      if len(ip_array) > 0:
         for startloop in range(0,number_to_kickoff):
            ip_address = ip_array[0]
            if debugf == 'yes':
               print ip_array[0]
            del ip_array[0]
            start_process((ip_address)[0])

   running_scans = get_running_processes()
   print 'Number of running Processes: '+str(running_scans)
  # Sleep for awhile so as not to waste too much system resources rechecking.
   time.sleep(2)
print 'All scans complete.'
