# myqstat
Because I got annoyed of default qstat output format on our clusters! This python script shows full job-names which contains useful information for my jobs. 

Output from default `qstat` command: 

```
                                                                                  Req'd    Req'd       Elap
Job ID                  Username    Queue    Jobname          SessID  NDS   TSK   Memory   Time    S   Time
----------------------- ----------- -------- ---------------- ------ ----- ------ ------ --------- - ---------
12329841.hpc-pbs.hpcc.  cbhushan    main     pbs_103111_rfMRI   5621     1      8   52gb  01:58:00 R  00:26:50
12329842.hpc-pbs.hpcc.  cbhushan    main     pbs_103111_rfMRI  49138     1      8   52gb  01:58:00 R  00:24:11
12329843.hpc-pbs.hpcc.  cbhushan    main     pbs_103111_rfMRI  26640     1      8   52gb  01:58:00 R  00:19:01
12329853.hpc-pbs.hpcc.  cbhushan    main     pbs_103111_rfMRI    --      1      8   52gb  01:58:00 Q       -- 
12329854.hpc-pbs.hpcc.  cbhushan    main     pbs_103111_rfMRI    --      1      8   52gb  01:58:00 Q       -- 
12329855.hpc-pbs.hpcc.  cbhushan    main     pbs_103111_rfMRI    --      1      8   52gb  01:58:00 Q       -- 
```

Output from `myqstat` script:

```
Job_Id   state        Resources        Used time          Job_Name              Queue
------   -----  --------------------   ---------  ------------------------ -------------
12329841   R   1:ppn=8 52gb 01:58:00   00:26:57   pbs_103111_rfMRI_REST1_LR_2_computeDiceTask.pbs 	main
12329842   R   1:ppn=8 52gb 01:58:00   00:24:18   pbs_103111_rfMRI_REST1_LR_4_computeDiceTask.pbs 	main
12329843   R   1:ppn=8 52gb 01:58:00   00:19:08   pbs_103111_rfMRI_REST1_LR_6_computeDiceTask.pbs 	main
12329853   Q   1:ppn=8 52gb 01:58:00   --:--:--   pbs_103111_rfMRI_REST2_RL_2_computeDiceTask.pbs 	main
12329854   Q   1:ppn=8 52gb 01:58:00   --:--:--   pbs_103111_rfMRI_REST2_RL_4_computeDiceTask.pbs 	main
12329855   Q   1:ppn=8 52gb 01:58:00   --:--:--   pbs_103111_rfMRI_REST2_RL_6_computeDiceTask.pbs 	main
```
