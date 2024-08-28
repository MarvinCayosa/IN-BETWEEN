from tkinter import *
import random
import pygame
from tkinter import messagebox


gui = Tk()
gui.title("IN BETWEEN")
gui.geometry("640x360")
gui.resizable(FALSE, FALSE)

pygame.mixer.init()  # start music

bgm = pygame.mixer.Sound("Komiku_-_12_-_Bicycle.mp3")
bgm.play(loops=-1)
bgm.set_volume(0.2)

canvas = Canvas(gui, width=640, height=360, highlightthickness=0)
canvas.pack()
bg = PhotoImage(file='BG.png')
bg_2 = PhotoImage(file='CONGRATS.png')
card = PhotoImage(file='CARD_BLANK.png')
new_card = PhotoImage(file='THIRDCARD.png')

button1 = PhotoImage(file='DEAL.png')
button2 = PhotoImage(file='NO_DEAL.png')
button3 = PhotoImage(file='button3.png')
button4 = PhotoImage(file='button4.png')
button5 = PhotoImage(file='button5.png')
button6 = PhotoImage(file='lower.png')
button7 = PhotoImage(file='higher.png')
button8 = PhotoImage(file='start.png')
button9 = PhotoImage(file='restart.png')
button10 = PhotoImage(file='New Game.png')
button11 = PhotoImage(file='quit.png')

canvas.create_image(320, 180, image=bg)

global rounds, count, rand1, rand2, rand3, blank_card_1, blank_card_2, blank_card_3
global pocket_money, total, higher, lower, card_3, game_end, bet, card_1, card_2


def three_rounds():
    global rounds, pocket_money
    start["state"] = 'normal'
    rounds5["state"] = 'disable'
    rounds10["state"] = 'disable'

    rounds = 3
    pocket_money = 1000
    money.config(text=str(pocket_money))

    pygame.mixer.music.load("mixkit-select-click-1109.wav")
    pygame.mixer.music.play(loops=0)
    pygame.mixer.music.set_volume(0.3)


def five_rounds():
    global rounds, pocket_money
    start["state"] = 'normal'
    rounds3["state"] = 'disable'
    rounds10["state"] = 'disable'

    rounds = 5
    pocket_money = 5000
    money.config(text=str(pocket_money))

    pygame.mixer.music.load("mixkit-select-click-1109.wav")
    pygame.mixer.music.play(loops=0)
    pygame.mixer.music.set_volume(0.3)


def ten_rounds():
    global rounds, pocket_money
    start["state"] = 'normal'
    rounds5["state"] = 'disable'
    rounds3["state"] = 'disable'

    rounds = 10
    pocket_money = 10000
    money.config(text=str(pocket_money))

    pygame.mixer.music.load("mixkit-select-click-1109.wav")
    pygame.mixer.music.play(loops=0)
    pygame.mixer.music.set_volume(0.3)


def deal():
    global card_3, rounds, count, rand1, rand2, rand3, blank_card_3, pocket_money, total, higher, lower, bet
    reset["state"] = 'normal'
    deal["state"] = 'disable'
    no_deal["state"] = 'disable'

    pygame.mixer.music.load("mixkit-select-click-1109.wav")
    pygame.mixer.music.play(loops=0)
    pygame.mixer.music.set_volume(0.3)

    try:
        bet = int(bet_entry.get())

        if bet > pocket_money:
            status.config(text="Not Enough\n Money!")

            deal["state"] = 'normal'
            no_deal["state"] = 'normal'
            reset["state"] = 'disable'

        else:

            if (rand3 > rand1 and rand3 < rand2) or (rand3 > rand2 and rand3 < rand1):
                status.config(text="You Won!")
                pocket_money += bet

                pygame.mixer.music.load("collect-5930.mp3")
                pygame.mixer.music.play(loops=0)
                pygame.mixer.music.set_volume(0.3)

            else:
                status.config(text="You Lost!")
                pocket_money -= bet

                pygame.mixer.music.load("negative_beeps-6008.mp3")
                pygame.mixer.music.play(loops=0)
                pygame.mixer.music.set_volume(0.3)

            blank_card_3 = Label(gui, image=new_card, bg='#f0e5c2')
            blank_card_3.place(x=280, y=107)
            card_3 = Label(gui, text=str(rand3), font=('KBLuckyClover', 35), bg='#d5a3cf')
            card_3.place(x=318, y=162, anchor="center")
            money.config(text=str(int(pocket_money)))
            print(int(pocket_money), bet)
            higher = 0
            lower = 0

            if pocket_money < 1:
                game_over = messagebox.askquestion("IN BETWEEN", "GAME OVER! \nContinue?")
                if game_over == 'no':
                    gui.quit()
                else:
                    global count
                    count = 1
                    start["state"] = 'disable'
                    deal["state"] = 'disable'
                    no_deal["state"] = 'disable'
                    reset["state"] = 'disable'
                    rounds5["state"] = 'normal'
                    rounds3["state"] = 'normal'
                    rounds10["state"] = 'normal'
                    bet_entry.delete(0, 'end')
                    blank_card_1.destroy()
                    blank_card_2.destroy()
                    card_1.destroy()
                    card_2.destroy()

                    money.config(text="0000.00")
                    status.config(text="Goodluck!")
                    rounds_played.config(text="0")
                    blank_card_3.destroy()
                    card_3.destroy()
                    if not higher == 0 and not lower == 0:
                        higher.destroy()
                        lower.destroy()
    except ValueError:  # error for no bet placed
        status.config(text="Please Enter\nYour Bet!")
        deal["state"] = 'normal'
        no_deal["state"] = 'normal'
        reset["state"] = 'disable'


def no_deal():
    global blank_card_3, card_3, pocket_money, higher, lower

    reset["state"] = 'normal'
    deal["state"] = 'disable'
    no_deal["state"] = 'disable'

    pygame.mixer.music.load("mixkit-select-click-1109.wav")
    pygame.mixer.music.play(loops=0)
    pygame.mixer.music.set_volume(0.3)

    pocket_money = pocket_money - (pocket_money * 0.10)
    money.config(text=str(int(pocket_money)))

    # setting value of not present widgets to avoid error

    blank_card_3 = 0
    card_3 = 0
    higher = 0
    lower = 0


def reveal_cards():
    global rounds, count, rand1, rand2, rand3, blank_card_1, blank_card_2, card_1, card_2, pocket_money, rounds
    global higher, lower
    rounds_played.config(text=count)

    start["state"] = 'disable'
    reset["state"] = 'disable'
    deal["state"] = 'normal'
    no_deal["state"] = 'normal'

    pygame.mixer.music.load("mixkit-select-click-1109.wav")
    pygame.mixer.music.play(loops=0)
    pygame.mixer.music.set_volume(0.3)

    rand1 = random.randint(0,13)
    rand2 = random.randint(0,13)
    rand3 = random.randint(0,13)

    blank_card_1 = Label(gui, image=card, bg='#f0e5c2')
    blank_card_1.place(x=184, y=107)
    blank_card_2 = Label(gui, image=card, bg='#f0e5c2')
    blank_card_2.place(x=366, y=107)

    card_1 = Label(gui, text=str(rand1), font=('KBLuckyClover', 35), bg='#f8d71f', )
    card_1.place(x=230, y=162, anchor="center")
    card_2 = Label(gui, text=str(rand2), font=('KBLuckyClover', 35), bg='#f8d71f')
    card_2.place(x=412, y=162, anchor="center")

    if rand1 == rand2:
        deal["state"] = 'disable'
        no_deal["state"] = 'disable'
        reset["state"] = 'disable'

        def higher_option():
            global pocket_money, blank_card_3, card_3, bet

            pygame.mixer.music.load("mixkit-select-click-1109.wav")
            pygame.mixer.music.play(loops=0)
            pygame.mixer.music.set_volume(0.3)

            reset["state"] = 'normal'
            try:
                bet = int(bet_entry.get())

                if bet > pocket_money:
                    status.config(text="Not Enough\n Money!")
                    deal["state"] = 'disable'
                    no_deal["state"] = 'disable'
                    reset["state"] = 'disable'
                else:
                    start["state"] = 'disable'
                    reset["state"] = 'normal'
                    deal["state"] = 'disable'
                    no_deal["state"] = 'disable'

                    if rand3 > rand1:
                        pocket_money += bet
                        money.config(text=str(int(pocket_money)))
                        status.config(text="You Won!")

                        pygame.mixer.music.load("collect-5930.mp3")
                        pygame.mixer.music.play(loops=0)
                        pygame.mixer.music.set_volume(0.3)
                    elif rand3 < rand1:
                        pocket_money -= bet
                        money.config(text=str(int(pocket_money)))
                        status.config(text="You Lost!")

                        pygame.mixer.music.load("negative_beeps-6008.mp3")
                        pygame.mixer.music.play(loops=0)
                        pygame.mixer.music.set_volume(0.3)
                    else:
                        start["state"] = 'disable'
                        reset["state"] = 'normal'
                        deal["state"] = 'disable'
                        no_deal["state"] = 'disable'

                        pocket_money = pocket_money * 3
                        money.config(text=str(int(pocket_money)))
                        status.config(text="Jackpot!")

                        pygame.mixer.music.load("mixkit-video-game-win-2016.wav")
                        pygame.mixer.music.play(loops=0)
                        pygame.mixer.music.set_volume(0.2)
                        print(int(pocket_money), bet)

                    blank_card_3 = Label(gui, image=new_card, bg='#f0e5c2')
                    blank_card_3.place(x=280, y=107)
                    card_3 = Label(gui, text=str(rand3), font=('KBLuckyClover', 35), bg='#d5a3cf')
                    card_3.place(x=318, y=162, anchor="center")

                    if pocket_money < 1:
                        game_over = messagebox.askquestion("IN BETWEEN", "GAME OVER! \nContinue?")
                        if game_over == 'no':
                            gui.quit()
                        else:
                            global count
                            count = 1
                            start["state"] = 'disable'
                            deal["state"] = 'disable'
                            no_deal["state"] = 'disable'
                            reset["state"] = 'disable'
                            rounds5["state"] = 'normal'
                            rounds3["state"] = 'normal'
                            rounds10["state"] = 'normal'

                            bet_entry.delete(0, 'end')
                            blank_card_1.destroy()
                            blank_card_2.destroy()
                            card_1.destroy()
                            card_2.destroy()

                            money.config(text="0000.00")
                            status.config(text="Goodluck!")
                            rounds_played.config(text="0")
                            blank_card_3.destroy()
                            card_3.destroy()
                            if not higher == 0 and not lower == 0:
                                higher.destroy()
                                lower.destroy()
            except ValueError:
                status.config(text="Please Enter\nYour Bet!")
                deal["state"] = 'normal'
                no_deal["state"] = 'normal'
                reset["state"] = 'disable'

        def lower_option():
            global pocket_money, blank_card_3, card_3, bet

            pygame.mixer.music.load("mixkit-select-click-1109.wav")
            pygame.mixer.music.play(loops=0)
            pygame.mixer.music.set_volume(0.3)

            reset["state"] = 'normal'
            try:
                bet = int(bet_entry.get())

                if bet > pocket_money:
                    status.config(text="Not Enough\n Money!")
                    deal["state"] = 'disable'
                    no_deal["state"] = 'disable'
                    reset["state"] = 'disable'
                else:
                    start["state"] = 'disable'
                    reset["state"] = 'normal'
                    deal["state"] = 'disable'
                    no_deal["state"] = 'disable'

                    if rand3 < rand1:
                        pocket_money += bet
                        money.config(text=str(int(pocket_money)))
                        status.config(text="You Won!")

                        pygame.mixer.music.load("collect-5930.mp3")
                        pygame.mixer.music.play(loops=0)
                        pygame.mixer.music.set_volume(0.3)
                    elif rand3 > rand1:
                        pocket_money -= bet
                        money.config(text=str(int(pocket_money)))
                        status.config(text="You Lost!")

                        pygame.mixer.music.load("negative_beeps-6008.mp3")
                        pygame.mixer.music.play(loops=0)
                        pygame.mixer.music.set_volume(0.3)
                    else:
                        start["state"] = 'disable'
                        reset["state"] = 'normal'
                        deal["state"] = 'disable'
                        no_deal["state"] = 'disable'

                        pocket_money = pocket_money * 3
                        money.config(text=str(int(pocket_money)))
                        status.config(text="Jackpot!")

                        pygame.mixer.music.load("mixkit-video-game-win-2016.wav")
                        pygame.mixer.music.play(loops=0)
                        pygame.mixer.music.set_volume(0.3)
                        print(int(pocket_money), bet)

                    blank_card_3 = Label(gui, image=new_card, bg='#f0e5c2')
                    blank_card_3.place(x=280, y=107)
                    card_3 = Label(gui, text=str(rand3), font=('KBLuckyClover', 35), bg='#d5a3cf')
                    card_3.place(x=318, y=162, anchor="center")

                    if pocket_money < 1:
                        game_over = messagebox.askquestion("IN BETWEEN", "GAME OVER! \nContinue?")
                        if game_over == 'no':
                            gui.quit()
                        else:
                            global count
                            count = 1
                            start["state"] = 'disable'
                            deal["state"] = 'disable'
                            no_deal["state"] = 'disable'
                            reset["state"] = 'disable'
                            rounds5["state"] = 'normal'
                            rounds3["state"] = 'normal'
                            rounds10["state"] = 'normal'

                            bet_entry.delete(0, 'end')
                            blank_card_1.destroy()
                            blank_card_2.destroy()
                            card_1.destroy()
                            card_2.destroy()

                            money.config(text="0000.00")
                            status.config(text="Goodluck!")
                            rounds_played.config(text="0")
                            blank_card_3.destroy()
                            card_3.destroy()
                            if not higher == 0 and not lower == 0:
                                higher.destroy()
                                lower.destroy()
            except ValueError:
                status.config(text="Please Enter\nYour Bet!")
                deal["state"] = 'normal'
                no_deal["state"] = 'normal'
                reset["state"] = 'disable'

        higher = Button(gui, image=button7, bd=0, bg='#f0e5c2', command=higher_option)
        lower = Button(gui, image=button6, bd=0, bg='#f0e5c2', command=lower_option)
        higher.place(x=260, y=310)
        lower.place(x=320, y=310)

    print(rand1, rand2, rand3)


def quit_game():  # for the ending page
    gui.destroy()


def reset_game():  # for the ending page
    global count
    count = 1

    start["state"] = 'disable'
    deal["state"] = 'disable'
    no_deal["state"] = 'disable'
    reset["state"] = 'disable'
    rounds5["state"] = 'normal'
    rounds3["state"] = 'normal'
    rounds10["state"] = 'normal'

    bet_entry.delete(0, 'end')
    game_end.destroy()
    blank_card_1.destroy()
    blank_card_2.destroy()
    card_1.destroy()
    card_2.destroy()

    money.config(text="0000.00")
    rounds_played.config(text="0")
    status.config(text="Goodluck!")

    if not blank_card_3 == 0 and not card_3 == 0:
        blank_card_3.destroy()
        card_3.destroy()
    if not higher == 0 and not lower == 0:
        higher.destroy()
        lower.destroy()


count = 1


def reset_cards():
    global count, pocket_money, game_end
    if count == rounds:  # If round is done

        pygame.mixer.music.load("win.mp3")
        pygame.mixer.music.play(loops=0)
        pygame.mixer.music.set_volume(0.3)

        game_end = Frame(gui, bg='#d5a3cf', width=640, height=360, highlightbackground='white', highlightthickness=5)
        background = Label(game_end, image=bg_2)
        tot_win_label = Label(game_end, text="PHP", font=('DK Lemon Yellow Sun', 20), fg='#f0e5c2', bg='#262626')
        tot_win = Label(game_end, text=int(pocket_money), font=('DK Lemon Yellow Sun', 20), fg='#f0e5c2', bg='#262626')
        new_game = Button(game_end, image=button10, bg='#262626', bd=0, command=reset_game)
        out = Button(game_end, image=button11, bg='#262626', bd=0, command=quit_game)

        new_game.place(x=240, y=278)
        out.place(x=330, y=278)
        tot_win.place(x=385, y=198, anchor="w")
        tot_win_label.place(x=345, y=178)
        background.place(x=-7, y=0)
        game_end.place(x=0, y=0)

    else:
        count += 1  # round counter every restart
        start["state"] = 'normal'
        deal["state"] = 'disable'
        no_deal["state"] = 'disable'
        reset["state"] = 'disable'

        pygame.mixer.music.load("mixkit-select-click-1109.wav")
        pygame.mixer.music.play(loops=0)
        pygame.mixer.music.set_volume(0.3)

        bet_entry.delete(0, 'end')
        blank_card_1.destroy()
        blank_card_2.destroy()
        card_1.destroy()
        card_2.destroy()

        status.config(text="Goodluck!")
        rounds_played.config(text=count)
        if not blank_card_3 == 0 and not card_3 == 0:
            blank_card_3.destroy()
            card_3.destroy()
        if not higher == 0 and not lower == 0:
            higher.destroy()
            lower.destroy()


money_label = Label(gui, text="Pocket Money:   Php", font=('Pumpkin Cheesecake', 13), bg='#f0e5c2')
money = Label(gui, text="0000.00", font=('Pumpkin Cheesecake', 13), bg='#f0e5c2')
bet_label = Label(gui, text="BET:      PHP", font=('Chonkies', 14), bg='#f0e5c2')
bet_entry = Entry(gui, text="", font=('Chonkies', 14), bg='#f0e5c2', width=5, bd=0)
status = Label(gui, text="GOODLUCK", font=('DK Lemon Yellow Sun', 18), fg='white', bg='#f37709')
rounds_label = Label(gui, text="ROUND:", font=('Pumpkin Cheesecake', 11), fg='#262626', bg='#f0e5c2')
rounds_played = Label(gui, text="0", font=('Pumpkin Cheesecake', 11), fg='#262626', bg='#f0e5c2')

deal = Button(gui, image=button1, bd=0, bg='#f0e5c2', command=deal, state=DISABLED)
no_deal = Button(gui, image=button2, bd=0, bg='#f0e5c2', command=no_deal, state=DISABLED)
rounds3 = Button(gui, image=button3, bd=0, bg='#262626', command=three_rounds)
rounds5 = Button(gui, image=button4, bd=0, bg='#262626', command=five_rounds)
rounds10 = Button(gui, image=button5, bd=0, bg='#262626', command=ten_rounds)
start = Button(gui, image=button8, bd=0, bg='#f0e5c2', command=reveal_cards, state=DISABLED)
reset = Button(gui, image=button9, bd=0, bg='#f0e5c2', command=reset_cards, state=DISABLED)

money_label.place(x=245, y=229)
money.place(x=350, y=229)
status.place(x=55, y=310, anchor="center")
bet_label.place(x=235, y=246)
bet_entry.place(x=350, y=247)
deal.place(x=249, y=283)
no_deal.place(x=316, y=283)
rounds3.place(x=230, y=8)
rounds5.place(x=295, y=8)
rounds10.place(x=360, y=8)
start.place(x=455, y=112)
reset.place(x=455, y=168)
rounds_label.place(x=290, y=87)
rounds_played.place(x=335, y=87)

gui.mainloop()
