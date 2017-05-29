from itertools import chain
f1 = open('file1.txt','r')
f2 = open('file2.txt','r')
outfile_i = open('outfile_intersection.txt', 'w')
outfile_c = open('outfile_complement.txt', 'w')
with f1 as f1, f2 as f2, outfile_i as outfile_i, outfile_c as outfile_c:
    i = 0
    l = len(f1.readlines())
    f1.seek(0)
    for line1 in chain(f1,f2):
        if i<l:
            if line1 in f2:
                print(line1, end='', file=outfile_i)
            else:
                print(line1,end='',file=outfile_c)
            f2.seek(0)
        else:
            f1.seek(0)
            if line1 not in f1:
                print(line1,end='',file=outfile_c)
        i = i+1
            
