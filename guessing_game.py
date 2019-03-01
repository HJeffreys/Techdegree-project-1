"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------

For this first project we will be using Workspaces.

NOTE: If you strongly prefer to work locally on your own computer, you can totally do that by clicking: File -> Download Workspace in the file menu after you fork the snapshot of this workspace.

"""


name = input("Welcome! What's your name?: ")
scores = []

def start_game():
    def high_score(x):
        high = x[0]
        for i in x[0:]:
            if i < high:
                high = i
        return high
    import random
    num = random.randint(1,10)
    attempts = int()
    while True:
        num_guess = input('Guess a number between 1-10 {}: '.format(name))
        try:
            num_guess = int(num_guess)
            if num_guess > 10:
                raise ValueError ('Your number must be between 1 - 10!')
            if num_guess < 1:
                raise ValueError ('Your number must be between 1 - 10!')
        except ValueError as err:
            print ('Ooops! We ran into an issue. {}. Please try again:'.format(err))
        else:
            if num_guess == num:
                attempts += 1
                print ('Got it! It took you {} attempts!'.format(attempts))
                scores.append(attempts)
                print ('The high score is - ', high_score(scores))
                again = input('\nWould you like to play again? Y/N: ')
                if again.lower() == 'y':
                    return start_game()
                elif again.lower() == 'n':
                    print ('Thank you for playing {}!'.format(name))
                    break
            if num_guess < num:
                attempts += 1
                print ("It's higher!: ")
                continue
            if num_guess > num:
                attempts += 1
                print ("It's lower!: ")
                continue

start_game()


if __name__ == '__main__':
    # Kick off the program by calling the start_game function.
    start_game()
