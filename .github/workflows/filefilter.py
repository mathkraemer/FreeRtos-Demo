import os

print(os.environ['CHANGESET_FILES'])

with open('changeset-files.lst', 'w') as csf:
   for f in os.environ['CHANGESET_FILES'].split(' '):
        if f.endswith('.c') or f.endswith('.cpp'):
             print('Adding', f, 'to scan file list')
             print(f, file=csf)

