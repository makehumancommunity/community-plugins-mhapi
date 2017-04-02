#!/usr/bin/python3

import os
import re

files = []

for dirName, subdirList, fileList in os.walk("1_mhapi"):
    for fileName in fileList:
        fileBase, fileExt = os.path.splitext(fileName)
        if fileExt == ".py" and fileBase.startswith("_") and not fileBase.startswith("__"):
            newFile = {}
            newFile["dirName"] = dirName
            newFile["fileBase"] = fileBase
            newFile["functions"] = {}

            with open(os.path.join(dirName,fileName),'r') as f:
                newFile["contents"] = f.readlines()

            files.append(newFile)

classMatch = re.compile('class\s+(.*):')
defMatch = re.compile('\s+def\s+([^_]*):')

for aFile in files:
    
    fn = aFile["fileBase"].replace("_","")
    fn = fn + ".md"
    fn = os.path.join("docs",fn)

    with open(fn,'wt') as f:

        length = len(aFile["contents"])
        i = 0
    
        while i < length:
            currentLine = aFile["contents"][i]
            m = classMatch.match(currentLine)
            if(m):            
                cn = m.group(1).replace("(NameSpace)","")
                f.write("# " + cn + "\n\n")
    
            m = defMatch.match(currentLine)
            if(m):            
                funcName = m.group(1)
                funcName = funcName.replace("self,","")
                funcName = funcName.replace("self","")
                funcName = funcName.replace("( ","(")
                f.write("## " + funcName + "\n\n")
            if '"""' in currentLine:
                currentLine = currentLine.replace('"""','').strip()
                f.write(currentLine + "\n\n")
    
            i = i + 1

