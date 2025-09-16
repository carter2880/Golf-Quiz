# --- Golf Quiz ---

# --- Variables ---
score = 0
total_questions = 20
correct_answers_needed = 13

# --- Questions ---

questions = [
  # --- Multi Choice Questions ---  
    ("What is the standard par for most golf courses?", 
     ["a) 60", "b) 72", "c) 80", "d) 90"], "b"),

    ("What is it called when you score 1 under par on a hole?", 
     ["a) Eagle", "b) Birdie", "c) Bogey", "d) Albatross"], "b"),

    ("What club is usually used to tee off on a par 5?", 
     ["a) Putter", "b) Wedge", "c) Driver", "d) 9-iron"], "c"),

    ("Which major is played at Augusta National?", 
     ["a) The Open", "b) PGA Championship", "c) US Open", "d) The Masters"], "d"),

    ("What does a handicap represent in golf?", 
     ["a) Age of golfer", "b) Skill level", "c) Course rating", "d) Club size"], "b"),

    ("How many holes are in a full round of golf?", 
     ["a) 9", "b) 12", "c) 18", "d) 21"], "c"),

    ("Which is the lowest score?", 
     ["a) Birdie", "b) Par", "c) Bogey", "d) Eagle"], "d"),

    ("Where was golf invented?", 
     ["a) USA", "b) Scotland", "c) England", "d) Ireland"], "b"),

    ("What's the maximum number of clubs allowed in a golf bag?", 
     ["a) 10", "b) 12", "c) 14", "d) 16"], "c"),

    ("What does PGA stand for?", 
     ["a) Pro Golf Association", "b) Professional Golfers Association", 
      "c) Players Golf Academy", "d) Public Golf Association"], "b"),

    ("What is the maximum time allowed to search for a lost ball under the Rules of Golf?", 
     ["a) 1 minute", "b) 3 minutes", "c) 5 minutes", "d) 10 minutes"], "b"),

    ("What is the term for going 3 under par on a single hole?", 
     ["a) Eagle", "b) Birdie", "c) Albatross", "d) Double Eagle"], "c"),

    ("Who has won the most men's major championships?", 
     ["a) Tiger Woods", "b) Rory McIlroy", "c) Jack Nicklaus", "d) Phil Mickelson"], "c"),

    ("What is the area around the hole called?", 
     ["a) Fringe", "b) Fairway", "c) Green", "d) Bunker"], "c"),

    ("Which golf course is known as the “Home of Golf?", 
     ["a) St Andrews", "b) Pebble Beach", "c) Augusta National", "d) Royal Melbourne"], "a"),

    # True/False
    ("A golf ball must have 336 dimples. (True/False)", ["true", "false"], "false"),

    ("Tiger Woods has won more Masters tournaments than Jack Nicklaus. (True/False)", ["true", "false"], "false"),

    ("Golf is the only sport to have been played on the moon. (True/False)", ["true", "false"], "true"),

    ("Every golf course has 18 holes. (True/False)", ["true", "false"], "false"),

    ("The Ryder Cup is played between Europe and the USA. (True/False)", ["true", "false"], "true"),
]

# --- Start Of Quiz ---
print("Welcome to the Golf Quiz!")
response = input("Do you want to play the quiz? (yes/no): ").strip().lower()
if response == "yes":
    play_game = True
else:
    play_game = False

if not play_game:
    print("Maybe next time. Goodbye!")
    exit()

player_name = input("What is your name? ")
print(f"Hello {player_name}! There are {total_questions} questions. You need at least {correct_answers_needed} correct answers to pass.")

# --- Quiz loop ---
for i in range(total_questions):
    question_number = i + 1
    print(f"\nQuestion {question_number}: {questions[i][0]}")

     # Show options
    for option in questions[i][1]:
        print(option)

    # Get answer
    answer = input("Your answer: ").strip().lower()

     # Check answer
    if answer == questions[i][2]:
        print("✅Correct!")
        score += 1
    else:
        print( f"❌Wrong! The correct answer was: {questions[i][2]}")

    # Bonus check every ∆5 questions
    if question_number % 5 == 0 and question_number != total_questions:
        print(f"--- 🎉 Bonus check: You've completed {question_number} questions, keep going! 🎉 --- ")

# --- Results ---
print("\n Quiz Complete!")
print(f"{player_name}, your final score is {score}/{total_questions}.")

# Pass/Fail
if score >= correct_answers_needed:
    print("🏆 You passed the quiz!")
else:
    print("💔 You didn't pass this time.")

# Percentage
percentage = (score / total_questions) * 100
print(f"That's {percentage:.1f}% correct.")

# --- Play Again Option ---
play_again = input("\nDo you want to play again? (yes/no): ").strip().lower()
if play_again == "yes":
    # Restart the program
    import os, sys
    os.execv(sys.executable, ['python'] + sys.argv) #I used Chatgpt for this line and line above to restart the program
else:
    print("Thanks for playing! Goodbye!")
