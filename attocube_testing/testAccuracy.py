#! /reg/g/pcds/pkg_mgr/release/controls-0.1.8/x86_64-rhel6-gcc44-opt/bin/python

from attocube_test_script import testAccuracy as testAccuracy
from attocube_test_script import home as home
from common.motor import Motor as psmotor
import sys
import csv

# Read in attocubes to be tested and build lists of PVs
stages = []
with open('stages.txt', 'rb') as f:
    reader = csv.reader(f)
    for row in reader:
        stages.append(row[0].strip())

# Define motors and run script
motors = []
for stage in enumerate(stages):
    motors.append(psmotor(stage[1], 'acube%i' % stage[0]))

args = sys.argv
if len(args) == 2:
    index = int(sys.argv[1])
    moves, data = testAccuracy(motors[index])
if len(args) == 3:
    index = int(sys.argv[1])
    step = float(sys.argv[2])
    moves, data = testAccuracy(motors[index], step)

datafile = open('accuracy_results.csv', 'wb')
writer = csv.writer(datafile)
writer.writerow(['Accuracy Test'])
writer.writerow(['Moves'])
writer.writerow(moves)
writer.writerow(['Readbacks'])
writer.writerow(data)