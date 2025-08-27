# --- Golf Quiz ---

# --- Variables ---
score = 0
total_questions = 20
correct_answers_needed = 10

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

    ("What is another name for the fairway?", 
     ["a) Rough", "b) Short grass", "c) Green", "d) Hazard"], "b"),

    ("What is the term for going 3 under par on a single hole?", 
     ["a) Eagle", "b) Birdie", "c) Albatross", "d) Double Eagle"], "c"),

    ("Who has won the most men's major championships?", 
     ["a) Tiger Woods", "b) Rory McIlroy", "c) Jack Nicklaus", "d) Phil Mickelson"], "c"),

    ("What is the area around the hole called?", 
     ["a) Fringe", "b) Fairway", "c) Green", "d) Bunker"], "c"),

    ("What's the name of the sand area hazard?", 
     ["a) Bunker", "b) Rough", "c) Trap", "d) Hazard"], "a"),

    # True/False
    ("A golf ball must have 336 dimples. (True/False)", ["true", "false"], "false"),

    ("A hole-in-one is also called an ace. (True/False)", ["true", "false"], "true"),

    ("Golf is the only sport to have been played on the moon. (True/False)", ["true", "false"], "true"),

    ("You can carry unlimited clubs in a professional round. (True/False)", ["true", "false"], "false"),

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
    