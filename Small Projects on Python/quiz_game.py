quiz = [
    {
        "question": "What is the capital of France?",
        "options": ["a) Berlin", "b) Paris", "c) Rome", "d) Madrid"],
        "answer": "b"
    },
    {
        "question": "Which language is this project written in?",
        "options": ["a) C++", "b) Java", "c) Python", "d) Ruby"],
        "answer": "c"
    },
    {
        "question": "What is 5 + 7?",
        "options": ["a) 10", "b) 11", "c) 12", "d) 13"],
        "answer": "c"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["a) Earth", "b) Venus", "c) Mars", "d) Jupiter"],
        "answer": "c"
    },
    {
        "question": "Who wrote 'Harry Potter'?",
        "options": ["a) J.R.R. Tolkien", "b) J.K. Rowling", "c) George R.R. Martin", "d) Mark Twain"],
        "answer": "b"
    },
    {
        "question": "What is the output of 3 * 2 ** 2 in Python?",
        "options": ["a) 12", "b) 36", "c) 16", "d) 8"],
        "answer": "a"
    },
    {
        "question": "Which data type is immutable in Python?",
        "options": ["a) List", "b) Dictionary", "c) Set", "d) Tuple"],
        "answer": "d"
    },
    {
        "question": "Which country is the Taj Mahal located in?",
        "options": ["a) India", "b) Pakistan", "c) Bangladesh", "d) Nepal"],
        "answer": "a"
    },
    {
        "question": "What is the chemical symbol for water?",
        "options": ["a) H2O", "b) O2", "c) CO2", "d) NaCl"],
        "answer": "a"
    },
    {
        "question": "Which keyword is used to define a function in Python?",
        "options": ["a) func", "b) def", "c) function", "d) define"],
        "answer": "b"
    }
]
score = 0

print("===== QUIZ GAME =====")
for i, q in enumerate(quiz, start=1):
    print(f"\nQ{i}: {q['question']}")
    for option in q["options"]:
        print(option)

    ans = input("Your answer (a/b/c/d): ").lower()
    if ans == q["answer"]:
      print("✅ Correct!")
      score += 1
    else:
        print(f"❌ Wrong! Correct answer: {q['answer']}")
    
    print("\n===== QUIZ OVER =====")
print(f"Your final score: {score}/{len(quiz)}")