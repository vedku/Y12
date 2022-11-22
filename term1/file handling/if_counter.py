if_total = 0
with open ("if.txt", "r") as whole_file:
   for line in whole_file:
       if "if" in line.lower():
           if_total += 1
print(if_total)

mam_total = 0
with open ("mam.txt", "r") as meow_file:
    for line in meow_file:
        if "if" in meow_file:
            mam_total += 1
print(mam_total)

if mam_total > if_total:
    print("The mam file has more instances of the word if than the if file")
else:
    print("The if file has more instances of the word if than the mam file")
