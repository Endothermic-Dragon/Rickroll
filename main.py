# Final resolution - just schedule two tasks in task scheduler instead of one

import os
from multiprocessing import Pool

os.chdir(os.path.dirname(os.path.abspath(__file__)))

def run_process(process):
    os.system(f'pyw {process}')

if __name__ == '__main__':
    Pool(processes=2).map(run_process, ["music.py", "volume.py"])