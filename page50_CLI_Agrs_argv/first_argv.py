from sys import argv
print("Number if CLI args",len(argv))
print("list of CLI args",argv)
print("Each argument")
for x in argv:
    print(x)