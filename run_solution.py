import sys
import subprocess
p = subprocess.getoutput("{} ./adventure.py < game_over.txt".format(sys.executable), encoding="UTF-8")
print(p)
