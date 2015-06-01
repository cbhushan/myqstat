#!/usr/bin/python
import os
import xml.etree.ElementTree as ET
import subprocess
from math import floor, fmod

def printSingleJobsDetails(id):
    p = subprocess.Popen(['qstat', '-f', '-x', id], stdout=subprocess.PIPE)
    output = p.communicate()[0].splitlines()
    job = ET.fromstring(output[0])[0]


    walltime = job.find('Resource_List').find('walltime').text
    s = walltime.split(":")
    walltime_sec = int(s[0])*3600 + int(s[1])*60 + int(s[2])


    if job.find('Walltime')!=None:
        s = walltime_sec - int(job.find('Walltime').find('Remaining').text)
        secs = s%60
        mins = floor(s/60)
        if mins>60:
            hrs = int(floor(mins/60))
            mins = fmod(mins,60)
        else:
            hrs = 0
        used_time = "%02d:%02d:%02d" % (hrs, mins, secs)

    else:
        used_time = '--:--:--'

    print id, " ",
    print job.find('job_state').text, " ",
    print job.find('Resource_List').find('nodes').text,
    print job.find('Resource_List').find('vmem').text,
    print walltime, " ",
    print used_time, " ",
    print job.find('Job_Name').text, "\t",
    print job.find('queue').text


def myqstat(t):
    user = os.environ['USER']

    proc1 = subprocess.Popen(['qstat', '-u', user], stdout=subprocess.PIPE)
    proc2 = subprocess.Popen(['grep', user],stdin=proc1.stdout, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    proc1.stdout.close() # Allow proc1 to receive a SIGPIPE if proc2 exits.

    lines = proc2.communicate()[0].splitlines()

    print "Job_Id   state        Resources        Used time          Job_Name              Queue"
    print "------   -----  --------------------   ---------  ------------------------ -------------"
    for i in range(0,len(lines)):
        printSingleJobsDetails(lines[i][:8])

# make this file usable as a script as well
if __name__ == "__main__":
    import sys
    myqstat(str(sys.argv[0]))
