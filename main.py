import subprocess
import os

problem_name = 'Reverse Words'
problem_file = '{}/main.py'.format(problem_name)
test_file = '{}/test.txt'.format(problem_name)
print(subprocess.run(['python3', problem_file, test_file], stdout=subprocess.PIPE, universal_newlines=True).stdout)
