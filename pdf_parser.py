from tika import parser
import os

from pprint import pprint

cwd = os.getcwd()

raw = parser.from_file(cwd + '/recipes/przepisy-1.pdf')

# safe_text = raw.encode('ISO-8859-2', errors='ignore')
safe_text = raw.get('content').replace('\n', ' ').replace('nn+', '').replace('\t+', '')

print('---- safe text----')
pprint(safe_text)
