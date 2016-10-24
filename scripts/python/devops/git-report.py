import os
from datetime import date, timedelta
import subprocess

#from modules.procutils import check_output2

fromdate = date.today() - timedelta(1)
chdir("c:/devops/test1")
cmd = ['git', 'log', '--pretty=email', '--after=%s' % (fromdate)]
output = subprocess.check_output(cmd)
print output
