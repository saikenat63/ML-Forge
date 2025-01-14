import os
import subprocess as sp
import time

file = "/home/c3ilab/Documents/lebc/super_resolution_model.weights.keras"
i = 1
while True:
    if os.path.isfile(file):

        cmd = [
            "mv", file, f"{file}_{i}"
        ]
        res = sp.run(cmd)
        print(res.stdout)
        print(res.stderr)
        

        cmd = [
            "git", "add", ".",
        ]
        res = sp.run(cmd)
        print(res.stdout)
        print(res.stderr)
        
        cmd = [
            "git", "commit", "-m", f"add {i}th model",
        ]
        res = sp.run(cmd)
        print(res.stdout)
        print(res.stderr)
        
        cmd = [
            "git", "push",
        ]
        res = sp.run(cmd)
        print(res.stdout)
        print(res.stderr)
        
        i += 1
        
    time.sleep(10)