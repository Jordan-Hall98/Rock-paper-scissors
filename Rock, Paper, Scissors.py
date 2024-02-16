import random

print ("Welcome to this rock, paper, scissors simulator! ")
name = input("What is your name? ")
print (f"Welcome {name}, to the simulation! You are being challenged by the computer!")



rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


computer = f'''
      ooooooooooooooooooooooooooooooooooooo
      8 \                              .d88
      8  oooooooooooooooooooooooooooood8888
      8  8                             8888    oooooooooooooooo
      8  8                             8888    8              8
      8  8                             8888    8             d8
      8  8             I               8888    8            d88
      8  8          am  better         8888    8           d888
      8  8                             8888    8          d8888
      8  8                             8888    8         d88888
      8  8                             8888    8        d888888
      8  8888oooooooooooooooooooooocgmm8888    8       d8888888
      8 .od88888888888888888888888888888888    8      d88888888
      8888888888888888888888888888888888888    8     d888888888
                                               8    d8888888888
         ooooooooooooooooooooooooooooooo       8   d88888888888
        d                       ...oood8b      8  d888888888888
       d              ...oood888888888888b     8 d8888888888888
      d     ...oood88888888888888888888888b    8d88888888888888
     dood8888888888888888888888888888888888b
'''

person = f'''
           __   
           .-'  '-.       
          /        )    ________________________                           
          |  C   o(    ( I am {name} and I win!)
           \       >    \/  
            )  \  /      ..`'
         .-._ / `'      /////     
        / _    \       ( | /
        |/ )    \\     / _,
        / /      |\   / /
       / /       | \ / /
      (  )       /\ ' /
       \ \      (  `-'
        \ \      Y 
        /\ `-.   |
        |(   ^'  |
        \ \\\\  /
         `-    f|
           |   ||
           |   f/
           j   /
           |   )
           |  |
           /  |
           f  |
           \  |
            | |&
           (   `-._,
            -^-----'
'''

draw_screen = '''
                .,-
                                 .,cc$$$"
                          ,   ,c$$P"'.,,,.              .
                         J' z$$$$$$$$$$$$$$c,.     ,r",JMx
                       ,JF J$$$$$$$$$$$$$$$$$$$$F ,F =MMMMM,
                     . J$hJ$$$$$$$$$$$$$$$$$$$$$ccccr MMMMMM,
                      $$$$$$$$$$$$$$$$$$$$$$$$$$$$$P JMMMMMMb
  .nnx,."""?cc,.      $$$$$$$$$???$$$$$$$$$$$$$$P"",JMP uMMMMr
  MMMMMMMMbn.`?$$$cc,`$$$$$$$??$cc,"?$??$$$$$$"",c,"MP uMMMMMM
  MMMMMMMMMMMb. ?$$$$$$$$$$P"' "$$$c, " .""",  $$$$C  xP")MMMM
, MMMMMMMMMMMMMbx "$$$$$$P',c$c,."$$$$$c,,J$$',$$$$$h.".nMMMMMr
J MMMMMMMMPMMMMMP ,J$$$$" c$$$$$$C`?$$$$$$$$$ $$P"`"??.`MMMMMM>
J `MMMMMMM MMMMP J$$$$$',$$$$$$$$$L $$$$$$$$$ $$ uMMn h `MMMMM
$h 4MMP"MM 4MMP J$$$$$F $$$$" .`"?$.`$$$$$$$$ $' """4b ? MMMMM
<$h 4MMx "'`MM z$$$$$$ J$$P'uMMMn.`$r`$$$$$$$ $      "L ;MMMM
<$$h "MMMn. `",$$$$$$P $$$ -"""44Mx`$ ?$$$$$$.?       M .)MMP
 $$$$.`4MMMMn J$$$$$$F,$$F       "M,?F`$$$$$$h c      P ' "P
 `$$$$h.`"4MM $$$$$$$'J$$F        )h $ $$$$$??-`c      ,c$hcc,
  ?$$$$$$c,`" $$$$$$$ ?$$$        JF,$ $$$$Cr=  '  =J$$$$$$$$$c,
   ?$$$$$$$$c,`$$$$$$,`$$$c       = J',$$$P" .:::`.n."$$$$$$$$$$F
    "$$$$$$$$$.`$$$$$$,."??==  .,cccc,J$".xnn.`` ,MMM $$$$$$$$$$$.
     `$$$$$$$' J$$$$$$$$$Ccc;c$$$$$$$$$P MMMMMMMnMMMP $$$$$$$$$$$P=
       "??"".=$$$$$$$$$$$$$$$$$$$$$$??" JMMMMMMM""P" J$$$$$P"""  .
          -r ,$$$$$$$$$$$$$$$$$$$$$' -."4MMMMM"   M $$$$PP -?$$$.`$c
            z$$$$$$$$$$$$$$$$$$$$$$$$."n.    .    M,`P" zc$c,"$$$.<$h
           <$$$$$$$$$$$$$$$$$$$$$$$$$$c`4b. `:::. `M> ,$$$$$$ $$$"<$$
            $$$$$$$$$$$$$$$$$$$$$$$$$$$h."MMn,,,,nJ" J$$$$$$$ $$$c$$P
           ,$$$$$$$$$$$$$$$$$$$$$$$$$$$$$c.`MMMMP",c$$$$$$$$hc$$$$$P'
           <$???????$$$$$$$$$$$$$$$$$$$$$$h.`"" c$$$$$$$$$$$$$$$$P"
                      ""???$$$$$$$$$$$$$PP$$$$ J$$$$$$$$$$$$$P"'
                     ,J$ccc,.`"""""""'.,,c$$$$ $$$$$$$$$$$P".zc$h
                     $$$$$$$$$$$??$$$$$$$$$$$$c`$$$$$$$$$$cr`$$$$F
                    z$$$$$$$$$$$F<$$??"""""?$$$ ?$$$$$$$$$$$ ?$$$F
                   ,$$$$$$$$$$$$ /"".nJMMMbn."?h`$$$$$$$$$$$L`$$$c
                   J$$$$$$$$$$$' .nMMMMMMMMMMbx. $$$$$$$$$$$$.`$$$h.
                  z$$$$$$$$$$$',JMMMMMMMMMMMMMMM,<$$$$$$$$$$$$.`$$$$c,
                 z$$$$$$$$$$P'uMMMMMMMMMMMMMMMMM>`$$$$$$$$$$$$$.`??$$$c
               ,J$$$$$$$$$$$' MMMMMMMMMMMMMMMMMMM $$$$$$$$$$$$$$c <$$$$h
              ,$$$$$$$$$$$$$$ `$$$$$$$$$$$$$$$$$$$$$$r
           z$$$$$$$$$$$$$cc,`? MMMMMMMMMMMMMMMMMMM ?$$$$$$$$$$$$$$$$$$$$$h
          J$$$$$$$$$$$$$$$$$c  4MMMMMMMMMMMMMMMMMMr`$$$$$$$$$$$$$$$$$$$$$$
          <$$$$$$$$$$$$$$$$$$h. 4MMMMMMMMMMMMMMMMMM ?$$$$$$$$$$$$$$$$$$$$$
          `$$$$$$$$$$$$$$$$$$$$h.`4MMMMMMMMMMMMMMMMb ?$$$$$$$$$$$$$$$$$$$'
           `"$$$$$$$$$$$$$$$$$$$$hc,'"4MMMMMMMMMMMP   ?$$$$$$$$$$$$$$$$L'
             `$$$$$$$$$$$$$$$$$$$$$$$cc,`""PPPP"'      "$$$$$$$$$$$$$?$F
               ?$$$$$$$$$$$$$$$$$$$$$$$$$$cccc,          `?$$$$$$$$P" '
                 `"?$$$$$$$$$$$$$$$$$$$$$$$$$$$c            `""??"'
                     `""??$$$$$$$$$$$$$$$$$$$??$r
                             ?$$$$$$$$$.`$$$$h ?F
                              `$$$$$$$$$.<$$$$h`'
                               `?$$$$$$$'<$$$??
                                 `"???"' ??"'
'''
player_count = 0
computer_count = 0



keep_playing = input("Do you want to begin? Press enter to begin, or type anything else to stop? ").lower()

while keep_playing == "":

    options = ["Rock", "Paper", "Scissors"]



    length_of_list = len(options)-1

    random_number = random.randint(0,length_of_list)

    print ("You can type the word or the first letter of your option. caps lock does not matter e.g Rock or r ")

    user_input = input("Rock, Paper, Scissors... ").lower()

    if user_input == "r":
        user_input = "rock"
    elif user_input == "p":
        user_input = "paper"
    elif user_input == "s":
        user_input = "scissors"
    else:
        print ()

    computer_output = (options[random_number]).lower()

    print (f"You picked {user_input}")

    if user_input == "scissors":
        print (scissors)
    elif user_input == "rock":
        print (rock)
    elif user_input == "paper":
        print (paper)
    else:
        print ()


    print (f"Computer picked {computer_output}")


    if computer_output == "scissors":
        print (scissors)
    elif computer_output == "rock":
        print (rock)
    elif computer_output == "paper":
        print (paper)
    else:
        print ()




    if user_input == "rock" and computer_output == "scissors":
        print ("You win!")
        player_count += 1
        print (f"Your score is {player_count} and the computers score is {computer_count}")
    elif user_input == "rock" and computer_output == "rock":
        print ("Its a draw")
        print (f"Your score is {player_count} and the computers score is {computer_count}")
    elif user_input == "rock" and computer_output == "paper":
        print ("You lose!")
        computer_count += 1
        print (f"Your score is {player_count} and the computers score is {computer_count}")
    else:
        print ()


    if user_input == "paper" and computer_output == "rock":
        print ("You win!")
        player_count += 1
        print (f"Your score is {player_count} and the computers score is {computer_count}")
    elif user_input == "paper" and computer_output == "paper":
        print ("Its a draw")
        print (f"Your score is {player_count} and the computers score is {computer_count}")
    elif user_input == "paper" and computer_output == "scissors":
        print ("You lose!")
        computer_count += 1
        print (f"Your score is {player_count} and the computers score is {computer_count}")
    else:
        print ()


    if user_input == "scissors" and computer_output == "paper":
        print ("You win!")
        player_count += 1
        print (f"Your score is {player_count} and the computers score is {computer_count}")
    elif user_input == "scissors" and computer_output == "scissors":
        print ("Its a draw")
        print (f"Your score is {player_count} and the computers score is {computer_count}")
    elif user_input == "scissors" and computer_output == "rock":
        print ("You lose!")
        computer_count += 1
        print (f"Your score is {player_count} and the computers score is {computer_count}")
    else:
        print ()

    keep_playing = input("Do you want to begin? Press enter to begin, or type anything else to stop? ").lower()
else: 
    print ("")
    print ("")
    print (f"Your final scores are {name} {player_count} and computer {computer_count}")


if player_count > computer_count:
    print ("")
    print ("")
    print ("")
    print (f"{name} won!!! {person}")
elif player_count == computer_count:
    print ("")
    print ("")
    print ("")
    print (f"Wow you drew! Well played {draw_screen} ")
elif computer_count > (player_count + 5):
    print ("")
    print ("")
    print ("")
    print (f"Wow {name}, You got thrashed!!!{computer}")
elif player_count > (computer_count + 5):
    print ("")
    print ("")
    print ("")
    print (f"Wow {name}, You destroyed the computer. Are you AI?!!!{person}")
else:
    print ("")
    print ("")
    print ("")
    print (f"You lost {name}, Humans suck!!!{computer}")