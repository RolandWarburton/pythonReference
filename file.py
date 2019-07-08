filepath = "file_demo.txt"

# simple read
fp = open(filepath)
lines = fp.readlines()
print(lines[0].strip())
print(lines[1].strip())
print(lines[2].strip())
fp.close()

# print the whole file
with open(filepath) as fp:
    for i, line in enumerate(fp):
        print("Line {}: {}".format(i, line.strip()))

# print a line from the file
with open(filepath) as fp:
    result = int(input("which line do you want to print? "))
    for i, line in enumerate(fp):
        if i == result:
            print(line.strip())

# write to the file
with open(filepath, "a") as fp:
    fp.write("\nwrote some text")
