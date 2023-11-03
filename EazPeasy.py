"""Example of a list based QA program"""

questions_list = [
  ['Which direction does the sun rise?: ', 'North', 'South', 'East', 'West', 'East'],
  ['Who invented the light bulb?: ', 'Thomas Edison', 'Alexander Graham Bell', 'Barack Obama', 'Justin Trudeau', 'Thomas Edison'],
  ['Which planet is closest to the sun?: ', 'Venus', 'Mercury', 'Earth', 'Mars', 'Mercury'],
  ['When was the first iPhone released?: ', '2007', '2008', '2009', '2010', '2007'],
  ['How many molecules of oxygen does ozone have?: ', '1', '2', '3', '4','3']
]
def myfunc():
    for i in range(0, len(questions_list)):
        user_input = input(questions_list[i][0] + "Please choose 1, 2, 3, 4")
        # Assuming they give me 1,2,3,4
        option = int(user_input)
        if questions_list[i][option] == questions_list[i][5]:
            print("correct!")
        else:
            print("Wrong answer genuis!")

    print("All questions have been asked!")

myfunc()
