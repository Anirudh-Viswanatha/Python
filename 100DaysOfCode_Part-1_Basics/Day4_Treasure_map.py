line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input("Where do you want to put the treasure? A1,A2,A3,B1,B2,B3,C1,C2,C3: ") # Where do you want to put the treasure?

letter=position[0].lower()
if letter=="a":
  letter=0
elif letter=="b":
  letter=1
elif letter=="c":
  letter=2

number= int(position[1])-1

map[number][letter]="X"
print(f"{line1}\n{line2}\n{line3}")



------------------------------------------------------

line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input("Where do you want to put the treasure? A1,A2,A3,B1,B2,B3,C1,C2,C3: ") # Where do you want to put the treasure?

letter=position[0].lower()
abc = ["a", "b", "c"]
letter_index=abc.index(letter)

number= int(position[1])-1

map[number][letter_index]="X"
print(f"{line1}\n{line2}\n{line3}")

