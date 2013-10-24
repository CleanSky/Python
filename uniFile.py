'''
An example of reading and writing Unicode strings: Writes
a Unicode string to a file in utf-8 and reads it back in.
'''

CODEC = 'utf-8'
File = 'unicode.txt'

hello_out = u'Hello World\n'
bytes_out = hello_out.encode(CODEC)
f = open(File, 'w')
f.write(bytes_out)
f.close()

f = open(File, 'r')
bytes_in = f.read()
f.close()

hello_in = bytes_in.decode(CODEC)
print hello_in,
