"""
In general programming, we receive a piece of data, and we do something with the data we receive to make it useful.
This could be for statistical analysis, results presentation, gathering metrics to do something useful, or many other reasons.
One of the most common data objects I work with is the file.
Taking the following file as input, execute a program which compiles the following useful metrics from the file:

    The time the job started (Started at Mon Oct 12 16:12:22 2020.)
    The time the job was Terminated (Terminated at Mon Oct 12 16:12:28 2020.)
    the CPU time: (CPU time :                                   2.40 sec.)
    The Max Memory used: (Max Memory :                                 2824 MB)
    The walltime (Terminated time - Start Time)
    Rough Estimate of the efficiciency: CPU Time / walltime (this may require conversion of units)

The program should execute as follows:
gather_stats job_log.txt and it should print the following information:
Walltime: 6s
CPU Time: 2.40s
Max Memory: 2.824G
Efficiency: 0.4

data in file_info.txt of this same package/dir
"""
import sys
import re
from datetime import datetime

## Input formatting
base_indent = '        '
label_start_time = 'Started at '
label_end_time = 'Terminated at '
datetime_format = '%a %b %d %H:%M:%S %Y.'
value_regex = r':[^A-Za-z0-9.-]+'
further_indent = base_indent + '    '

## Output formatting
label_walltime = 'Walltime'
label_cpu_time = 'CPU time'
label_max_memory = 'Max Memory'
label_efficiency = 'Efficiency'

## Intermediate data
data = dict()
output_strings = []


def process_datetime(input_str):
    datetime_str = re.split(' at ', input_str.rstrip(' \n'))[1]
    return datetime.strptime(datetime_str, datetime_format)


def process_value(input_str):
    return re.split(value_regex, input_str.rstrip('\n'))[1]


def process_file(file_name):
    with open(file_name, 'r') as log_file:
        for line in log_file:
            if label_start_time in line:
                data[label_start_time] = process_datetime(line)
            elif label_end_time in line:
                data[label_end_time] = process_datetime(line)
            elif label_cpu_time in line:
                data[label_cpu_time] = process_value(line)
            elif label_max_memory in line:
                data[label_max_memory] = process_value(line)
            # else:
            #     print(line.rstrip('\n'))


def render_data():
    data[label_walltime] = (data[label_end_time] - data[label_start_time]).total_seconds()
    data[label_efficiency] = round(int(re.findall(r'\d', data[label_cpu_time])[0]) / data[label_walltime], 1)


def print_report():
    print(f'{label_walltime}: {data[label_walltime]}s\n'
          f'CPU Time: {data[label_cpu_time]}\n'
          f'{label_max_memory}: {data[label_max_memory]}\n'
          f'{label_efficiency}: {data[label_efficiency]}')


if __name__ == '__main__':
    # log_file_name = sys.argv[1]
    log_file_name = 'file_info.txt'
    process_file(log_file_name)
    render_data()
    print_report()
