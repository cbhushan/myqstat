#!/usr/bin/env
import os
import xml.etree.ElementTree as ET
import subprocess

def printSingleJobsDetails(t):
    f = os.popen('qstat -x')
    tree = ET.parse(f)
    root = tree.getroot()
    print "Job_Id   walltime state     nodes       Job_Name"
    print "------   -------- ----- --------------- --------------------------"
    for job in root:
        print job.find('Job_Id').text, " ",
        print job.find('resources_used').find('walltime').text, " ",
        print job.find('job_state').text, " ",
        print job.find('Resource_List').find('nodes').text, " ",
        print job.find('Job_Name').text


def myqstat(t):
#    p = os.popen('qstat -x')

    p = subprocess.Popen(['ls', '-1'], stdout=subprocess.PIPE)
    lines = p.communicate()[0].splitlines()
    for i in range(0,len(lines)):
        print lines[i]

# make this file usable as a script as well
if __name__ == "__main__":
    import sys
    myqstat(str(sys.argv[0]))
