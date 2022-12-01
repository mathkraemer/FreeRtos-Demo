import json

scopepaths = False

with open('coverity-results.json') as fin, open('coverity-results2.json', 'w') as fout:
    for line in fin.readlines():
        if line.find('strippedFilePathname') > 0 or line.find('strippedMainEventFilePathname') > 0:
            line = line.replace('\\\\', '/')
        elif line.find('stripped') > 0 and line.find('[]') < 0:
            #print('ent', line)
            scopepaths = True
        elif scopepaths == True and line.find(']') < 0:
            line = line.replace('\\\\', '/')
            #print('in ', line)
        elif scopepaths == True and line.find(']') > 0:
            #print('out', line)
            scopepaths = False

        fout.write(line)
