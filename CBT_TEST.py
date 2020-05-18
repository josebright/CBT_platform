# this program will ask multiple choice questions
import time
print('>> ICT BOOT CAMP 2019:' + '\n' + '   CBT TEST v 1.0')
name = input('What is your name?' + '\n' + ': ')
exam_no = input('Examination number' + '\n' + ': ')
print('\n' + 'Welcome ' + name + ' with Examination number of ' + exam_no)
print("Answer the following questions" + '\n')
time.sleep(2)


def check_guess(guess, answer):
    global score
    still_guessing = True
    attempt = 0
    if guess.lower() == answer.lower():
        time.sleep(1.5)
        print('Correct answer')
        score = score + 1
        still_guessing = False
    else:
        if guess.lower() != answer.lower():
            time.sleep(1.5)
            print('Wrong answer')
        if guess.lower() == (''):
            print('No Idea!')


score = 0
guess1 = input('(1). What is the meaning of IYRC? ' + '\n' + 'A. Initiative for Youth Resource Centre ' + '\n' + 'B. Initiative for Young Resource Centre' + '\n'+'C. Initiative Resource Centre' + '\n' + 'Answer:')
check_guess(guess1, 'a')
guess2 = input('\n'+'(2). Who is the director of IYRC? ' + '\n' + 'A. Mr Bukola Idowu ' + '\n' + 'B. Mr Femi Adefila' + '\n'+'C. Mr Osazee Isonarae' + '\n' + 'Answer:')
check_guess(guess2, 'c')
guess3 = input('\n'+'(3). The following are team names at the 2019 BOOT CAMP except? ' + '\n' + 'A. Cyber Fishers ' + '\n' + 'B. Innovators' + '\n'+'C. Coding' + '\n' + 'Answer:')
check_guess(guess3, 'c')
guess4 = input('\n'+'(4). One of these is amongst the topics of the success clinic ' + '\n' + 'A. You are beautiful ' + '\n' + 'B. Self control' + '\n'+'C. Do not be shy' + '\n' + 'Answer:')
check_guess(guess4, 'b')
guess5 = input('\n'+'(5). The person who took the seminar "THINK BIG, START SMALL" is? ' + '\n' + 'A. Mr Femi Olanipekun ' + '\n' + 'B. Mr Femi Adefila' + '\n'+'C. Dr Samuel Adebola' + '\n' + 'Answer:')
check_guess(guess5, 'c')
guess6 = input('\n'+'(6). The topic RUNNING "A SUCCESSFUL LIFE RACE" was treated by? ' + '\n' + 'A. Mr Femi Adefila ' + '\n' + 'B. Mr femi Olanipekun' + '\n'+'C. Mrs Adebayo Isaac' + '\n' + 'Answer:')
check_guess(guess6, 'a')
guess7 = input('\n'+'(7). Which day is the International Youth Day? ' + '\n' + 'A. August 12 ' + '\n' + 'B. August 11' + '\n'+'C. August 22' + '\n' + 'Answer:')
check_guess(guess7, 'a')
guess8 = input('\n'+'(8). What is the name of the head of service in OSUN STATE? ' + '\n' + 'A. Olowogboyega Alabi ' + '\n' + 'B. Oyebade Olowogboyega' + '\n'+'C. Benedict Gboyega Alabi' + '\n' + 'Answer:')
check_guess(guess8, 'b')
guess9 = input('\n'+'(9). How many senators do we have in Nigeria? ' + '\n' + 'A. 108 ' + '\n' + 'B. 109' + '\n'+'C. 119' + '\n' + 'Answer:')
check_guess(guess9, 'b')
guess10 = input('\n'+'(10). Which day did the boys pursue a RAT without planning? ' + '\n' + 'A. August 11 ' + '\n' + 'B. August 12' + '\n'+'C. August 13' + '\n' + 'Answer:')
check_guess(guess10, 'b')
print('\n'+'You scored ' + str(score) + ' out of 10 points.')
if score <= 5:
    print(name.capitalize() + ' You need to put in more effort, ' + '\n' + 'Come back Next Year')
if score > 5:
    print('EXCELLENT!!'+'\n'+ name.capitalize() + ' You are now qualified to graduate'+ " this year's ICT boot camp .")

print('\n'+'ICT boot camp 2019')
print('#thinkmoretalkless.com')
end = input('Press ENTER To ExIT')