#Case№3
#Developers: Shatalov Alexander, Denis Kachkin, Andrew Svilin

import random as ran
from math import prod
import local as loc

#Following four strokes represent key characteristics of game for all three teams
fin=[50,50,50]
hth=[50,50,50]
joy=[50,50,50]
grd=[50,50,50]
#Card bank
unused_cards = []
for i in range (1, 43):
    unused_cards.append(i)

def card(n,p):
    '''
    :param n: Receives number of card from main()
    :param p: Receives player's number from main()
    :return: Difference of characteristic, depend on users' choices
    '''
    global grd
    global joy
    global hth
    global fin
    if n == 1:
        print(loc.THE_NEIGHBOR_INVITES)
        c = int(input(loc.NASTOLKI))
        if c == 1:
            hth[p] -= 10
            joy[p] += 5
        elif c == 2:
            grd[p] += 10
    if n == 2:
        print(loc.THE_TEACHER_OFFERS_JOB)
        c = int(input(loc.OFFERSJOB))
        if c == 1:
            hth[p] -= 10
            fin[p] += 5
        elif c == 2:
            joy[p] += 5
            hth[p] +=10
    if n == 3:
        print(loc.WENT_TO_THE_CLUB_INSTEAD)
        c = int(input(loc.BUNKER))
        if c == 1:
            joy[p] += 10
            fin[p] -= 10
        elif c == 2:
            joy[p] -= 5
            hth[p] += 8
    if n == 4:
        print(loc.FRIEND_ASKS_HELP_PROJECT)
        c = int(input(loc.FRIENDASKS))
        if c == 1:
            joy[p] -= 2
            grd[p] += 3
        elif c == 2:
            joy[p] += 2
            hth[p] -= 5
    if n == 5:
        print(loc.BUY_LAPTOP)
        c = int(input(loc.LAPTOPIK))
        if c == 1:
            fin[p] -= 7
            grd[p] += 10
        elif c == 2:
            grd[p] -= 5
    if n == 6:
        print(loc.TEACHER_SUGGEST_TO_CHEAT)
        c = int(input(loc.CHEAT))
        if c == 1:
            joy[p] += 2
            grd[p] += 10
        elif c == 2:
            grd[p] -= 10
    if n == 7:
        print(loc.GO_TO_CONCERT)
        c = int(input(loc.YES_NO))
        if c == 1:
            joy[p] += 7
            fin[p] -= 9
        elif c == 2:
            grd[p] += 7
    if n == 8:
        print(loc.FRIEND_INVITE_RUN)
        c = int(input(loc.RUN))
        if c == 1:
            joy[p] += 10
            fin[p] -= 10
        elif c == 2:
            grd[p] += 4
    if n == 9:
        print(loc.ROOMMATE_OFFERS_SPLIT)
        c = int(input(loc.SPLIT))
        if c == 1:
            joy[p] += 7
            fin[p] -= 7
        elif c == 2:
            grd[p] += 8
    if n == 10:
        print(loc.SKIP_LESSON_TO_SLEEP)
        c = int(input(loc.YES_NO))
        if c == 1:
            joy[p] += 5
            hth[p] += 5
            grd[p] -= 6
        elif c == 2:
            grd[p] += 5
    if n == 11:
        print(loc.COLLECT_BOTTLES)
        c = int(input(loc.BOTTLES))
        if c == 1:
            joy[p] -= 8
            fin[p] += 10
        elif c == 2:
            hth[p] += 8
    if n == 12:
        print(loc.FRIEND_INVITES_TO_GYM)
        c = int(input(loc.GYM))
        if c == 1:
            joy[p] += 5
            fin[p] -= 7
            hth[p] += 10
        elif c == 2:
            hth[p] -= 6
    if n == 13:
        print(loc.YOU_FOUND_MONEY)
        c = int(input(loc.MONEY))
        if c == 1:
            fin[p] += 8
        elif c == 2:
            joy[p] -= 10
    if n == 14:
        print(loc.BUS_LEAVING)
        c= int(input(loc.ASK_FOR_MONEY_ACCEPT_FATE))
        if c == 1:
            joy[p] += 6
            fin[p] += 5
        elif c == 2:
            joy[p] -= 12
    if n == 15:
        print(loc.YOU_GET_INTERVIEW)
        c = int(input(loc.INTERVIEW))
        if c == 1:
            joy[p] += 5
        elif c == 2:
            joy[p] -= 4
    if n == 16:
        print(loc.BUY_ANSWERS_FOR_EXAM)
        c = int(input(loc.ANSWERS))
        if c == 1:
            joy[p] += 4
            fin[p] -= 6
            grd[p] -= 8
        elif c == 2:
            grd[p] += 5
    if n == 17:
        print(loc.LEAVE_OR_STAY)
        c = int(input(loc.LEAVE))
        if c == 1:
            joy[p] += 3
            grd[p] -= 4
        elif c == 2:
            grd[p] += 3
    if n == 18:
        print(loc.COFFE_SMELLING)
        c = int(input(loc.YES_NO))
        if c == 1:
            joy[p] += 5
            fin[p] -= 5
        elif c == 2:
            joy[p] -= 5
    if n == 19:
        print(loc.PE_SKIING)
        c = int(input(loc.PE))
        if c == 1:
            joy[p] += 3
            hth[p] -= 4
        elif c == 2:
            grd[p] += 1
            hth[p] += 7
    if n == 20:
        print(loc.PROGR_EXAM)
        c= int(input(loc.YES_YES))
        if c == 1:
            grd[p] += 7
        elif c == 2:
            grd[p] += 7
    if n == 21:
        print(loc.FRIEND_OFERS_HELP)
        c = int(input(loc.HELP))
        if c == 1:
            grd[p] += 5
        elif c == 2:
            grd[p] -= 5
    if n == 22:
        print(loc.THE_TEACHER_OFFERS)
        c = int(input(loc.A_DILIGENT_STUDENT))
        if c == 1:
            hth[p] -= 5
            joy[p] += 5
            grd[p] += 10
        elif c == 2:
            hth[p] += 5
            grd[p] -= 10
    if n == 23:
        print(loc.THE_DEADLINE_COMING)
        c = int(input(loc.BUY_A_READY_MADE_ONE_DO_IT_YOURSELF))
        if c == 1:
            fin[p] -= 5
            hth[p] += 5
        elif c == 2:
            hth[p] -= 10
            grd[p] += 5
    if n == 24:
        print(loc.ORDER_A_COPY)
        c = int(input(loc.ORDER_WRITE_IT_YOURSELF))
        if c == 1:
            fin[p] -= 15
            hth[p] += 10
            grd[p] -= 5
            joy[p] -= 5
        elif c == 2:
            fin[p] += 10
            hth[p] -= 15
            grd[p] += 10
    if n == 25:
        print(loc.PLAY_A_PRANK)
        c = int(input(loc.PRANK_LEAVE_HIM_ALONE))
        if c == 1:
            hth[p] += 5
            joy[p] += 10
        elif c == 2:
            joy[p] -= 5
    if n == 26:
        print(loc.I_FOUND_A_BOOK)
        c = int(input(loc.BUY_DO_NOT_BUY))
        if c == 1:
            fin[p] -= 5
            hth[p] += 5
            joy[p] += 5
            grd[p] += 10
        elif c == 2:
            fin[p] += 5
            joy[p] -= 5
            grd[p] -= 5
    if n == 27:
        print(loc.BUY_TEXTBOOKS_OR_BORROW)
        c = int(input(loc.BORROW_THEM_FROM_THE_LIBRARY_ORDER))
        if c == 1:
            fin[p] -= 15
            joy[p] += 10
        elif c == 2:
            fin[p] += 15
            joy[p] -= 10
    if n == 28:
        print(loc.THE_TEACHER_OFFERS_OLYMPIAD)
        c = int(input(loc.AGREE_AFRAID))
        if c == 1:
            hth[p] -= 10
            grd[p] += 15
        elif c == 2:
            joy[p] -= 10
            grd[p] -= 10
    if n == 29:
        print(loc.PARTICIPATE_IN_ACTIVITIES)
        c = int(input(loc.STUDENT_SPRING))
        if c == 1:
            hth[p] += 10
            joy[p] += 15
            grd[p] -= 5
        elif c == 2:
            joy[p] -= 10
            grd[p] += 10
    if n == 30:
        print(loc.GET_AN_EVENING_JOB)
        c = int(input(loc.MAKING_MONEY))
        if c == 1:
            hth[p] -= 10
            joy[p] -= 5
            grd[p] -= 5
            fin[p] += 15
        elif c == 2:
            grd[p] += 10
            fin[p] -= 10
    if n == 31:
        print(loc.TO_HELP_WITH_EXAM)
        c = int(input(loc.HELP_ME))
        if c == 1:
            hth[p] -= 5
            joy[p] += 5
            grd[p] += 5
        elif c == 2:
            joy[p] -= 5
    if n == 32:
        print(loc.DO_MATHEMATICAL_HOMEWORK)
        c = int(input(loc.CHINA))
        if c == 1:
            hth[p] -= 10
            joy[p] -= 5
            grd[p] += 15
        elif c == 2:
            hth[p] += 5
            joy[p] += 10
            grd[p] -= 10
    if n == 33:
        print(loc.RENT_A_COTTAGE)
        c = int(input(loc.RENT_COTTAGE))
        if c == 1:
            hth[p] += 10
            joy[p] += 10
        elif c == 2:
            hth[p] -= 10
            joy[p] -= 10
            grd[p] += 5
    if n == 34:
        print(loc.TRY_TO_FIND_AN_SEAT)
        c = int(input(loc.AGREE_DISAGREE))
        if c == 1:
            hth[p] -= 5
            joy[p] -= 5
        elif c == 2:
            hth[p] += 5
            joy[p] += 10
    if n == 35:
        print(loc.LEAVE_YOUR_PHONE_ON)
        c = int(input(loc.AGREE_DISAGREE))
        if c == 1:
            hth[p] -= 10
            joy[p] += 5
        elif c == 2:
            hth[p] += 5
            joy[p] += 5
    if n == 36:
        print(loc.THE_ROOMMATE_GOT_SICK)
        c = int(input(loc.RENT_AN_APARTMENT_STAY))
        if c == 1:
            fin[p] -= 15
            hth[p] += 10
        elif c == 2:
            hth[p] -= 15
            joy[p] += 5
            fin[p] += 5
    if n == 37:
        print(loc.THE_TEACHER_MADE_A_MISTAKE)
        c = int(input(loc.CORRECT_THE_TEACHER_DO_NOT_SAY_ANYTHING))
        if c == 1:
            grd[p] += 5
            joy[p] += 10
        elif c == 2:
            joy[p] -= 5
            grd[p] -= 5
    if n == 38:
        print(loc.MAKE_A_BAD_PRESENTATION)
        c = int(input(loc.RUSSIAN_FLASH_DRIVE))
        if c == 1:
            joy[p] += 5
            grd[p] -= 5
        elif c == 2:
            grd[p] -= 10
    if n == 39:
        print(loc.PLAY_SPORTS_OR_PLAY_VIDEO_GAMES)
        c = int(input(loc.PLAY_SPORTS_PLAY_VIDEO_GAMES))
        if c == 1:
            joy[p] += 5
            hth[p] +=15
        elif c == 2:
            joy[p] += 10
            hth[p] -= 5
    if n == 40:
        print(loc.ATTEND_AN_ADDITIONAL_COURSE)
        c = int(input(loc.AGREE_DISAGREE))
        if c == 1:
            joy[p] += 5
            hth[p] += 5
            fin[p] -= 5
            grd[p] += 5
        elif c == 2:
            joy[p] -= 10
            fin[p] += 5
    if n == 41:
        print(loc.BUY_AN_ENERGY_DRINK)
        c = int(input(loc.ENERGETIK_HONEY))
        if c == 1:
            joy[p] += 10
            hth[p] -= 15
            fin[p] -= 5
            grd[p] += 5
        elif c == 2:
            joy[p] -= 5
            fin[p] += 5
            hth[p] += 10
            grd[p] += 5
    if n == 42:
        print(loc.PROGR_PARA)
        c = int(input(loc.PROG_PARA_ANSW))
        if c == 1:
            joy[p] -= 10
            grd[p] += 5
            hth[p] += 10
        elif c == 2:
            joy[p] += 10
            hth[p] -= 10
            grd[p] -= 5

def accidents(a,p):
    '''
    :param a: Receives number of accident from main()
    :param p: Receives player's number from main()
    :return: Differences of characteristics, that user can't affect
    '''
    global hth
    global joy
    global grd
    global fin
    if a == 1:
        print (loc.MISSING)
        fin[p]-=10
    if a == 2:
        print(loc.SICKNESS)
        hth[p]-=10
    if a == 3:
        print(loc.FINDING)
        fin[p]+=5
    if a == 4:
        print(loc.SUNNY_DAY)
        hth[p]+=3
    if a == 5:
        print(loc.FRIENDS)
        joy[p]+=5
    if a == 6:
        print(loc.FRIENDS_NO)
        joy[p]-=5
    if a == 7:
        print(loc.MOM_CALL)
        joy[p]+=3
        fin[p]+=3
        hth[p]+=3
    if a == 8:
        print(loc.BAD_DAY)
        joy[p]-=5
    if a == 9:
        print(loc.OFFENSIVE_JOKE)
        joy[p]-=2
    if a == 10:
        print(loc.EASY_TEST)
        grd[p]+=2

def main():
    '''
    Main function
    :return: None
    '''
    p_name=[]
    p1=input()
    p_name.append(p1)
    p2=input()
    p_name.append(p2)
    p3=input()
    p_name.append(p3)
    print('Начальные характеристики:')
    print('HP: 50 J: 50 M: 50 GR: 50')
    print('\n')
    while prod(fin) > 0 and prod(hth) > 0 and prod(joy) > 0 and prod(grd) > 0:
        p=0
        accident = ran.randrange(0,11)
        if fin[0] > 99 or fin[1] > 99 or fin[2] > 99:
            print(loc.TOO_MANY_M)
            break
        if hth[0] > 99 or hth[1] > 99 or hth[2] > 99:
            print(loc.TOO_MANY_H)
            break
        if joy[0] > 99 or joy[1] > 99 or joy[2] > 99:
            print(loc.TOO_MANY_J)
            break
        if grd[0] > 99 or grd[1] > 99 or grd[2] > 99:
            print(loc.TOO_MANY_G)
            break
        if accident < 10:
            if sum(unused_cards) > 0:
                print('Ход команды:',p_name[p])
                n = ran.choice(unused_cards)
                card(n,p)
                unused_cards.remove(n)
                p+=1
                print('\n')
                print('Ход команды:',p_name[p])
                n = ran.choice(unused_cards)
                card(n,p)
                unused_cards.remove(n)
                p+=1
                print('\n')
                print('Ход команды:',p_name[p])
                n = ran.choice(unused_cards)
                card(n,p)
                unused_cards.remove(n)
                print('\n')
                print('Параметры команд:')
                print(p_name[0],'| HP:', hth[0], 'J:', joy[0], 'M:', fin[0], 'GR:', grd[0])
                print(p_name[1],'| HP:', hth[1], 'J:', joy[1], 'M:', fin[1], 'GR:', grd[1])
                print(p_name[2],'| HP:', hth[2], 'J:', joy[2], 'M:', fin[2], 'GR:', grd[2])
            else:
                print(loc.VICTORY)
                break
        else:
            a = ran.randrange(1, 11)
            accidents(a,p)
            p+=1
            print('\n')
            a = ran.randrange(1, 11)
            accidents(a,p)
            p+=1
            print('\n')
            a = ran.randrange(1, 11)
            accidents(a,p)
            print('\n')
            print('Параметры команд:')
            print('HP:', hth[0], 'J:', joy[0], 'M:', fin[0], 'GR:', grd[0])
            print('HP:', hth[1], 'J:', joy[1], 'M:', fin[1], 'GR:', grd[1])
            print('HP:', hth[2], 'J:', joy[2], 'M:', fin[2], 'GR:', grd[2])
            print('\n')
    else:
        if fin[0] < 1 or fin[1] < 1 or fin[2] < 1:
            print(loc.LOW_F)
        if hth[0] < 1 or hth[1] < 1 or hth[2] < 1:
            print(loc.LOW_H)
        if joy[0] < 1 or joy[1] < 1 or joy[2] < 1:
            print(loc.LOW_J)
        if grd[0] < 1 or grd[1] < 1 or grd[2] < 1:
            print(loc.LOW_M)

main()
