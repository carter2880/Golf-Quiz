
# --- Variables ---
score = 0
total_questions = 20
correct_answers_needed = 10
GREEN = "\033[92m"
RED = "\033[91m"
RESET = "\033[0m"  #Used ChatGPT to find color codes

# --- Questions ---

easyquiz = [
  # --- Multi Choice Questions ---  
    ("What is the standard par for most golf courses?", 
     ["a) 60", "b) 72", "c) 80", "d) 90", "Enter a/b/c/d"], "b"),

    ("What is it called when you score 1 under par on a hole?", 
     ["a) Eagle", "b) Birdie", "c) Bogey", "d) Albatross", "Enter a/b/c/d"], "b"),

    ("What club is usually used to tee off on a par 5?", 
     ["a) Putter", "b) Wedge", "c) Driver", "d) 9-iron", "Enter a/b/c/d"], "c"),

    ("Which major is played at Augusta National?", 
     ["a) The Open", "b) PGA Championship", "c) US Open", "d) The Masters", "Enter a/b/c/d"], "d"),

    ("What does a handicap represent in golf?", 
     ["a) Age of golfer", "b) Skill level", "c) Course rating", "d) Club size", "Enter a/b/c/d"], "b"),

    ("How many holes are in a full round of golf?", 
     ["a) 9", "b) 12", "c) 18", "d) 21", "Enter a/b/c/d"], "c"),

    ("Which is the lowest score?", 
     ["a) Birdie", "b) Par", "c) Bogey", "d) Eagle", "Enter a/b/c/d"], "d"),

    ("Where was golf invented?", 
     ["a) USA", "b) Scotland", "c) England", "d) Ireland", "Enter a/b/c/d"], "b"),

    ("What's the maximum number of clubs allowed in a golf bag?", 
     ["a) 10", "b) 12", "c) 14", "d) 16", "Enter a/b/c/d"], "c"),

    ("What does PGA stand for?", 
     ["a) Pro Golf Association", "b) Professional Golfers Association", 
      "c) Players Golf Academy", "d) Public Golf Association", "Enter a/b/c/d"], "b"),

    ("What is the maximum time allowed to search for a lost ball under the Rules of Golf?", 
     ["a) 1 minute", "b) 3 minutes", "c) 5 minutes", "d) 10 minutes", "Enter a/b/c/d"], "b"),

    ("What is the term for going 3 under par on a single hole?", 
     ["a) Eagle", "b) Birdie", "c) Albatross", "d) Double Eagle", "Enter a/b/c/d"], "c"),

    ("Who has won the most men's major championships?", 
     ["a) Tiger Woods", "b) Rory McIlroy", "c) Jack Nicklaus", "d) Phil Mickelson", "Enter a/b/c/d"], "c"),

    ("What is the area around the hole called?", 
     ["a) Fringe", "b) Fairway", "c) Green", "d) Bunker", "Enter a/b/c/d"], "c"),

    ("Which golf course is known as the “Home of Golf?", 
     ["a) St Andrews", "b) Pebble Beach", "c) Augusta National", "d) Royal Melbourne", "Enter a/b/c/d"], "a"),

    # True/False
    ("A golf ball must have 336 dimples.", ["Enter true or false"], "false"),
    ("A golf ball must have 336 dimples.", ["Enter T or F"], "f"),

    ("Tiger Woods has won more Masters tournaments than Jack Nicklaus.", ["Enter T or F"], "f"),

    ("Golf is the only sport to have been played on the moon.", ["Enter T or F"], "t"),

    ("Every golf course has 18 holes.", ["Enter T or F"], "f"),

    ("The Ryder Cup is played between Europe and the USA.", ["Enter T or F"], "t"),
]

hardquiz = [
  # --- Harder Multi Choice Questions ---
    ("Which golfer is known as 'The Golden Bear'?", 
     ["a) Arnold Palmer", "b) Jack Nicklaus", "c) Gary Player", "d) Tom Watson", "Enter a/b/c/d"], "b"),

    ("What is the name of the trophy awarded to the winner of The Open Championship?", 
     ["a) Claret Jug", "b) Wanamaker Trophy", "c) Ryder Cup", "d) Masters Trophy", "Enter a/b/c/d"], "a"),

    ("In what year was golf first included in the Olympic Games?", 
     ["a) 1900", "b) 1904", "c) 2016", "d) 2020", "Enter a/b/c/d"], "c"),
    
    ("Who is the only player to win the Masters, U.S. Open, The Open, and PGA Championship in the same year?", 
     ["a) Bobby Jones", "b) Ben Hogan", "c) Jack Nicklaus", "d) Tiger Woods", "Enter a/b/c/d"], "b"),

    ("What is the name of the oldest golf tournament in the world?", 
     ["a) The Masters", "b) The Open Championship", "c) U.S. Open", "d) PGA Championship", "Enter a/b/c/d"], "b"),
   
    ("Which country has produced the most winners of The Open Championship?", 
     ["a) USA", "b) Scotland", "c) England", "d) Ireland", "Enter a/b/c/d"], "b"),

    ("Which major championship did Phil Mickelson win at age 50, becoming the oldest major winner?", 
     ["a) The Masters", "b) U.S. Open", "c) PGA Championship", "d) The Open Championship", "Enter a/b/c/d"], "c"),

    ("Which golf course is famous for its 'Amen Corner'?", 
     ["a) Augusta National", "b) Pebble Beach", "c) Royal Birkdale", "d) Pinehurst No. 2", "Enter a/b/c/d"], "a"),

    ("Which golf course famously features the 'Postage Stamp' - one of the smallest greens in championship golf?", 
     ["a) Royal Troon", "b) Carnoustie", "c) Royal Birkdale", "d) Turnberry", "Enter a/b/c/d"], "a"),

    ("What is the name of the only major played outside the United States?", 
     ["a) The Masters", "b) The Open Championship", "c) PGA Championship", "d) U.S. Open", "Enter a/b/c/d"], "b"),

    ("Which country hosted the first golf tournament at the Olympic Games in the 21st century?", 
     ["a) USA", "b) Brazil", "c) UK", "d) Japan", "Enter a/b/c/d"], "b"),

    ("Which major championship did Jordan Spieth win at age 21?", 
     ["a) The Open Championship", "b) U.S. Open", "c) PGA Championship", "d) The Masters", "Enter a/b/c/d"], "d"),

    ("What is the name of the famous par-3 17th hole at TPC Sawgrass?", 
     ["a) The Island Green", "b) The Devil's Elbow", "c) Hogan's Alley", "d) The Road Hole", "Enter a/b/c/d"], "a"),

    ("Who was the first Japanese male golfer to win a major championship?", 
     ["a) Hideki Matsuyama", "b) Shingo Katayama", "c) Ryo Ishikawa", "d) Isao Aoki", "Enter a/b/c/d"], "a"),

    ("Which golfer won the U.S. Open with a broken leg and torn ACL in 2008?", 
     ["a) Phil Mickelson", "b) Tiger Woods", "c) Brooks Koepka", "d) Rory McIlroy", "Enter a/b/c/d"], "b"),

    # True/False
    ("True or False: The longest recorded hole-in-one in professional golf is over 400 yards.", ["Enter T or F"], "f"),

    ("True or False: In match play, the player with the lowest total strokes wins.", ["Enter T or F"], "f"),

    ("True or False: The Presidents Cup is played every four years.", ["Enter T or F"], "f"),

    ("True or False: The first televised golf tournament was broadcast in the 1950s.", ["Enter T or F"], "t"),

    ("True or False: The 'cut' in a major championship is always set at even par.", ["Enter T or F"], "f"),
]


# Shuffle questions for replayability
import random
random.shuffle(easyquiz)
random.shuffle(hardquiz)

# --- Start Of Quiz ---
print("Welcome to the Golf Quiz!")
response = input("Do you want to play a quiz? (yes/no): ").strip().lower()
if response != "yes":
    print("Maybe next time. Goodbye!")
    exit()

player_name = input("What is your name? ")
print(f"\nHello {player_name}!")

# --- Quiz loop ---
while True:
    difficulty = input("Would you like to play the Easy or Hard quiz? (easy/hard): ").strip().lower()
    if difficulty in ['easy', 'hard']:
        break
    print("Please enter either 'easy' or 'hard'")

# Select quiz based on difficulty
quiz = easyquiz if difficulty == 'easy' else hardquiz

print(f"\nGreat choice {player_name}! You've selected the {difficulty.capitalize()} quiz.")
print(f"There are {total_questions} questions. You need at least {correct_answers_needed} correct answers to pass.")

# Update the quiz loop to use the selected quiz:
for i in range(total_questions):
    question_number = i + 1
    print(f"\nQuestion {question_number}: {quiz[i][0]}")

     # Show options
    for option in quiz[i][1]:
        print(option)

    # Get valid answer
    while True:
        answer = input("Your answer: ").strip().lower()

        # Check if it's a multiple choice question
        if len(quiz[i][1]) > 1:  # More than 1 option means multiple choice
            if answer in ['a', 'b', 'c', 'd']:
                break
            print("Please enter a valid option (a/b/c/d)")
        else:  # True/False question
            if answer in ['t', 'f']:
                break
            print("Please enter either 't' or 'f'")
            

    # Check answer
    if answer == quiz[i][2]:
        print(GREEN + "✅ Correct!" + RESET)
        score += 1
    else:
        print(RED + f"❌ Wrong! The correct answer was: {quiz[i][2]}" + RESET)

       # Bonus check every 5 questions
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

