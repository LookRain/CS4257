'''
https://imgur.com/a/rhFuj
https://www.wired.com/story/age-of-social-credit/
https://icml.cc/Conferences/2017/Videos
https://ds9a.nl/amazing-dna/
https://www.wired.com/story/dont-make-ai-artificially-stupid-in-the-name-of-transparency/
https://www.benthamsgaze.org/2018/01/16/practicing-a-science-of-security/
https://medium.com/mlreview/deep-neural-network-capsules-137be2877d44
https://medium.com/ai%C2%B3-theory-practice-business/understanding-hintons-capsule-networks-part-i-intuition-b4b559d1159b
https://www.torproject.org/
https://en.wikipedia.org/wiki/Panopticon
https://leastauthority.com/blog/mixnet-intro/
https://petsymposium.org/award/winners.php
https://www.coursera.org/learn/probabilistic-graphical-models
https://www.comp.nus.edu.sg/about/depts/cs/research/security/people/
https://en.wikipedia.org/wiki/Liverpool_F.C.
https://en.wikipedia.org/wiki/Privacy
https://www.pdpc.gov.sg/news/press-room/2017/11/pdpc-investigating-complaints-against-school
https://www.wired.com/2016/09/machine-learning-can-identify-pixelated-faces-researchers-show/
https://www.cnnindonesia.com/teknologi/20160418075754-185-124588/waspada-pemendek-url-bisa-undang-malware/
https://www.technologyreview.com/s/601294/microsoft-and-google-want-to-let-artificial-intelligence-loose-on-our-most-private-data/
https://www.technologyreview.com/s/603494/10-breakthrough-technologies-2017-paying-with-your-face/
https://sg.news.yahoo.com/uber-380000-users-singapore-exposed-2016-data-breach-121243067.html
https://www.reuters.com/article/us-yahoo-cyber/yahoo-says-all-three-billion-accounts-hacked-in-2013-data-theft-idUSKCN1C82O1
https://crypto.stanford.edu/~dabo/
https://www.theregister.co.uk/2013/03/01/post_cryptography_security_shamir/
https://www.rsaconference.com/blogs/congressional-votes-on-controversial-surveillance-law-close-door-on-privacy-debateor-do-they
https://users.ece.cmu.edu/~adrian/731-sp04/readings/dcnets.html
https://github.com/frankmcsherry/blog/blob/master/posts/2016-02-03.md
https://blog.cryptographyengineering.com/2012/01/02/very-casual-introduction-to-fully/
https://www.nytimes.com/2017/11/02/magazine/how-facebooks-oracular-algorithm-determines-the-fates-of-start-ups.html
https://www.theguardian.com/technology/2017/apr/13/ai-programs-exhibit-racist-and-sexist-biases-research-reveals
https://cacm.acm.org/news/223100-battling-ai-biases/fulltext
https://cacm.acm.org/magazines/2016/7/204032-why-google-stores-billions-of-lines-of-code-in-a-single-repository/fulltext
https://www.theguardian.com/world/2013/jun/09/edward-snowden-nsa-whistleblower-surveillance
https://askubuntu.com/questions/799184/how-can-i-install-cuda-on-ubuntu-16-04
'''

import subprocess as sub
import sys
import re

link = sys.argv[1]
link_without_https = link[8:]
hostname = link_without_https.split('/')[0]
filename = re.sub(r'\W+', '', link_without_https)


# print(hostname)

newline = '\n'
whitespace = '\t'
out_word = 'out'
in_word = 'in'
local_addr = '192.168'
fh = open(filename, "wb")
# fh.writelines("sdfsdf")
p = sub.Popen(('sudo', 'tcpdump', '-l', 'host', hostname), stdout=sub.PIPE)
for line in p.stdout:
  print(line)
  text = line.split()

  time = text[0]
  # size = text[-1]
  # id_of_direction_char = text.index('>')

  len_string = 'length'
  id_of_length = text.index(len_string.encode('utf-8'))
  size = text[id_of_length+1].replace(':'.encode('utf-8'), ''.encode('utf-8'))

  left = text[2][:7]
  right = text[4]

  fh.write(time)
  fh.write(whitespace.encode('utf-8'))
  fh.write(size)
  fh.write(whitespace.encode('utf-8'))

  if left == local_addr.encode('utf-8'):
    fh.write(out_word.encode('utf-8'))
  else:
    fh.write(in_word.encode('utf-8'))
  fh.write(newline.encode('utf-8'))
fh.close()
# for row in iter(p.stdout.readline, b''):
#   # fh = open("sig1.txt", "w")
#   print(row.rstrip())
#   # fh.writelines(row)   # process here