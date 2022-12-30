# Author  : zhai1xiao
# Date    : 2022-12-29
# Function: Call shell commend with python
#           record the RUN TIME and MEMORY USED based on psutil

import time, os, sys
import pandas as pd
from ProcessTimer import ProcessTimer

if __name__ == '__main__':
    # list the dir file
    # filename = os.listdir("/home/zqzhaiyixiao/TPRA/23s_simu/raw_data/g1")
    dir_path = sys.argv[1]
    filename = os.listdir(dir_path)
    return_code_list = []
    run_time_list = []
    max_vms_memory_list = []
    max_rss_memory_list = []
    for i in filename:
        #I am executing "make target" here
        # ptimer = ProcessTimer(['~/software/WEBSITE/Unix\ Binary/./ReformAlign -i ' + dir_path + '/' + i + ' -o test.fas ' + '-a /home/zqzhaiyixiao/TPRA/23s_simu/' + i + '/' + i + '_kalign3.fasta'])
        ptimer = ProcessTimer(['mafft --retree 1 ' + dir_path + '/' + i + ' > /home/zqzhaiyixiao/TPRA/mt_like/' + i + '/' + i + '_mafft.fasta'])

        try:
            ptimer.execute()
            #poll as often as possible; otherwise the subprocess might 
            # "sneak" in some extra memory usage while you aren't looking
            while ptimer.poll():
                time.sleep(.5)
        finally:
            #make sure that we don't leave the process dangling?
            ptimer.close()
        return_code_list.append(ptimer.p.returncode)
        run_time_list.append(ptimer.t1 - ptimer.t0)
        max_vms_memory_list.append(ptimer.max_vms_memory / (1024 * 1024))
        max_rss_memory_list.append(ptimer.max_rss_memory / (1024 * 1024))
        # print('return code:',ptimer.p.returncode)
        # print('time:',ptimer.t1 - ptimer.t0)
        # print('max_vms_memory:' + str({ptimer.max_vms_memory / (1024 * 1024)}) + " MB")
        # print('max_rss_memory:' + str({ptimer.max_rss_memory / (1024 * 1024)}) + " MB")
    reformalign_info = pd.DataFrame(filename, columns=['filename'])
    reformalign_info = pd.concat([reformalign_info, pd.DataFrame(return_code_list,columns=['return code'])],axis=1)
    reformalign_info = pd.concat([reformalign_info, pd.DataFrame(run_time_list,columns=['run time'])],axis=1)
    reformalign_info = pd.concat([reformalign_info, pd.DataFrame(max_vms_memory_list,columns=['max vms memory'])],axis=1)
    reformalign_info = pd.concat([reformalign_info, pd.DataFrame(max_rss_memory_list,columns=['max rss memory'])],axis=1)
    reformalign_info.to_csv("mt_like_mafft.csv")
