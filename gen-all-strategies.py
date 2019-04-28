import os
import subprocess

dir_name = "strategies/"
if not os.path.exists(dir_name):
    os.makedirs(dir_name)

def gen_strategy(num_steps, comprehensive):
    filename = "strategy-"+str(num_steps)+".txt"
    if comprehensive: filename = "comprehensive-"+filename
    with open(dir_name+filename, "w") as file:
        subprocess.run(["python3", "calc-gimkit-strategy.py", "1", "4000000000000000", str(int(comprehensive)), str(num_steps)], stdout=file)

def run_diff(num_steps):
    filename = "strategy-"+str(num_steps)+".txt"
    subprocess.run(["diff", dir_name+filename, dir_name+"comprehensive-"+filename])

for i in range(2, 140):
    gen_strategy(i, False)
    gen_strategy(i, True)
    run_diff(i)
    print("Generated strategy for", i, "steps")