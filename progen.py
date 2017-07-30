import os
import sys

class ProjectBuilder(object):
	def __init__(self, argv):
		self.readyToBuild=True
		if len(argv)<2:
			print "usage: progen.py \"projectName\""
			print "you typed :",argv
			self.readyToBuild=False
		else:
			for index in [x+1 for x in range(len(argv)-1)]:
				if argv[index]=="-p":
					if index+1<len(argv):self.projectName=argv[index+1]
					else: print "specify a project name [-p projectName]"
	def build(self):
		self.add_CMakeLists(self.projectName)
	def add_CMakeLists(self,ProjectName):
		text=[
			"cmake_minimum_required(VERSION 2.8)",
			"project({})".format(ProjectName),
			"set(CMAKE_BUILD_TYPE",
			"   #Debug",
			"   Release",
			")",

			"FILE(GLOB_RECURSE SrcFiles \"src/*\")",
			"FILE(GLOB_RECURSE Heders \"inc/*\")",
			"FILE(GLOB_RECURSE Resources \"res/*\")",

			"INCLUDE_DIRECTORIES(inc)",

			"file(COPY ${CMAKE_SOURCE_DIR}/res DESTINATION ${CMAKE_BINARY_DIR})",
			"############################################################################",
			"add_executable(${PROJECT_NAME} ${SrcFiles} ${Heders})",
		]
		try:file=open("CMakeLists.txt", 'w')
		except:
			print "ERROR: unknown"
			return
		for l in text:file.write(l+"\n")
		file.close()
	def add_AddClass(self,):
		text=[
			"import sys",
			"def main(argv):",
			"	if len(argv)<2:",
			"		print \"usage : add_class.py className\"",
			"		print \"you typed :\",argv",
			"	elif len(argv)==2:",
			"		fileNames=[",
			"		\"inc/{}.h\".format(argv[1]),",
			"		\"src/{}.cpp\".format(argv[1])",
			"		]",
			"",
			"		#chk if the file are existing",
			"		for fileName in fileNames:",
			"			try:",
			"				file=open(fileName, 'r')",
			"",
			"				if [file.readline()]!=['']:",
			"					print \"this class is existing or src/inc dir are not existing!\"",
			"					return",
			"			except:pass#not existing",
			"",
			"		#creat them then",
			"		try:fileListe=[open(fileNames[0], 'w'),open(fileNames[1], 'w')]",
			"		except:",
			"			print \"src/inc dir are not existing!\"",
			"			return",
			"",
			"		fileListe[0].write(\"#ifndef {}_H\\n\".format(argv[1].upper()))",
			"		fileListe[0].write(\"#define {}_H\\n\".format(argv[1].upper()))",
			"		fileListe[0].write(\"\\n\\n\\n\\n\")",
			"		fileListe[0].write(\"#endif\".format(argv[1].upper()))",
			"		fileListe[1].write('#include \"{0}\"\\n'.format(fileNames[0]))",
			"		for file in fileListe: file.close()",
			"",
			#"		print \"Remember to add {} and {} to the project files\".format(fileNames[0],fileNames[1])",
			"",
			"",
			"if __name__ == '__main__':",
			"	main(sys.argv)",
		]
		try:file=open("addclass.py", 'w')
		except:
			print "ERROR: unknown"
			return
		for l in text:file.write(l+"\n")
		file.close()
	def add_Folders(self,folderNames=["src","inc","res"]):
		for forlderName in folderNames:
			if not os.path.exists(forlderName): os.makedirs(forlderName)
	def creatPro(self,ProjectName):
		add_CMakeLists(ProjectName)
		add_AddClass()
		addFolders()
	def add_MainCpp(self,):
		pass


def main(argv):
	builder=ProjectBuilder(argv)
	if builder.readyToBuild:builder.build()
	
if __name__ == '__main__':
	main(sys.argv)

