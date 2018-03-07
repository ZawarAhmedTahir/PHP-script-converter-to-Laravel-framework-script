import os
for filename in os.listdir("files"):
    print(filename)
    F = open("files/"+filename,encoding="utf8")
    names = []
    count = 0
    C = open("updated/"+filename,"w+",encoding="utf8")

    for line in F.readlines():
       #names.append(line.rstrip())
       if(line.find('href="https:')>0):
           str=line.replace('href="','href="{{url('+"'")
           str=str.replace('" rel="',"')}}"+" rel="+'"')
           C.write(str)
          # print(str)
       elif(line.find('href="assets')>0):
           str = line.replace('href="', 'href="{{url(' + "'")
           str = str.replace('" type="', "')}}"+'" type=')
         #  print(str)
           C.write(str)
       elif(line.find('type="text/javascript" ')>0):
           str = line.replace('src="assets','src="'+"{{url('assets")
           str=str.replace('"></script>',"')}}"+'"></script>')
       #    print(str)
           C.write(str)
       else:
           C.write(line)
