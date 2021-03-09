Python 3.9.0 (v3.9.0:9cf6752276, Oct  5 2020, 11:29:23) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> def make_all_caps(in_filename, out_filename):
	"""Changes every character in filename to all caps and saves to a new file.
make_all_caps(str,str)->None
Precondition: The files can be opened for reading and writing
"""
	fin=open(in_filename, "r")
	fout=open(out_filename,"w")
	for line in fin:
		fout.write(line.upper())
		fin.close()
		fout.close()

		
>>> make_all_caps("lets_write.txt","text_caps.txt")
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    make_all_caps("lets_write.txt","text_caps.txt")
  File "<pyshell#11>", line 8, in make_all_caps
    for line in fin:
ValueError: I/O operation on closed file.
>>> 
KeyboardInterrupt
>>> f=open("Lea_DANG-resume.docx","r")
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    f=open("Lea_DANG-resume.docx","r")
FileNotFoundError: [Errno 2] No such file or directory: 'Lea_DANG-resume.docx'
>>> 
KeyboardInterrupt
>>> f=open("lets_write.txt","w")
>>> f.write("Im writing in the file\n")
23
>>> text=["look","more","words"]
>>> for word in text:
	f.write(word)

	
4
4
5
>>> f.close()
>>> f=open("Lets_write.txt","w")
>>> text=["many, many\n","lines\n","are\n","inserted\n","easily\n","this way!"]
>>> f.writelines(text)
>>> f.close()
>>> 
>>> def make_all_caps(in_filename,out_filename):
	"""Changes every character in filename to all caps and saves to a new file.
make_all_caps(str,str)->None
Precondition: The files can be opened for reading and writing
"""
	fin=open(in_filename, 'r')
	fout=open(out_filename, 'w')
	for line in fin:
		fout.write(line.upper())
		fin.close()
		fout.close()

		
>>> 