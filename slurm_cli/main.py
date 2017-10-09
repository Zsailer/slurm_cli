
import os
import getpass
import subprocess



def get_running_jobs_by_user(whoiam):
    """Get all jobs running by user."""
    # Build command
    command = ["squeue", "-u", whoiam] 
    
    # output
    output = subprocess.run(command)

    # Print standard output.
    print(output.stdout) 

def kill_running_job_by_user(whoiam):
    """"""
    # Print running jobs for user
    get_running_jobs_by_user(whoiam)

    # Ask for job to kill
    job = input("\nWhich job would you like to kill?\n")

    # Build command
    command = ["scancel", job]
    
    # Kill those jobs
    output = subprocess.run(command)

    #print(output.stdout)
