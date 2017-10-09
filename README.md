# Simpler SLURM systems command line interface

A list of command-line shortcuts for a SLURM HPC system.

## commands


List all jobs that I am currently running. This is the same as `squeue -u <user>` 

```
$ q
             JOBID PARTITION     NAME     USER ST       TIME  NODES NODELIST(REASON)
                177605       fat   sample  zsailer  R      32:59      1 n123
```


Kill a job that is currently running. This command gives lists running jobs first, then
asks for JOBID.

```
$ k
             JOBID PARTITION     NAME     USER ST       TIME  NODES NODELIST(REASON)
                177605       fat   sample  zsailer  R      32:59      1 n123

Which job would you like to kill?

$ 177605
```
