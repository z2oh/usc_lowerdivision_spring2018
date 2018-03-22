# Test the Solutions to the problem to make sure that they match.
# Input Constraints:
#   Length of Court
#   Width of Court
#   Start Position
#   Starting Direction
#   Player Hits
import subprocess
import os
import sys

# Check Parameters
if len(sys.argv) < 5:
  sys.exit("Check Parameters: {Length, Width, Position, Direction, Hits}")

langs = os.listdir()
print(langs)
cmd_py = ""
cmd_java = ""
proc_py = ""
proc_java = ""
if "python" in langs:
  print("Has Python")
  os.chdir("python")
  cmd_py = ["python","Main.py"]
  print(os.listdir())
  proc_py = subprocess.Popen(cmd_py)
  os.chdir("..")
  
if "java" in langs:
  print("Has Java")
  os.chdir("java")
  cmd_java = ["java","Main"]
  print(os.listdir())
  proc_java = subprocess.Popen(cmd_java)
  os.chdir("..")
  
for i in range(0,4):
  proc_py.communicate(sys.argv[i] + "\n")
  proc_java.communicate(sys.argv[i] + "\n")

