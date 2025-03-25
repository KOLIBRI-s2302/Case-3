#Case№3
#Developers: Shatalov Alexander, Denis Kachkin, Andrew Svilin

import random as ran
import sys
import local as loc

#Following four strokes represent key characteristics of game
fin = 50
hth = 50
joy = 50
grd = 50
#Card bank
unused_cards = []
for i in range (1, 51):
    unused_cards.append(i)

def card(n):
    '''
    :param n: Receives number of card from main()
    :return: Difference of characteristic, depend on users' choices
    '''
    global hth
    global joy
    global grd
    global fin
    if n == 1:
        print(loc.THE_NEIGHBOR_INVITES)
        c = int(input(loc.AGREE_DISAGREE))
        if c == 1:
            hth -= 10
            joy += 5
        elif c == 2:
            grd += 2
        print('HP:', hth, 'J:', joy, 'M:', fin, 'GR:', grd)
        print('\n')
    if n == 2:
        print(loc.THE_TEACHER_OFFERS_JOB)
        c = int(input(loc.AGREE_DISAGREE))
        if c == 1:
            hth -= 10
            fin += 5
        elif c == 2:
            joy += 2
        print('HP:', hth, 'J:', joy, 'M:', fin, 'GR:', grd)
        print('\n')
    if n == 3:
        print(loc.WENT_TO_THE_CLUB_INSTEAD)
        c = int(input(loc.YES_NO))
        if c == 1:
            joy += 10
            fin -= 10
        elif c == 2:
            joy -= 5
        print('HP:', hth, 'J:', joy, 'M:', fin, 'GR:', grd)
        print('\n')
    if n == 4:
        print(loc.FRIEND_ASKS_HELP_PROJECT)
        c = int(input(loc.AGREE_DISAGREE))
        if c == 1:
            joy -= 2
            grd += 3
        elif c == 2:
            joy += 2
        print('HP:', hth, 'J:', joy, 'M:', fin, 'GR:', grd)
        print('\n')
    if n == 5:
        print(loc.BUY_LAPTOP)
        c = int(input(loc.YES_NO))
        if c == 1:
            fin -= 7
            grd += 10
        elif c == 2:
            grd -= 5
        print('HP:', hth, 'J:', joy, 'M:', fin, 'GR:', grd)
        print('\n')
    if n == 6:
        print(loc.TEACHER_SUGGEST_TO_CHEAT)
        c = int(input(loc.AGREE_DISAGREE))
        if c == 1:
            joy += 2
            grd += 10
        elif c == 2:
            grd -= 10
        print('HP:', hth, 'J:', joy, 'M:', fin, 'GR:', grd)
        print('\n')
    if n == 7:
        print(loc.GO_TO_CONCERT)
        c = int(input(loc.YES_NO))
        if c == 1:
            joy += 7
            fin -= 4
        elif c == 2:
            grd += 3
        print('HP:', hth, 'J:', joy, 'M:', fin, 'GR:', grd)
        print('\n')
    if n == 8:
        print(loc.FRIEND_INVITE_RUN)
        c = int(input(loc.AGREE_DISAGREE))
        if c == 1:
            joy += 10
            fin -= 10
        elif c == 2:
            grd += 1
        print('HP:', hth, 'J:', joy, 'M:', fin, 'GR:', grd)
        print('\n')
    if n == 9:
        print(loc.ROOMMATE_OFFERS_SPLIT)
        c = int(input(loc.AGREE_DISAGREE))
        if c == 1:
            joy += 2
            fin -= 2
        elif c == 2:
            grd += 2
        print('HP:', hth, 'J:', joy, 'M:', fin, 'GR:', grd)
        print('\n')
    if n == 10:
        print(loc.SKIP_LESSON_TO_SLEEP)
        c = int(input(loc.YES_NO))
        if c == 1:
            joy += 2
            hth += 5
            grd -= 6
        elif c == 2:
            grd += 3
        print('HP:', hth, 'J:', joy, 'M:', fin, 'GR:', grd)
        print('\n')
    if n == 11:
        print(loc.COLLECT_BOTTLES)
        c = int(input(loc.YES_NO))
        if c == 1:
            joy -= 2
            fin += 10
        elif c == 2:
            hth += 3
        print('HP:', hth, 'J:', joy, 'M:', fin, 'GR:', grd)
        print('\n')
    if n == 12:
        print(loc.FRIEND_INVITES_TO_GYM)
        c = int(input(loc.AGREE_DISAGREE))
        if c == 1:
            joy += 1
            fin -= 3
            hth += 10
        elif c == 2:
            hth -= 6
        print('HP:', hth, 'J:', joy, 'M:', fin, 'GR:', grd)
        print('\n')
    if n == 13:
        print(loc.YOU_FOUND_MONEY)
        c = int(input(loc.TAKE_LEAVE))
        if c == 1:
            fin += 4
        elif c == 2:
            joy -= 5
        print('HP:', hth, 'J:', joy, 'M:', fin, 'GR:', grd)
        print('\n')
    if n == 14:
        print(loc.BUS_LEAVING)
        c= int(input(loc.ASK_FOR_MONEY_ACCEPT_FATE))
        if c == 1:
            joy += 1
            fin += 2
        elif c == 2:
            joy -= 12
        print('HP:', hth, 'J:', joy, 'M:', fin, 'GR:', grd)
        print('\n')
    if n == 14:
        print(loc.YOU_GET_INTERVIEW)
        c = int(input(loc.AGREE_DISAGREE))
        if c == 1:
            joy += 2
        elif c == 2:
            joy -= 4
        print('HP:', hth, 'J:', joy, 'M:', fin, 'GR:', grd)
        print('\n')
    if n == 15:
        print(loc.BUY_ANSWERS_FOR_EXAM)
        c = int(input(loc.YES_NO))
        if c == 1:
            joy += 1
            fin -= 3
            grd -= 8
        elif c == 2:
            grd += 5
        print('HP:', hth, 'J:', joy, 'M:', fin, 'GR:', grd)
        print('\n')
    if n == 16:
        print(loc.LEAVE_OR_STAY)
        c = int(input(loc.YES_NO))
        if c == 1:
            joy += 3
            grd -= 4
        elif c == 2:
            grd += 3
        print('HP:', hth, 'J:', joy, 'M:', fin, 'GR:', grd)
        print('\n')
    if n == 17:
        print(loc.COFFE_SMELLING)
        c = int(input(loc.YES_NO))
        if c == 1:
            joy += 2
            fin -= 5
        elif c == 2:
            joy -= 2
        print('HP:', hth, 'J:', joy, 'M:', fin, 'GR:', grd)
        print('\n')
    if n == 18:
        print(loc.PE_SKIING)
        c = int(input(loc.YES_NO))
        if c == 1:
            joy += 1
            hth -= 4
        elif c == 2:
            grd += 1
            hth += 7
        print('HP:', hth, 'J:', joy, 'M:', fin, 'GR:', grd)
        print('\n')
    if n == 19:
        print(loc.PROGR_EXAM)
        c= int(input(loc.YES_YES))
        if c == 1:
            grd += 7
        elif c == 2:
            grd += 7
        print('HP:', hth, 'J:', joy, 'M:', fin, 'GR:', grd)
        print('\n')
    if n == 20:
        print(loc.FRIEND_OFERS_HELP)
        c = int(input(loc.AGREE_DISAGREE))
        if c == 1:
            grd += 5
        elif c == 2:
            grd -= 5
        print('HP:', hth, 'J:', joy, 'M:', fin, 'GR:', grd)
        print('\n')
    if n == 21:
        print(loc.THE_TEACHER_OFFERS_TO_VOLUNTEER_AT_THE_EVENT_FOR_BONUS_POINTS)
        c = int(input(loc.AGREE_DISAGREE))
        if c == 1:
            hth -= 5
            joy += 5
            grd += 10
        elif c == 2:
            hth += 5
            grd -= 10
        print('HP:', hth, 'J:', joy, 'M:', fin, 'GR:', grd)
        print('\n')
    if n == 22:
        print(loc.THE_DEADLINE_FOR_THE_COURSE_IS_COMING_SOON_AND_YOU_HAVE_ONLY_JUST_STARTED)
        c = int(input(loc.BUY_A_READY_MADE_ONE_DO_IT_YOURSELF))
        if c == 1:
            fin -= 5
            hth += 5
        elif c == 2:
            hth -= 10
            grd += 5
        print('HP:', hth, 'J:', joy, 'M:', fin, 'GR:', grd)
        print('\n')
    if n == 23:
        print(loc.ORDER_A_COPY_OF_THE_DIPLOMA_OR_WRITE_IT_YOURSELF)
        c = int(input(loc.ORDER_WRITE_IT_YOURSELF))
        if c == 1:
            fin -= 15
            hth += 10
            grd -= 5
            joy -= 5
        elif c == 2:
            fin += 10
            hth -= 15
            grd += 10
        print('HP:', hth, 'J:', joy, 'M:', fin, 'GR:', grd)
        print('\n')
    if n == 24:
        print(loc.PLAY_A_PRANK_ON_A_FRIEND_OR_LEAVE_HIM_ALONE)
        c = int(input(loc.PRANK_LEAVE_HIM_ALONE))
        if c == 1:
            hth += 5
            joy += 10
        elif c == 2:
            joy -= 5
        print('HP:', hth, 'J:', joy, 'M:', fin, 'GR:', grd)
        print('\n')
    if n == 25:
        print(loc.I_FOUND_A_RARE_BOOK_IN_THE_STORE_FOR_STUDYING)
        c = int(input(loc.BUY_DO_NOT_BUY))
        if c == 1:
            fin -= 5
            hth += 5
            joy += 5
            grd += 10
        elif c == 2:
            fin += 5
            joy -= 5
            grd -= 5
        print('HP:', hth, 'J:', joy, 'M:', fin, 'GR:', grd)
        print('\n')
    if n == 26:
        print(loc.BUY_TEXTBOOKS_OR_BORROW_THEM_FROM_THE_LIBRARY)
        c = int(input(loc.BORROW_THEM_FROM_THE_LIBRARY_ORDER))
        if c == 1:
            fin -= 15
            joy += 10
        elif c == 2:
            fin += 15
            joy -= 10
        print('HP:', hth, 'J:', joy, 'M:', fin, 'GR:', grd)
        print('\n')
    if n == 27:
        print(loc.THE_TEACHER_OFFERS_TO_PARTICIPATE_IN_THE_OLYMPIAD)
        c = int(input(loc.AGREE_DISAGREE))
        if c == 1:
            hth -= 10
            grd += 15
        elif c == 2:
            joy -= 10
            grd -= 10
        print('HP:', hth, 'J:', joy, 'M:', fin, 'GR:', grd)
        print('\n')
    if n == 28:
        print(loc.PARTICIPATE_IN_STUDENT_AMATEUR_ACTIVITIES)
        c = int(input(loc.AGREE_DISAGREE))
        if c == 1:
            hth += 10
            joy += 15
            grd -= 5
        elif c == 2:
            joy -= 10
            grd += 10
        print('HP:', hth, 'J:', joy, 'M:', fin, 'GR:', grd)
        print('\n')
    if n == 29:
        print(loc.GET_AN_EVENING_JOB)
        c = int(input(loc.AGREE_DISAGREE))
        if c == 1:
            hth -= 10
            joy -= 5
            grd -= 5
            fin += 15
        elif c == 2:
            grd += 10
            fin -= 10
        print('HP:', hth, 'J:', joy, 'M:', fin, 'GR:', grd)
        print('\n')
    if n == 30:
        print(loc.TO_HELP_A_FELLOW_STUDENT_WITH_AN_EXAM)
        c = int(input(loc.AGREE_DISAGREE))
        if c == 1:
            hth -= 5
            joy += 5
            grd += 5
        elif c == 2:
            joy -= 5
        print('HP:', hth, 'J:', joy, 'M:', fin, 'GR:', grd)
        print('\n')
    if n == 31:
        print(loc.DO_YOUR_MATHEMATICAL_ANALYSIS_HOMEWORK_YOURSELF_OR_ORDER_FROM_A_FREELANCER)
        c = int(input(loc.BUY_A_READY_MADE_ONE_DO_IT_YOURSELF))
        if c == 1:
            hth -= 10
            joy -= 5
            grd += 15
        elif c == 2:
            hth += 5
            joy += 10
            grd -= 10
        print('HP:', hth, 'J:', joy, 'M:', fin, 'GR:', grd)
        print('\n')
    if n == 32:
        print(loc.A_FRIEND_IS_CALLING_FOR_A_TRIP_TO_ANOTHER_CITY)
        c = int(input(loc.AGREE_DISAGREE))
        if c == 1:
            hth += 10
            joy += 10
        elif c == 2:
            hth -= 10
            joy -= 10
            grd += 5
        print('HP:', hth, 'J:', joy, 'M:', fin, 'GR:', grd)
        print('\n')
    if n == 33:
        print(loc.TRY_TO_FIND_AN_EMPTY_SEAT_IN_KUKURUZA)
        c = int(input(loc.AGREE_DISAGREE))
        if c == 1:
            hth -= 5
            joy -= 5
        elif c == 2:
            hth += 5
            joy += 10
        print('HP:', hth, 'J:', joy, 'M:', fin, 'GR:', grd)
        print('\n')
    if n == 34:
        print(loc.LEAVE_YOUR_PHONE_ON_DURING_THE_EXAM)
        c = int(input(loc.AGREE_DISAGREE))
        if c == 1:
            hth -= 10
            joy += 5
        elif c == 2:
            hth += 5
            joy += 5
        print('HP:', hth, 'J:', joy, 'M:', fin, 'GR:', grd)
        print('\n')
    if n == 35:
        print(loc.THE_ROOMMATE_GOT_SICK)
        c = int(input(loc.RENT_AN_APARTMENT_STAY_IN_THE_DORM))
        if c == 1:
            fin -= 15
            hth += 10
        elif c == 2:
            hth -= 15
            joy += 5
            fin += 5
        print('HP:', hth, 'J:', joy, 'M:', fin, 'GR:', grd)
        print('\n')
    if n == 36:
        print(loc.THE_TEACHER_MADE_A_MISTAKE_IN_YOUR_ASSESSMENT)
        c = int(input(loc.CORRECT_THE_TEACHER_DO_NOT_SAY_ANYTHING))
        if c == 1:
            grd += 5
            joy += 10
        elif c == 2:
            joy -= 5
            grd -= 5
        print('HP:', hth, 'J:', joy, 'M:', fin, 'GR:', grd)
        print('\n')
    if n == 37:
        print(loc.MAKE_A_BAD_PRESENTATION_IN_FRONT_OF_AN_AUDIENCE)
        c = int(input(loc.AGREE_DISAGREE))
        if c == 1:
            joy += 5
            grd -= 5
        elif c == 2:
            grd -= 10
        print('HP:', hth, 'J:', joy, 'M:', fin, 'GR:', grd)
        print('\n')
    if n == 38:
        print(loc.PLAY_SPORTS_OR_PLAY_VIDEO_GAMES)
        c = int(input(loc.PLAY_SPORTS_PLAY_VIDEO_GAMES))
        if c == 1:
            joy += 5
            hth +=15
        elif c == 2:
            joy += 10
            hth -= 5
        print('HP:', hth, 'J:', joy, 'M:', fin, 'GR:', grd)
        print('\n')
    if n == 39:
        print(loc.ATTEND_AN_ADDITIONAL_COURSE)
        c = int(input(loc.AGREE_DISAGREE))
        if c == 1:
            joy += 5
            hth += 5
            fin -= 5
            grd += 5
        elif c == 2:
            joy -= 10
            fin += 5
        print('HP:', hth, 'J:', joy, 'M:', fin, 'GR:', grd)
        print('\n')
    if n == 40:
        print(loc.BUY_AN_ENERGY_DRINK_BEFORE_STUDYING_AT_NIGHT)
        c = int(input(loc.BUY_DO_NOT_BUY))
        if c == 1:
            joy += 10
            hth -= 15
            fin -= 5
            grd += 5
        elif c == 2:
            joy -= 5
            fin += 5
            hth += 10
            grd += 5
        print('HP:', hth, 'J:', joy, 'M:', fin, 'GR:', grd)
        print('\n')

def accidents(a):
    '''
    :param a: Receives number of accident from main()
    :return: Differences of characteristics, that user can't affect
    '''
    global hth
    global joy
    global grd
    global fin
    if a == 1:
        print (loc.MISSING)
        fin-=10
    if a == 2:
        print(loc.SICKNESS)
        hth-=10
    if a == 3:
        print(loc.FINDING)
        fin+=5
    if a == 4:
        print(loc.SUNNY_DAY)
        hth+=3
    if a == 5:
        print(loc.FRIENDS)
        joy+=5
    if a == 6:
        print(loc.FRIENDS_NO)
        joy-=5
    if a == 7:
        print(loc.MOM_CALL)
        joy+=3
        fin+=3
        hth+=3
    if a == 8:
        print(loc.BAD_DAY)
        joy-=5
    if a == 9:
        print(loc.OFFENSIVE_JOKE)
        joy-=2
    if a == 10:
        print(loc.EASY_TEST)
        grd+=2

def main():
    '''
    Main function
    :return: None
    '''
    print('HP:', hth, 'J:', joy, 'M:', fin, 'GR:', grd)
    print('\n')
    while sum(unused_cards) != 0:
        while fin * hth * joy * grd != 0:
            accident = ran.randrange(0, 11)
            if fin > 99:
                print(loc.TOO_MANY_M)
                sys.exit()
            if hth > 99:
                print(loc.TOO_MANY_H)
                sys.exit()
            if joy > 99:
                print(loc.TOO_MANY_J)
                sys.exit()
            if grd > 99:
                print(loc.TOO_MANY_G)
                sys.exit()
            if accident < 10:
                n = ran.choice(unused_cards)
                unused_cards.remove(n)
                card(n)
            else:
                a = ran.randrange(1, 11)
                accidents(a)
                print('HP:', hth, 'J:', joy, 'M:', fin, 'GR:', grd)
                print('\n')
        else:
            if fin < 1:
                print(loc.LOW_F)
                sys.exit()
            if hth < 1:
                print(loc.LOW_H)
                sys.exit()
            if joy < 1:
                print(loc.LOW_J)
                sys.exit()
            if grd < 1:
                print(loc.LOW_M)
                sys.exit()
    else:
        print (loc.VICTORY)

main()