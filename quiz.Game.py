def main():
    print("Welcome to the Quiz Game ")

    playing = input("Do you want to play? Y/N: ")

    if playing.lower() != 'y':
         quit_game()

    print("Great! Let's begin.")
    
    questions = [
    ("What does CPU stand for? ", "central processing unit"),
    ("What does GPU stand for? ", "graphics processing unit"),
    ("What does RAM stand for? ", "random access memory")
    ]
    
    score = conduct_quiz(questions)
    display_results(score, len(questions))

  
    def quit_game():
        print("Thank you for considering playing the Quiz Game. Goodbye!")
        exit()  
    
    
    def conduct_quiz(questions):
        score = 0 
        for question , correct_answer in questions:
            answer = input(question).lower()
            if answer == correct_answer:
                print("Correct :) ")
                score += 1
            else:
                print("Incorrect :( ")
        return score
        
        
    def display_results(score, total_questions):
        print(f"You got {score} out of {total_questions} questions correct!")
        percentage = (score / total_questions) * 100
        print(f"You scored {percentage:.2f}%.")
        
    if __name__ == "__main__":
        main()
        