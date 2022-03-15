import re
##phoneRegex = re.compile(r'(\d{3})-(\d{3}-\d{3})')
## phoneRegex = re.compile(r'\d{3}-\d{3}-\d{3}')
phoneRegex = re.compile(r'''(
(\d{1,5}|\+\d{1,3})?
(\s|-|\.)
(\d{3}|\(\d{3}\))
(\s|-|\.)
\d{3}
(\s|-|\.)
\d{4}
(\s*(ext|x|ext.)\s*\d{2,5})?
)''',re.VERBOSE)

mo = phoneRegex.search(input())
print ('phone number is: ')
print(mo.group(1))
## print(mo.groups())