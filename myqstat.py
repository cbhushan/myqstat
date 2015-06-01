#!/usr/bin/python
import os
import xml.etree.ElementTree as ET
import subprocess

def printSingleJobsDetails(id):
    p = subprocess.Popen(['qstat', '-f', '-x', id], stdout=subprocess.PIPE)
    output = p.communicate()[0].splitlines()
    root = ET.fromstring(output[0])

    for job in root:
        print id + " ",
        print job.find('job_state').text, " ",
        print job.find('Resource_List').find('nodes').text, " ",
        print job.find('Job_Name').text


def myqstat(t):
    user = os.environ['USER']

    proc1 = subprocess.Popen(['qstat', '-u', user], stdout=subprocess.PIPE)
    proc2 = subprocess.Popen(['grep', user],stdin=proc1.stdout, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    proc1.stdout.close() # Allow proc1 to receive a SIGPIPE if proc2 exits.

    lines = proc2.communicate()[0].splitlines()

    print "Job_Id   walltime state     nodes       Job_Name"
    print "------   -------- ----- --------------- --------------------------"
    for i in range(0,len(lines)):
        printSingleJobsDetails(lines[i][:8])

# make this file usable as a script as well
if __name__ == "__main__":
    import sys
    myqstat(str(sys.argv[0]))
