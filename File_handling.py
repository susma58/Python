'''
File: collection of data
Read, write, data, appendd, modify, delete

2 primary file types
- text files (.txt, .csv)
- binary files (non text data, .png, .jpg, .pdf, .mp3)

'''

# open files: open('file name', 'mode')
file = open('/Users/Susma/Documents/Python/Python_course/tuple.txt', 'r')

content = file.read()
print(content)
file.close()

# write: file.write(content) ; file.close()
# with statement; close file automatically; with open('file_name', 'mode) as file_name
# print(file_name.read())

with open('file_path', 'w')
content = input('enter content to write = ')
file.write(content)
print('saved')