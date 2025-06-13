# Which year do you want to check?
Print("Guess if it's Leap Year or Not")
year = int(input("Please entry the year you want to chcek: "))

if year%4==0:
  if year%100!=0:
    print("Leap year")
  else:
    if year%400==0:
      print("Leap Year")
    else:
      print("Not Leap Year")
else:
  print("Not Leap Year")
  