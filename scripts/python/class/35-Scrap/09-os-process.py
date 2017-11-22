import subprocess
import os

output_file = "test.txt"

cmd = ["ls", "-a"]
with open(output_file, 'w') as out:
    return_code = subprocess.call(cmd, stdout=out)

out.close()
