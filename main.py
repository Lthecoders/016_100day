intro = "fill in the blank Lyrics!"
print(intro.title())
print("--------------------------\n")
print("------> YOUR NUMBER OF ATTEMPTS WILL BE NOTE DOWN <--------.\n")
print(
    "type in the following blank lyrice, see if you're as cool JUSTIN BIBER fan as me.😏🧐"
)

attemt = 0
while True:
  print("\033[34m",
        "\nif you ever ____ on without me, i need to make sure you ____\n",
        "\033[0m")
  user_ans_1 = input(
      "what you think would be the 1st fill in the blank answer?\n---> ")
  user_ans_2 = input(
      "\nwhat you think would be the 2nd fill in the blank answer?\n---> ")
  if user_ans_1 == "move" and user_ans_2 == "know":
    print("\033[32m", "\n\nwell done,🥳🥳\nfinaaly a JB fan like me spotted.",
          "\033[0m")
    attemt += 1
    break
  else:
    print(
        "\033[31m",
        "\nwrong try again😥😕\nmake sure you fill both the blanks correctly and in lowerCase",
        "\033[0m")
    print(
        "\033[31m",
        "make sure you do not put any space in between the text as your input in 1st as well as 2nd fill in the blank",
        "\033[0m")
    attemt += 1

if attemt > 1:

  print(
      f"\n-----> you took {attemt} attempts to answer the correct fill in the blank 😏😁 <-----"
  )
else:
  print(
      f"\n-----> you took {attemt} attempt to answer the correct fill in the blank 😍<-----"
  )
