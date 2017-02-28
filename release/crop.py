import sys
import re

pdf = sys.stdin.read()

trimboxes = re.findall('^/TrimBox \[(.*)\]$', pdf, re.M)

parts = re.split('/CropBox \[.*\]', pdf)

pdf = parts[0]

for n in range(1,len(parts)):
    pdf += "/CropBox [%s]"%(trimboxes[n-1])
    pdf += parts[n]


sys.stdout.write(pdf)
