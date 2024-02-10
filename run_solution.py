import sys
import subprocess
p = subprocess.getoutput("{} ./adventure.py < solution.txt".format(sys.executable), encoding="UTF-8")
print(p)
