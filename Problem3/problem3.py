#log_parser
import re
src_file=open('sample_log.txt','r')
error_file=open("error_file.txt",'w+') #+ for new fle creation if not laready present
seek=0
error_count=0
for i in src_file:
    seek+=1
    if re.search('(?i).*error.*(?i)',i) or re.search('(?i).*warning.*(?i)',i):
        error_file.write("Error/Warning occured at line {}: ".format(seek)+i)
        error_count+=1
error_file.write("\n\n\n***************************************************************************** TOTAL LOG COUNT ({})".format(error_count)+"*************************************************************")

src_file.close()
error_file.close()