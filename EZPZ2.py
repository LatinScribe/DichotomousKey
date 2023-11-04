"""Updated version"""
import os

user_correct = 0
questions_num = 0
# HERE IS THE FIX
n = 0

questions_list = [[
    'Which direction does the sun rise?: ', 'North', 'South', 'East', 'West',
    'East'
],
                  [
                      'Who invented the light bulb?: ', 'Thomas Edison',
                      'Alexander Graham Bell', 'Barack Obama',
                      'Justin Trudeau', 'Thomas Edison'
                  ],
                  [
                      'Which planet is closest to the sun?: ', 'Venus',
                      'Mercury', 'Earth', 'Mars', 'Mercury'
                  ],
                  [
                      'When was the first iPhone released?: ', '2007', '2008',
                      '2009', '2010', '2007'
                  ],
                  [
                      'How many molecules of oxygen does ozone have?: ', '1',
                      '2', '3', '4', '3'
                  ]]

for row in questions_list:
    print(row[0])
    questions_num += 1
    for i in range(1, 5):
        print(str(i) + ': ' + row[i])
    answer = input('Please select 1, 2, 3, or 4: ')
    while not answer.isdigit() or int(answer) > len(row) - 1:
        print('Invalid answer. Select an option between 1 and 4.')
        answer = input('Enter your answer: ')
    answer = int(answer)
    if questions_list[n][answer] == questions_list[n][5]:
        print('Correct!')
        user_correct += 1
        print(
            f"You have answered {user_correct} out of {questions_num} questions correctly."
        )
        user_next = input("Press 'n' to continue. ")
        os.system('clear')
    else:
        print(f"Incorrect. The correct answer was {row[5]}.")
        print(
            f"You have answered {user_correct} out of {questions_num} questions correctly."
        )
        user_next = input("Press 'n' to continue. ")
        os.system('clear')

    # YOU NEED TO INCREMENT THIS
    n += 1

print("All questions have been asked.")
