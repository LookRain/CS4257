import os

features = []

for filename in os.listdir('./signatures/'):
  if "DS" not in filename:
    
    filepath = './signatures/' + filename
    with open(filepath, 'r') as fp:  
      # print(filename)
      line = fp.readline()
      cnt = 1
      total_size = 0
      while line:
        words = line.split()

        # print(words[-2])
        size = int(words[-2])
      
        total_size += size
      
        # print("totalsize {}".format(total_size))
        line = fp.readline()
      print("total size: " + str(total_size) + "\t" + filename)
 