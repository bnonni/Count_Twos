#!/bin/bash
#SBATCH --nodelist=node01
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=4
#SBATCH --output=%j_node01.out
#SBATCH --error=%j_node01.err
#SBATCH --partition=nonwulfcluster

python3 CountTwos.py 0 1 50000000
python3 CountTwos.py 50000000 50000001 100000000
python3 CountTwos.py 100000000 100000001 150000000
python3 CountTwos.py 150000000 150000001 200000000
