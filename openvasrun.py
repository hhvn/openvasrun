#
#  Working copy:  It works but looks like a mess right now!  I"ll clean up later after I code and test the task 
#  execution throttling logic.
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
# Requirements: Linux OS / Python / Openvas
#
# Instructions:
#
# 1. Create a directory.
# 2. Download openvasrun.py to the directory.
# 3. Create a text file called target_addresses.txt containing
# the IP addresses to be scanned, one IP per line.  It should 
# be in the same directory as openvasrun.py.
# 4. Ensure the current directory is this newly created 
# directory by typing pwd.
# 5. Run the following command: sudo python openvasrun.py .
#
# Please email me with recommendations for improvements.  I
# tailored this program to my specific needs but want to 
# eventually make it as widely useful as possible.
#
# Feel free to modify the source code on your system, such as
# the ID for the 'Full and Fast' configuration.
#
def process_exists(tst):
    """Check whether pid exists in the current process table."""
    retcode = tst.poll()
    if retcode is None:
       return True
    else:
       return False

def start_process(ip_address):

#
# The following code creates the target and task records and then kicks off the task for a single IP
# 
# The test IP address here to be changed to the variable:

   command_line = " omp --xml=\"<create_target><name>" + ip_address + "</name><hosts>" + ip_address + "</hosts></create_target>\""
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

   print command_line
   p = subprocess.Popen([command_line],
       shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

   lines_iterator = iter(p.stdout.readline, b"")
   already_exists = 'No'
   for line in lines_iterator:
       print line

# Sample Output:
# <create_task_response id="4a2a53aa-5a80-4900-8128-cee5be30f44b" status_text="OK, resource created" status="201"></create_task_response>

#
# Kick off task here:
#

# *&*&*&*& End of task-create-kickoff routine

# The debugf flag essentially displays trace messages to aid in 
# troubleshooting.  It must be 'yes' to show the messages.
#
debugf = 'no'

# All processes are stored in process_array just after they are started.
# This allows for checking if it is still running. We count the number
# of processes in the following variable.                                      
#
max_processes = 8
running_processes = 0
process_array = []
ip_array = []

file = open('target_addresses.txt', 'r')

for line in file:
   ip_array.append([str(line).rstrip(), "Waiting",0])
   start_process(str(line).rstrip())

print ip_array[0]

#
# xxx: The following must be modified to call the opm command with appropriate  parameters.
# 
#
#
#   p = subprocess.Popen(["nmap", str(line)],

#   stdout=subprocess.PIPE)
#   process_array.append(p);
#   running_processes += 1

#
# Wait for all nmap processes started above to complete by counting the number of
# nmap processes which have completed and holding until they reach zero.  The array
# process_array contains information about all started processes.   
#
#sv_running_processes = 0
                                                                               
#while running_processes > 0:
  # Computer the number of processes by looking at all the processes stored in the process_array
  # structure.  The format of that object is defined in the subprocess module.
#    running_processes = 0
#    for s in process_array:    
#        if process_exists(s):
#           running_processes = running_processes + 1

#    if sv_running_processes != running_processes:
  # If the number of running processes has changed, display the value on the screen.
#       print 'Number of running Processes: '+str(running_processes)
#       sv_running_processes = running_processes
  # Sleep for awhile so as not to waste too much system resources rechecking.
#    time.sleep(5)

#
# All scans are now complete and the results are stored as individual files for
# each IP.  To ease the reformatting process, they will now be recombined.  The resultant                                                                      
