import os

# -------------------------------
# Question Database
# -------------------------------

questions = {

    "Python": [

        {
            "question": "Which keyword is used to define a function in Python?",
            "options": ["A. function", "B. define", "C. def", "D. fun"],
            "answer": "C"
        },

        {
            "question": "Which data type stores True or False?",
            "options": ["A. int", "B. bool", "C. string", "D. float"],
            "answer": "B"
        },

        {
            "question": "Which loop is used when the number of iterations is unknown?",
            "options": ["A. for", "B. while", "C. do while", "D. switch"],
            "answer": "B"
        },

        {
            "question": "Which symbol is used for comments?",
            "options": ["A. //", "B. <!--", "C. #", "D. **"],
            "answer": "C"
        },

        {
            "question": "Python is a ______ language.",
            "options": ["A. Compiled", "B. Interpreted", "C. Machine", "D. Assembly"],
            "answer": "B"
        }

    ],

    "Computer Science": [

        {
            "question": "CPU stands for?",
            "options": [
                "A. Central Processing Unit",
                "B. Computer Processing Unit",
                "C. Central Program Unit",
                "D. Control Processing Unit"
            ],
            "answer": "A"
        },

        {
            "question": "RAM is:",
            "options": [
                "A. Permanent Memory",
                "B. Temporary Memory",
                "C. Cache",
                "D. Hard Disk"
            ],
            "answer": "B"
        },

        {
            "question": "Which data structure follows FIFO?",
            "options": [
                "A. Stack",
                "B. Queue",
                "C. Tree",
                "D. Graph"
            ],
            "answer": "B"
        },

        {
            "question": "HTML is used for?",
            "options": [
                "A. Database",
                "B. Programming",
                "C. Web Pages",
                "D. Networking"
            ],
            "answer": "C"
        },

        {
            "question": "Binary numbers use:",
            "options": [
                "A. 0-9",
                "B. 0-7",
                "C. 0 & 1",
                "D. 1-9"
            ],
            "answer": "C"
        }

    ],

    "General Knowledge": [

        {
            "question": "Capital of India?",
            "options": [
                "A. Mumbai",
                "B. Delhi",
                "C. Chennai",
                "D. Kolkata"
            ],
            "answer": "B"
        },

        {
            "question": "Largest planet?",
            "options": [
                "A. Earth",
                "B. Mars",
                "C. Jupiter",
                "D. Saturn"
            ],
            "answer": "C"
        },

        {
            "question": "National animal of India?",
            "options": [
                "A. Lion",
                "B. Tiger",
                "C. Elephant",
                "D. Peacock"
            ],
            "answer": "B"
        },

        {
            "question": "Who invented the light bulb?",
            "options": [
                "A. Newton",
                "B. Einstein",
                "C. Edison",
                "D. Tesla"
            ],
            "answer": "C"
        },

        {
            "question": "How many continents are there?",
            "options": [
                "A. 5",
                "B. 6",
                "C. 7",
                "D. 8"
            ],
            "answer": "C"
        }

    ]
}

# -------------------------------
# Functions
# -------------------------------

def start_quiz():

    os.system("cls" if os.name == "nt" else "clear")

    print("=" * 50)
    print("      GENERAL KNOWLEDGE QUIZ")
    print("=" * 50)

    name = input("Enter Your Name : ")

    print("\nChoose Category")

    print("1. Python")
    print("2. Computer Science")
    print("3. General Knowledge")

    choice = input("Enter Choice : ")

    if choice == "1":
        category = "Python"

    elif choice == "2":
        category = "Computer Science"

    elif choice == "3":
        category = "General Knowledge"

    else:
        print("Invalid Choice")
        return

    score = 0

    print("\nStarting Quiz...\n")

    for q in questions[category]:

        print(q["question"])

        for option in q["options"]:
            print(option)

        ans = input("Your Answer : ").upper()

        if ans == q["answer"]:
            print("Correct\n")
            score += 1

        else:
            print("Wrong")
            print("Correct Answer :", q["answer"])
            print()

    total = len(questions[category])

    return name, category, score, total


# -------------------------------
# Main
# -------------------------------

result = start_quiz()

if result:

    name, category, score, total = result

    print("=" * 50)
    print("Quiz Completed")
    print("=" * 50)

    print("Name :", name)
    print("Category :", category)
    print("Score :", score, "/", total)
