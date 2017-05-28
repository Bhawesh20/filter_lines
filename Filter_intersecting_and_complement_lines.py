f1 = open('file1.txt')
f2 = open('file2.txt')
outfile_i = open('outfile_intersection.txt', 'w')
outfile_c = open('outfile_complement.txt', 'w')
with f1 as f1, f2 as f2, outfile_i as outfile_i, outfile_c as outfile_c:
    for line1 in f1:
        if line1 in f2:
            print(line1, end='', file=outfile_i)
        f2.seek(0)
        
    f1.seek(0)
    f2.seek(0)
    for line1 in f1:
        if line1 not in f2:
            print(line1,end='',file=outfile_c)
        f2.seek(0)
        
    f1.seek(0)
    f2.seek(0)
    outfile_i.seek(0)
    for line2 in f2:
        if line2 not in f1:
            print(line2,end='',file=outfile_c)
        f1.seek(0)
                
