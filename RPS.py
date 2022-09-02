# Best of 5 game of Rock, Paper, Scissors against the CPU that keeps score

def rock_paper_scissors():
    import random

    name = input('HELLO AND WELCOME TO THE GREATEST ROCK PAPER SCISSORS GAME \n'
                 '............OF ALL TIME!!!!! \n'
                 'ARE YOU READY TO FREAKING RUMBLE??!! \n'
                 "GOOD - HOWEVER, YOU'LL BE PLAYING AGAINST ME, THE CPU, SO BEST OF LUCK...(NOT!) \n"
                 "TO BEGIN PLEASE ENTER YOUR NAME: ")

    print('OKAY THEN ' + name.upper() + ' YOU MUST BE FEELING BRAVE... \n'
                                        'RIGHT...BEST OF 5! TIME TO BEGIN! \n')

    play_count = 0
    user_score = 0
    cpu_score = 0

    while True:
        play = input("Enter 'Rock', 'Paper' or 'Scissors': ")

        cpu_go = random.choice(range(1, 4))
        # 1 is rock, 2 is paper, 3 is scissors

        if play == 'Rock' or play == 'rock':
            if cpu_go == 1:
                print('Rock! \n''I went for Rock too! A draw it is')
                print('The score is ' + name + ':', user_score, 'Me: ', cpu_score)
            if cpu_go == 2:
                print('Paper! \n''Haha! I win!')
                cpu_score += 1
                print('The score is ' + name + ':', user_score, 'Me: ', cpu_score)
            if cpu_go == 3:
                print('Scissors! \n''Noooo! You win')
                user_score += 1
                print('The score is ' + name + ':', user_score, 'Me: ', cpu_score)
            play_count += 1
        elif play == 'Paper' or play == 'paper':
            if cpu_go == 1:
                print('Rock! \n''Damn, I went for rock! You win!')
                user_score += 1
                print('The score is ' + name + ':', user_score, 'Me: ', cpu_score)
            if cpu_go == 2:
                print('Paper! \n''A draw!')
                print('The score is ' + name + ':', user_score, 'Me: ', cpu_score)
            if cpu_go == 3:
                print('Scissors! \n' 'Imma chop you up! I win!')
                cpu_score += 1
                print('The score is ' + name + ':', user_score, 'Me: ', cpu_score)
            play_count += 1
        elif play == "Scissors" or play == 'scissors':
            if cpu_go == 1:
                print('Rock! \n''I went for rock! I win!')
                cpu_score += 1
                print('The score is ' + name + ':', user_score, 'Me: ', cpu_score)
            if cpu_go == 2:
                print('Paper! \n''You win :(')
                user_score += 1
                print('The score is ' + name + ':', user_score, 'Me: ', cpu_score)
            if cpu_go == 3:
                print('Scissors! \n' 'Hmmm both the same, a tie!')
                print('The score is ' + name + ':', user_score, 'Me: ', cpu_score)
            play_count += 1
        else:
            print('That is not a valid move!')

        if user_score < 3 and cpu_score < 3:
            continue
        elif user_score == 3:
            print('That is the end...congratulations you win! :( \n' 'Guess I shall try again another time')
            break
        elif cpu_score == 3:
            print('HAHA I WIN - YOU LOST TO A COMPUTER BRUH')
            break


rock_paper_scissors()
