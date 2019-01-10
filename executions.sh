#!/bin/bash
# Disable unnecessary cores and puts the GPU at the lower frequency available
echo 140250000 > /sys/devices/17000000.gp10b/devfreq/17000000.gp10b/max_freq
echo 0 > /sys/devices/system/cpu/cpu1/online
echo 0 > /sys/devices/system/cpu/cpu2/online
echo 0 > /sys/devices/system/cpu/cpu3/online
echo 0 > /sys/devices/system/cpu/cpu4/online
echo 0 > /sys/devices/system/cpu/cpu5/online
# for i in abod cblof fb hbos iforest knn lof mcd; do
for i in hbos cblof iforest knn lof mcd abod; do
	for j in 1 2 3; do
		sudo ruby simple_monitoring.rb &
		sleep 5
		python3 run_all.py $i
		sleep 5
		sudo echo 255 > /sys/kernel/debug/tegra_fan/target_pwm
		sleep 60
		sudo echo 0 > /sys/kernel/debug/tegra_fan/target_pwm
		sleep 60
	done
done
