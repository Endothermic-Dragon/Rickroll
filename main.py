import os
import subprocess

os.chdir(os.path.dirname(os.path.abspath(__file__)))
subprocess.call("pyw threaded_run.pyw")