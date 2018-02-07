import os
import matplotlib.pyplot as plt
import numpy as np
features = []

for filename in os.listdir('./signatures/'):
  if "DS" not in filename:
    
    filepath = './signatures/' + filename
    with open(filepath, 'r') as fp:  
      # print(filename)
      file_out = open('./fingerprints/' + filename, 'w')

      line = fp.readline()
      cnt = 1
      x_ax = np.arange(0,4000,100)
      in_list = [0] * 40
      out_list = [0] * 40

      total_size = 0

      starting_time = 0

      time_stop = 100

      first_words = line.split()
      first_time = first_words[0].split(':')
      first_time_converted = int(first_time[0])*3600+int(first_time[1])*60+float(first_time[2])
      first_time_converted = first_time_converted * 1000000

      starting_time = first_time_converted
      # file_out.write("first: " + str(first_time_converted)+"\n")
      in_size = 0
      out_size = 0
      while line:
        
        words = line.split()
        time = words[0].split(':')
        time_converted = int(time[0])*3600+int(time[1])*60+float(time[2])
        time_converted = time_converted * 1000000
        position_to_write = int((time_converted - starting_time) / 100000)

        if position_to_write < 40:
          size = int(words[-2])
        
          total_size += size

          if words[-1] == "in":
            print("position: " + str(position_to_write) + "in: " + str(size))
            in_list[position_to_write] += size
          if words[-1] == "out":
            print("position: " + str(position_to_write) + "out: " + str(size))
            out_list[position_to_write] += size

          # file_out.write(str(time_converted)+"\n")
          # print(words[-2])
          
        
          # print("totalsize {}".format(total_size))
        line = fp.readline()
      # file_out.write(in_list)
      # file_out.write(in_list)
      plt.plot(x_ax, in_list)
      plt.plot(x_ax, out_list)
      
      plt.savefig(filename+'.png')
      plt.show()
      print("total size: " + str(total_size) + "\t" + filename)
 