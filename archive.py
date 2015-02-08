import os,shutil
def parse_date(f):
	cutnames=f.split('-')
	if len(cutnames) > 3:
		cutname=cutnames[0]+'-'+cutnames[1]+'-'+cutnames[2]
		return cutname

## make directories
PICS='pics'
for f in os.listdir(PICS):
	date=parse_date(f)
	if date != None:
		if not os.path.exists(os.path.join(PICS,date)):
			os.mkdir(os.path.join(PICS,date))
		print os.path.join(PICS,f), os.path.join(PICS,date)
		shutil.move(os.path.join(PICS,f),os.path.join(PICS,date))

## make tar gz file
for d in os.listdir(PICS):
	td=str(os.path.join(PICS,d))
	if os.path.isdir(td):
		print 'tar -cvzf '+td+'.tar.gz '+td
		os.system('tar -cvzf '+td+'.tar.gz '+td)
		os.system('rm -rf '+td)