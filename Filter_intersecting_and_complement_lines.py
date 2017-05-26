f1 = open('file1.txt')
f2 = open('file2.txt')
outfile_i = open('outfile_intersection.txt', 'w')
outfile_c = open('outfile_complement.txt', 'w')
with f1 as f1, f2 as f2, outfile_i as outfile_i, outfile_c as outfile_c:
    for line1, line2 in zip(f1, f2):
        if line1 == line2:
            print(line1, end='', file=outfile_i)
        else:
            print('File 1 -->', line1, end='',file=outfile_c)
            print('File 2 -->', line2, end='',file=outfile_c)
