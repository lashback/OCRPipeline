import os
import re
import shutil

path = 'parallel_pdfs'
files = os.listdir(path)
for f in files:
	pattern = r'(.*)_(\d+)\.pdf'
	bits = re.findall(pattern, f)[0]
	print(bits)
	zfilled = bits[1].zfill(3)
	print(zfilled)
	os.rename("{}/{}".format(path, f), '{}/{}_{}.pdf'.format(path, bits[0],zfilled))

if not os.path.exists('{}/combined'.format(path)):
	os.mkdir('{}/combined'.format(path))
newfiles = os.listdir(path)
base_list = set()

counter = 0
for f in newfiles:
	if ".pdf" in f:
		print(f)
		pattern = r'(.*)_(\d+)\.pdf'
		bits = re.findall(pattern, f)[0]
		print(bits)
		pdf_base = bits[0]
		base_list.add(pdf_base)
		counter +=1
		# if counter ==20:
		# 	print(base_list)
		# 	break

for i,b in enumerate(base_list):
	print('{} of {}'.format(i,len(base_list)))
	filtered_files = sorted(["{}/{}".format(path,f) for f in newfiles if b in f])
	outfile = '{}/combined/{}.pdf'.format(path,b)
	filtered_String = ' '.join(sorted(filtered_files))
	command = "gs -q -dNOPAUSE -sDEVICE=pdfwrite -sOUTPUTFILE={} -dBATCH {}".format(outfile, filtered_String)
	# print(filtered_String)
	# print(command)
	os.system(command)
	# break