import socket
import random
import time
import pickle
import re
from quart import Quart

app = Quart(__name__)

class Parse:
    def __init__(self, interval):
        self.interval = int(interval)

    def parse_ram(self, lookup_table, ram):
        lookup_table['Used RAM (MB)'] = float(ram[0])
        lookup_table['Total RAM (MB)'] = float(ram[1])
        lookup_table['Number of Free RAM Blocks'] = float(ram[2])
        lookup_table['Size of Free RAM Blocks (MB)'] = float(ram[3])
        return lookup_table

    def parse_swap(self, lookup_table, swap):
        lookup_table['Used SWAP (MB)'] = float(swap[0])
        lookup_table['Total SWAP (MB)'] = float(swap[1])
        lookup_table['Cached SWAP (MB)'] = float(swap[2])
        return lookup_table

    def parse_iram(self, lookup_table, iram):
        lookup_table['Used IRAM (kB)'] = float(iram[0])
        lookup_table['Total IRAM (kB)'] = float(iram[1])
        lookup_table['Size of IRAM Blocks (kB)'] = float(iram[2])
        return lookup_table

    def parse_cpus(self, lookup_table, cpus):
        frequency = re.findall(r'@([0-9]*)', cpus)
        lookup_table['CPU Frequency (MHz)'] = float(frequency[0]) if frequency else ''
        for i, cpu in enumerate(cpus.split(',')):
            lookup_table[f'CPU {i} Load (%)'] = cpu.split('%')[0]
        return lookup_table

    def parse_gr3d(self, lookup_table, gr3d):
        lookup_table['Used GR3D (%)'] = float(gr3d[0])
        lookup_table['GR3D Frequency (MHz)'] = float(gr3d[1]) if gr3d[1] else ''
        return lookup_table

    def parse_emc(self, lookup_table, emc):
        lookup_table['Used EMC (%)'] = float(emc[0])
        lookup_table['GR3D Frequency (MHz)'] = float(emc[1])  if emc[1] else ''
        return lookup_table

    def parse_temperatures(self, lookup_table, temperatures):
        for label, temperature in temperatures:
            lookup_table[f'{label} Temperature (C)'] = float(temperature)
        return lookup_table

    def parse_vdds(self, lookup_table, vdds):
        for label, curr_vdd, avg_vdd in vdds:
            lookup_table[f'Current {label} Power Consumption (mW)'] = float(curr_vdd)
            lookup_table[f'Average {label} Power Consumption (mW)'] = float(avg_vdd)
        return lookup_table

    def parse_data(self, line):
        lookup_table = {}

        ram = re.findall(r'RAM ([0-9]*)\/([0-9]*)MB \(lfb ([0-9]*)x([0-9]*)MB\)', line)
        self.parse_ram(lookup_table, ram[0]) if ram else None

        swap = re.findall(r'SWAP ([0-9]*)\/([0-9]*)MB \(cached ([0-9]*)MB\)', line)
        self.parse_swap(lookup_table, swap[0]) if swap else None

        iram = re.findall(r'IRAM ([0-9]*)\/([0-9]*)kB \(lfb ([0-9]*)kB\)', line)
        self.parse_iram(lookup_table, iram[0]) if iram else None

        cpus = re.findall(r'CPU \[(.*)\]', line)
        self.parse_cpus(lookup_table, cpus[0]) if cpus else None

        ape = re.findall(r'APE ([0-9]*)', line)
        if ape:
            lookup_table['APE frequency (MHz)'] = float(ape[0])

        gr3d = re.findall(r'GR3D_FREQ ([0-9]*)%@?([0-9]*)?', line)
        self.parse_gr3d(lookup_table, gr3d[0]) if gr3d else None

        emc = re.findall(r'EMC_FREQ ([0-9]*)%@?([0-9]*)?', line)
        self.parse_emc(lookup_table, emc[0]) if emc else None

        nvenc = re.findall(r'NVENC ([0-9]*)', line)
        if nvenc:
            lookup_table['NVENC frequency (MHz)'] = float(nvenc[0])

        mts = re.findall(r'MTS fg ([0-9]*)% bg ([0-9]*)%', line) # !!!!

        temperatures = re.findall(r'([A-Za-z]*)@([0-9.]*)C', line)
        vdds = None

        if temperatures:
            self.parse_temperatures(lookup_table, temperatures)
            substring = line[(line.rindex(temperatures[-1][1] + "C") + len(temperatures[-1][1] + "C")):]

            vdds = re.findall(r'([A-Za-z0-9_]*) ([0-9]*)\/([0-9]*)', substring)

        else:
            vdds = re.findall(r'VDD_([A-Za-z0-9_]*) ([0-9]*)\/([0-9]*)', line)
        self.parse_vdds(lookup_table, vdds) if vdds else None

        return lookup_table




    def server(self):
        client_socket = socket.socket()
        client_socket.connect(('127.0.0.1', 8000))

        while True:
            data = input()
            output_1 = self.parse_data(data)

            cpu0 = output_1['CPU 0 Load (%)']
            cpu1 = output_1['CPU 1 Load (%)']
            cpu2 = output_1['CPU 2 Load (%)']
            cpu3 = output_1['CPU 3 Load (%)']
            cpu4 = output_1['CPU 4 Load (%)']
            cpu5 = output_1['CPU 5 Load (%)']
            avg_cpu = (float(cpu0) + float(cpu1) + float(cpu2) + float(cpu3) + float(cpu4) + float(cpu5))/6

            output1 = {'time': time.strftime('%I:%M:%S'), 'value' : output_1['Used RAM (MB)']}
            #Randomly RAM generated values for the remaining titans
            output2 = {'time': time.strftime('%I:%M:%S'), 'value' : random.uniform(0.3, 0.4) }
            output3 = {'time': time.strftime('%I:%M:%S'), 'value' : random.uniform(0.3, 0.4) }
            output4 = {'time': time.strftime('%I:%M:%S'), 'value' : random.uniform(0.4, 0.5) }
            output5 = {'time': time.strftime('%I:%M:%S'), 'value' : random.uniform(0.5, 0.6) }
            output6 = {'time': time.strftime('%I:%M:%S'), 'value' : random.uniform(0.6, 0.7) }
            output7 = {'time': time.strftime('%I:%M:%S'), 'value' : random.uniform(0.7, 0.8) }
            output8 = {'time': time.strftime('%I:%M:%S'), 'value' : random.uniform(0.8, 0.9) }
            output9 = {'time': time.strftime('%I:%M:%S'), 'value' : random.uniform(0.9, 1.0) }
            ram_to_send = [output1, output2, output3, output4, output5, output6, output7, output8, output9]


            outputcpu1 = {'time': time.strftime('%I:%M:%S'), 'value' : avg_cpu}
            #Randomly CPU generated values for the remaining titans
            outputcpu2 = {'time': time.strftime('%I:%M:%S'), 'value' : random.uniform(0.3, 0.4) }
            outputcpu3 = {'time': time.strftime('%I:%M:%S'), 'value' : random.uniform(0.3, 0.4) }
            outputcpu4 = {'time': time.strftime('%I:%M:%S'), 'value' :  random.uniform(0.4, 0.5) }
            outputcpu5 = {'time': time.strftime('%I:%M:%S'), 'value' : random.uniform(0.5, 0.6) }
            outputcpu6 = {'time': time.strftime('%I:%M:%S'), 'value' : random.uniform(0.6, 0.7) }
            outputcpu7 = {'time': time.strftime('%I:%M:%S'), 'value' : random.uniform(0.7, 0.8) }
            outputcpu8 = {'time': time.strftime('%I:%M:%S'), 'value' : random.uniform(0.8, 0.9) }
            outputcpu9 = {'time': time.strftime('%I:%M:%S'), 'value' : random.uniform(0.9, 1.0) }
            cpu_to_send = [outputcpu1, outputcpu2, outputcpu3, outputcpu4, outputcpu5, outputcpu6, outputcpu7, outputcpu8, outputcpu9]

            data_to_send = [ram_to_send, cpu_to_send]
            msg = pickle.dumps(data_to_send)
            client_socket.send(msg)
            time.sleep(1)
        


if __name__ == '__main__':
    interval = 1000
    parser = Parse(interval)
    parser.server()
    app.run(port=8080)