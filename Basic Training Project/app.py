class Exercise:
    def __init__(self, name, calories_per_minute):
        self.name = name
        self.calories_per_minute = calories_per_minute
        self.duration = 0

    def calculate_calories_burned(self):
        return self.duration * self.calories_per_minute

class TrainingProgram:
    def __init__(self):
        self.exercises = []

    def add_exercise(self, exercise):
        self.exercises.append(exercise)

    def start_training(self):
        print("Welcome to the Training Program!")

        while True:
            print("\nSelect an option:")
            print("1. Add Exercise")
            print("2. View Exercises")
            print("3. Exit")

            choice = input("Enter your choice (1, 2, or 3): ")

            if choice == "1":
                self.add_exercise_from_user()
            elif choice == "2":
                self.view_exercises()
            elif choice == "3":
                print("Exiting the Training Program. Goodbye!")
                break
            else:
                print("Invalid choice. Please enter 1, 2, or 3.")

    def add_exercise_from_user(self):
        name = input("Enter the exercise name: ")
        calories_per_minute = float(input("Enter calories burned per minute: "))
        duration = int(input("Enter the duration in minutes: "))

        exercise = Exercise(name, calories_per_minute)
        exercise.duration = duration

        self.add_exercise(exercise)
        print(f"{name} added to the training program.")

    def view_exercises(self):
        if not self.exercises:
            print("No exercises added yet.")
        else:
            print("\nExercises:")
            for i, exercise in enumerate(self.exercises, 1):
                print(f"{i}. {exercise.name} ({exercise.duration} minutes) - Calories Burned: {exercise.calculate_calories_burned()}")

if __name__ == "__main__":
    program = TrainingProgram()
    program.start_training()
