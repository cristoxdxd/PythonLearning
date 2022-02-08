# Reorder the string to RAMO in a print
string1 = 'AMOR'
print(string1[-1]+string1[0]+string1[1]+string1[2])

# Validate the links (starts with ->'https://' & ends with ->'.com')
link1 = 'https://wwww.epn.edu.ec.ecuador' 
link2 = 'https://modemat.com' 
link3 = 'http:/fis.edu.lat' 
if(link1.startswith('https://') & link1.endswith('.com')) : print('link 1 is validated')
if(link2.startswith('https://') & link2.endswith('.com')) : print('link 2 is validated')
if(link3.startswith('https://') & link3.endswith('.com')) : print('link 3 is validated')
