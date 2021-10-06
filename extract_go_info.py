f = open("GO.obo", "r")

list_file = []
for line in f:
   list_file+=[line.strip()]

dict_go = {}

for i in range(len(list_file)):
   line = list_file[i]
   if line.startswith("id:"):
      GO = line
      namespace = list_file[i+2]
      dict_go[GO]=namespace
   if line.startswith("alt_id:"):
      GO_alt=line
      dict_go[GO_alt]=namespace

with open("GO_namespace_alt.txt", 'w') as f: 
    for key, value in dict_go.items(): 
        f.write('%s,%s\n' % (key, value))
