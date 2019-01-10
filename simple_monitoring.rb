def mean array
	sum = 0.0
	array.each { |item| sum += item.to_f }
	return sum / array.size
end
# Available options: 0-255
system 'echo 0 > /sys/kernel/debug/tegra_fan/target_pwm'
# https://developer.ridgerun.com/wiki/index.php?title=Nvidia_TX2_NVP_model
system 'nvp model -m 1'
tests_running = false
while tests_running != true do
	pid_file = `ps -ef | grep "run_all.py" | awk "{print $2}"`
	tests_running = true if pid_file.lines.count > 2
end
puts "\n\n****************************************\n** Process Found. Monitoring Started! **\n****************************************\n\n"
system 'sudo /home/ubuntu/tegrastats >> tegrastats_output.txt &'
while tests_running do
	system 'cat /sys/bus/i2c/drivers/ina3221x/0-0041/iio:device1/in_current0_input >> power_consumption.txt'
	sleep 0.33
	pid_file = `ps -ef | grep "run_all.py" | awk "{print $2}"`
	tests_running = false if pid_file.lines.count <= 2
end
# puts "\n*************************************************\n** Monitoring finished. Data analysis started! **\n*************************************************\n"
system "killall /home/ubuntu/tegrastats"
ram_usage = []
cpu_usage = []
gpu_usage = []
temperature = []
power_consumption = []
File.open('power_consumption.txt', 'r') do |file|
	while line = file.gets
		# Power Consumption
		power_consumption << line.to_f
	end
end
File.open('tegrastats_output.txt', 'r') do |file|
	while line = file.gets
		# RAM Usage
		ram_usage << line.split[1].gsub('/', ' ').split[0].to_i
		# CPU Usage
		core_1 = line.split[5].gsub('[', '').gsub(']', '').gsub(',', ' ').split[0].gsub('%', ' ').split[0].to_i
		core_2 = line.split[5].gsub('[', '').gsub(']', '').gsub(',', ' ').split[1].gsub('%', ' ').split[0].to_i
		core_3 = line.split[5].gsub('[', '').gsub(']', '').gsub(',', ' ').split[2].gsub('%', ' ').split[0].to_i
		core_4 = line.split[5].gsub('[', '').gsub(']', '').gsub(',', ' ').split[3].gsub('%', ' ').split[0].to_i
		core_5 = line.split[5].gsub('[', '').gsub(']', '').gsub(',', ' ').split[4].gsub('%', ' ').split[0].to_i
		core_6 = line.split[5].gsub('[', '').gsub(']', '').gsub(',', ' ').split[5].gsub('%', ' ').split[0].to_i
		cpu_usage << ((core_1 + core_2 + core_3 + core_4 + core_5 + core_6) / 6)
		# GPU Usage
		gpu_usage << line.split[9].to_i
		# Temperature
		# If nvp model = 0, then split has to access position 24 instead of 19
		temperature << line.split[19].gsub('thermal@', '').gsub('C', '').to_f
	end
end
puts "RAM Usage: #{mean ram_usage}"
puts "CPU Usage: #{mean cpu_usage}%"
puts "GPU Usage: #{mean gpu_usage}"
puts "Temperature: #{mean temperature}ºC"
puts "Power Consumption: #{mean power_consumption}mA"
system "rm power_consumption.txt && rm tegrastats_output.txt"
