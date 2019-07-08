import re

a = r"eggs"

# checks the start and the end
if re.match(a, "and eggs and"):
    print("match found")
else:
    print("no match found")

# searches whole string
if re.search(a, "and eggs and"):
    print("match found")
else:
    print("no match found")

# searches whole string and returns locations
if re.findall(a, "and eggs and eggs"):
    print("match found")
    # get the number of results found
    print(len(re.findall(a, "and eggs and eggs")))
else:
    print("no match found")

# find and replace
mystring = "hi john my name is john"
pattern = r"john"
newstring = re.sub(pattern, "roland", mystring)
print(newstring)

# METACHARACTERS ====================================
pattern = r"aa....bb"
if re.match(pattern, "aatestbb"):
    print("match")
else:
    print("false")

pattern = r"^gr.y$"
if re.match(pattern, "grey"):
    print("match")

# CHARACTER CLASSES / REGULAR EXPRESSIONS ====================================
import re

# pattern for AA1
pattern = r"[A-Z][A-Z][0-9]"

# re.I == flags=re.IGNORECASE
if re.search(pattern, "AA1", re.I):
    print("match")
else:
    print("false")

# eggs bacon bacon bacon... etc
pattern = r"eggs(bacon)*"
if re.match(pattern, "eggs"):
    print("match")
if re.match(pattern, "eggsbacon"):
    print("match")
if re.match(pattern, "eggsbaconbacon"):
    print("match")
if re.match(pattern, "baconeggs"):
    print("match")
# the only time it fails
if re.match(pattern, "bacon"):
    print("match")
else:
    print("false")

# GROUPS ====================================
print("\nGROUPS:")
# bread. eggs forever. bread
pattern = r"bread(eggs)*bread"

# no match
if re.match(pattern, "bread eggs eggs bread"):
    print("match")

if re.match(pattern, "breadeggseggsbread"):
    print("match")

if re.match(pattern, "breadbread"):
    print("match")


print("\nTEST:")
content = "warburtonroland@gmail.com purple"
# \b  [\w.-]    +    @[\w.-]    +    .\w{2,4}  \b
pattern = r"\b[\w.-]+@[\w.-]+.\w{2,4}\b"

# email = re.search(pattern, content, re.I)
email = re.match(pattern, content)
print(email[0])

# for email in emails:
#     print(email)
