import os
import sys

class ProjectBuilder(object):
	def __init__(self, argv):
		self.readyToBuild=False
		for arg in Util.splitListByChar(argv,'-')[1:]:
			# project name handling
			if arg[0]=='-p':
				if len(arg)>1:
					self.projectName=arg[1]
					self.readyToBuild=True
				else: print "invalide project name"

			# help handling
			if arg[0]=='-h' or arg[0]=='--help':pass

		if (not self.readyToBuild):print "usage: progen.py -p \"projectName\""



	def build(self):
		self.add_CMakeLists()
		self.add_Folders()
		self.add_AddClass()
		self.add_MainCpp()

	def add_CMakeLists(self):
		text=[
			"cmake_minimum_required(VERSION 2.8)",
			"project({})".format(self.projectName),
			"set(CMAKE_BUILD_TYPE",
			"   #Debug",
			"   Release",
			")",
			"FILE(GLOB_RECURSE SrcFiles \"src/*\")",
			"FILE(GLOB_RECURSE Heders \"inc/*\")",
			"INCLUDE_DIRECTORIES(inc)",
			"FILE(GLOB_RECURSE Resources \"res/*\")",
			"add_custom_target(res SOURCES ${Resources})",
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
	
	@staticmethod
	def add_AddClass():
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
			"		fileListe[0].write('#ifndef {}_H\\n'.format(argv[1].upper()))",
			"		fileListe[0].write('#define {}_H\\n'.format(argv[1].upper()))",
			"		fileListe[0].write('\\n\\n\\n\\n')",
			"		fileListe[0].write('#endif'.format(argv[1].upper()))",
			"		fileListe[1].write('#include \"{}.h\"\\n'.format(argv[1]))",
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
	
	@staticmethod
	def add_Folders(folderNames=["src","inc","res","build"]):
		for forlderName in folderNames:
			if not os.path.exists(forlderName): os.makedirs(forlderName)
	
	@staticmethod
	def add_MainCpp():
		text=[
			"int main(int argc, char* argv[]){\n\n}",
		]
		try:file=open("src/main.cpp", 'w')
		except:
			print "ERROR: unknown"
			return
		for l in text:file.write(l+"\n")
		file.close()



class Util(object):
	@staticmethod
	def splitListByChar(liste,char):
		if len(liste)==1:return liste
		argGoup=[]
		last_startId=0
		for index in [x+1 for x in range(len(liste)-1)]:
			if liste[index][0]==char:
				argGoup.append(liste[last_startId:index])
				last_startId=index
		argGoup.append(liste[last_startId:index+1])
		return argGoup


if __name__ == '__main__':
	builder=ProjectBuilder(sys.argv)
	if builder.readyToBuild:builder.build()