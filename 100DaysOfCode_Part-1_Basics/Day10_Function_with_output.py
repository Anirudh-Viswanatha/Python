def format_name(fname, lname):
  return fname.title() + " " + lname.title()
  
output = format_name("ANI", "VIS")
print(output)

# or

# print(format_name("ANI", "VIS"))


# --------------------------------------
# Other version

# def format_name(fname, lname):
#   fname = fname.title()
#   lname = lname.title()
#   print(f"{fname } {lname}") 

#format_name("ANI", "VIS")
