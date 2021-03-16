# Jordan Trombly
# 11/5/18
# Blackjack
from graphics import *
from random import shuffle
import random
from time import *
from random import randrange

def main():

##########################################
###########CREATE PLAYER DECK#############
##########################################

    suitsP = ['C', 'D', 'H', 'S']
    valuesP = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    pointsP = [2,3,4,5,6,7,8,9,10,10,10,10,11]

    player_hand = []
    Pdeck_list = []

    Pindex = 0
    for s in suitsP:
        Pindex = 0
        for v in valuesP:
            Pcard = ['./cards/' + v + s + '.gif']
            Pcards = [v + s, pointsP[Pindex],'./cards/' + v + s + '.gif']
            Pdeck_list.append(Pcards)
            Pindex += 1

    
##########################################
###########CREATE DEALER DECK#############
##########################################

    suitsD = ['C', 'D', 'H', 'S']
    valuesD = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    pointsD = [2,3,4,5,6,7,8,9,10,10,10,10,11]

    dealer_hand = []
    Ddeck_list = []

    Dindex = 0
    for s in suitsD:
        Dindex = 0
        for v in valuesD:
            Dcard = ["./cards/" + v + s + ".gif"]
            Dcards = [v + s, pointsD[Dindex],'./cards/' + v + s + ".gif"]
            Ddeck_list.append(Dcards)
            Dindex += 1


##########################################
## Create the Home Screen for BlackJack ##
##########################################

    
    # create window
    win = GraphWin("Blackjack", 500, 500)

    # change coords
    win.setCoords(0, 0, 50, 50)

    # create lines
    

    # create a point for the image
    point1 = Point(25, 25)

    image1 = Image(point1, "500x500BlackJack.gif")
    image1.draw(win)

    # create text
    message = Text(Point(25, 45), "Blackjack")
    message.setSize(36)
    message.setTextColor("white")
    message.draw(win)

    # create play box
    rect1 = Rectangle(Point(20, 5), Point(30, 10))
    rect1.setFill(color_rgb(0, 191, 255))
    rect1.draw(win)
    # label play box
    rectPlay = Text(rect1.getCenter(), "Play")
    rectPlay.setSize(20)
    rectPlay.draw(win)

    # change screen if user clicks play
    point = win.checkMouse()
    
###################################################################
## If user clicks play then change the screen to the actual game ##
###################################################################

    while True:
        point = win.checkMouse()
        if play_btnClick(point, rect1):
            
            rect1.undraw()
            rectPlay.undraw()
            message.undraw()
            image1.undraw()
            image2 = Image(Point(25, 25), "blackjack_table2.gif")
            image2.draw(win)
            break

##CREATE BOX FOR WINNER##

    winner_box = Rectangle(Point(0, 0), Point(50, 50))
    winner_box.setFill('white')

##CREATE BOX FOR LOSER##
    
    loser_box = Rectangle(Point(0, 0), Point(50, 50))
    loser_box.setFill('white')

##CREATE BOX FOR DEALER AND PLAYER SCORES##
    ##DRAW SCORE IN BOX LATER##
    sumDealer = 0
    sumPlayer = 0
    dealer_score = Rectangle(Point(40, 35), Point(45, 40))
    dealer_score.setOutline('white')
    dealer_score.draw(win)
 
    player_score = Rectangle(Point(40, 5), Point(45, 10))
    player_score.setOutline('white')
    player_score.draw(win)
    
##CREATE BOX TO DEAL CARDS##
    
    # create deal box
    rect2 = Rectangle(Point(22, 22), Point(32, 28))
    rect2.setFill(color_rgb(0, 191, 255))
    rect2.draw(win)
    
    # label deal box
    rectDeal = Text(rect2.getCenter(), "Deal")
    rectDeal.setSize(20)

##CREATE BOX FOR QUIT##
    btnquit = Rectangle(Point(2, 2), Point(8, 5))
    btnquit.setFill('blue')
    btnquit.draw(win)
    
    # label
    quit_lbl = Text((btnquit.getCenter()), 'Quit')
    quit_lbl.setSize(15)
    quit_lbl.draw(win)

##CREATE BOXES FOR HIT AND STAND##
    ## DONT SHOW LABELS TILL AFTER CARDS ARE DEALT##
    
    # create hit button
    rect3 = Rectangle(Point(10, 22), Point(19, 28))
    rect3.setFill('blue')
    rect3.draw(win)

    # create stand button
    rect4 = Rectangle(Point(35, 22), Point(44, 28))
    rect4.setFill('blue')
    rect4.draw(win)

    
##    betting_button(win, betting)
##    bank = bank - betting_button(win, betting)
##    
##    print(bank)



# how many rounds of dealing played
    Round = 0
    Sentinel = True
    while True:
        Sentinel2 = True
        while Sentinel2 :
            rectDeal.draw(win)
            Sentinel = True
            champ = ''
            sumPlayer = 0
            sumDealer = 0
            Sentinel3 = True
            while Sentinel:
                point2 = win.getMouse()
                if dealbtn(point2, rect2) :
                    player_hand = []
                    dealer_hand = []
                    #### Take 2 cards out of the deck_list and put them in the player_hand list
                    randIndex = random.randint(0,len(Pdeck_list) - 1)
                    Pcards = Pdeck_list[randIndex]
                    player_hand.append(Pcards)
                    Pdeck_list.remove(Pcards)
                    # Display card
                    Card1_player = Image(Point(25, 10), (Pcards[2]))
                    Card1_player.draw(win)

                    randIndex = random.randint(0,len(Pdeck_list) - 1)
                    Pcards = Pdeck_list[randIndex]
                    player_hand.append(Pcards)
                    Pdeck_list.remove(Pcards)
                    # Display card
                    Card2_player = Image(Point(Card1_player.getAnchor().getX() + 2, 10), (Pcards[2]))
                    Card2_player.draw(win)
                    ### Read a card from the players hand using the matrix notation
                    ### Playerhas two cards, two lists, in his hand_list.  We know that for
                    ### every list (or card) in their hand that in that list index 1
                    ### contains the numeric value of the card.
                    sumPlayer = 0
                    for i in range(0, len(player_hand)):
                        sumPlayer += player_hand[i][1]
                        for j in range(0,3):
                            print(player_hand[i][j])
                    print("Player is holding: ", sumPlayer)
                    # label score box
                    player_lbl = Text(player_score.getCenter(), sumPlayer)
                    player_lbl.setSize(20)
                    player_lbl.draw(win)

                    # Cover deal label
                    rectDeal.undraw()
                    
                    # label hit box
                    rectHit = Text(rect3.getCenter(), "Hit")
                    rectHit.setSize(20)
                    rectHit.draw(win)
                    # label stand box
                    rectStand = Text(rect4.getCenter(), "Stand")
                    rectStand.setSize(20)
                    rectStand.draw(win)


                    ### Take 2 cards out of the deck_list and put them in the dealer_hand list
                    DrandIndex = random.randint(0,len(Ddeck_list) - 1)
                    Dcards = Ddeck_list[DrandIndex]
                    dealer_hand.append(Dcards)
                    Ddeck_list.remove(Dcards)
                    # Display card
                    Card1_dealer = Image(Point(25, 40), (Dcards[2]))
                    Card1_dealer.draw(win)
                    

                    
                    DrandIndex = random.randint(0,len(Ddeck_list) - 1)
                    Dcards = Ddeck_list[DrandIndex]
                    dealer_hand.append(Dcards)
                    Ddeck_list.remove(Dcards)
                    # Display card
                    Card2_dealer = Image(Point(Card1_dealer.getAnchor().getX() + 2, 40), (Dcards[2]))
                    Card2_dealer.draw(win)
                    ### Read a card from the dealers hand using the matrix notation
                    ### Dealerhas two cards, two lists, in his hand_list.  We know that for
                    ### every list (or card) in their hand that in that list index 1
                    ### contains the numeric value of the card.
                    sumDealer = 0
                    for i in range(0, len(dealer_hand)):
                        sumDealer += dealer_hand[i][1]
                        for j in range(0,3):
                            print(dealer_hand[i][j])
                    print("dealer is holding: ", sumDealer)
                    # label score box
                    dealer_lbl = Text(dealer_score.getCenter(), sumDealer)
                    dealer_lbl.setSize(20)
                    dealer_lbl.draw(win)

                    sleep(1)
                    Round = 1
                    # check for winner
                    # champ is variable for winner
                    # status is true or false
                    status, champ = winner(sumPlayer, sumDealer)
                    print(status, champ)
                    if status and champ == 'Player Wins' :
                        champ = 'Player Wins'
                        winner_text = Text((winner_box.getCenter()), champ)
                        winner_text.setSize(25)
                        winner_box.draw(win)
                        winner_text.draw(win)
                        sleep(2)
                        winner_box.undraw()
                        winner_text.undraw()
                        Card1_dealer.undraw()
                        Card2_dealer.undraw()
                        Card1_player.undraw()
                        Card2_player.undraw()
                        rectHit.undraw()
                        rectStand.undraw()
                        dealer_lbl.undraw()
                        player_lbl.undraw()
                        Round = 0
                        sumPlayer = 0
                        sumDealer = 0
                        Sentinel = False
                        Sentinel2 = True
                        break
                    if status == False :
                        Round = 2
                        Sentinel = False
                        
                    
                    if status and champ == 'PUSH' :
                        champ = 'PUSH'
                        winner_text = Text((winner_box.getCenter()), champ)
                        winner_text.setSize(25)
                        winner_box.draw(win)
                        winner_text.draw(win)
                        sleep(2)
                        winner_box.undraw()
                        winner_text.undraw()
                        Card1_dealer.undraw()
                        Card2_dealer.undraw()
                        Card1_player.undraw()
                        Card2_player.undraw()
                        rectHit.undraw()
                        rectStand.undraw()
                        dealer_lbl.undraw()
                        player_lbl.undraw()
                        sumPlayer = 0
                        sumDealer = 0
                        Round = 0
                        Sentinel = False
                        Sentinel2 = True
                        break
                    if status and champ == 'Dealer Black Jack' :
                        loser = 'Dealer Black Jack'
                        loser_text = Text((winner_box.getCenter()), loser)
                        loser_text.setSize(25)
                        loser_box.draw(win)
                        loser_text.draw(win)
                        sleep(2)
                        loser_box.undraw()
                        loser_text.undraw()
                        Card1_dealer.undraw()
                        Card2_dealer.undraw()
                        Card1_player.undraw()
                        Card2_player.undraw()
                        rectHit.undraw()
                        rectStand.undraw()
                        dealer_lbl.undraw()
                        player_lbl.undraw()
                        Round = 0
                        sumPlayer = 0
                        sumDealer = 0
                        Sentinel = False
                        Sentinel2 = True
                        break
                    if status and champ == 'Player Black Jack' :
                        champ = 'Player Black Jack'
                        winner_text = Text((winner_box.getCenter()), champ)
                        winner_text.setSize(25)
                        winner_box.draw(win)
                        winner_text.draw(win)
                        sleep(2)
                        winner_box.undraw()
                        winner_text.undraw()
                        Card1_dealer.undraw()
                        Card2_dealer.undraw()
                        Card1_player.undraw()
                        Card2_player.undraw()
                        rectHit.undraw()
                        rectStand.undraw()
                        dealer_lbl.undraw()
                        player_lbl.undraw()
                        Round = 0
                        sumPlayer = 0
                        sumDealer = 0
                        Sentinel = False
                        Sentinel2 = True
                        break
                    
                    point3 = win.getMouse()
                    if hitBtn(point3, rect3):
                        #### Take 1 card out of the deck_list and put them in the player_hand list
                        randIndex = random.randint(0,len(Pdeck_list) - 1)
                        Pcards = Pdeck_list[randIndex]
                        player_hand.append(Pcards)
                        Pdeck_list.remove(Pcards)
                        sumPlayer += player_hand[i][1]
                        # Display card
                        Card3_player = Image(Point(Card2_player.getAnchor().getX() + 2, 10), (Pcards[2]))
                        Card3_player.draw(win)
                        player_lbl.setText(sumPlayer)
                        sleep(3)
                        # check for winner
                        # champ is variable for winner
                        # status is true or false
                        status, champ = winner(sumPlayer, sumDealer)
                        print(status, champ)
                        if status and champ == 'Player Wins' :
                            champ = 'Player Wins'
                            winner_text = Text((winner_box.getCenter()), champ)
                            winner_text.setSize(25)
                            winner_box.draw(win)
                            winner_text.draw(win)
                            sleep(2)
                            winner_box.undraw()
                            winner_text.undraw()
                            Card1_dealer.undraw()
                            Card2_dealer.undraw()
                            Card1_player.undraw()
                            Card2_player.undraw()
                            Card3_player.undraw()
                            rectHit.undraw()
                            rectStand.undraw()
                            dealer_lbl.undraw()
                            player_lbl.undraw()
                            Round = 0
                            sumPlayer = 0
                            sumDealer = 0
                            Sentinel2 = True
                            break
                        if status == False :
                            loser = 'Dealer Wins'
                            loser_text = Text((winner_box.getCenter()), loser)
                            loser_text.setSize(25)
                            loser_box.draw(win)
                            loser_text.draw(win)
                            sleep(2)
                            loser_box.undraw()
                            loser_text.undraw()
                            Card1_dealer.undraw()
                            Card2_dealer.undraw()
                            Card1_player.undraw()
                            Card2_player.undraw()
                            Card3_player.undraw()
                            rectHit.undraw()
                            rectStand.undraw()
                            dealer_lbl.undraw()
                            player_lbl.undraw()
                            sumPlayer = 0
                            sumDealer = 0
                            Round = 0
                            Sentinel2 = True
                            break
                            
                        if status and champ == 'Push' :
                            champ = 'PUSH'
                            winner_text = Text((winner_box.getCenter()), champ)
                            winner_text.setSize(25)
                            winner_box.draw(win)
                            winner_text.draw(win)
                            sleep(2)
                            winner_box.undraw()
                            winner_text.undraw()
                            Card1_dealer.undraw()
                            Card2_dealer.undraw()
                            Card1_player.undraw()
                            Card2_player.undraw()
                            Card3_player.undraw()
                            rectHit.undraw()
                            rectStand.undraw()
                            dealer_lbl.undraw()
                            player_lbl.undraw()
                            Round = 0
                            sumPlayer = 0
                            sumDealer = 0
                            Sentinel2 = True
                            break
                        if status and champ == 'BUST' :
                            loser = 'BUST'
                            loser_text = Text((winner_box.getCenter()), loser)
                            loser_text.setSize(25)
                            loser_box.draw(win)
                            loser_text.draw(win)
                            sleep(2)
                            loser_box.undraw()
                            loser_text.undraw()
                            Card1_dealer.undraw()
                            Card2_dealer.undraw()
                            Card1_player.undraw()
                            Card2_player.undraw()
                            Card3_player.undraw()
                            rectHit.undraw()
                            rectStand.undraw()
                            dealer_lbl.undraw()
                            player_lbl.undraw()
                            sumPlayer = 0
                            sumDealer = 0
                            Round = 0
                            Sentinel2 = True
                            break
                    point5 = win.getMouse()
                    if quitbtn(btnquit, point5) :
                        # Close the window
                        win.close()
                        # if winner go back to top of loop
                        Round = 2
                        i += 1
                        break
                    point4 = win.getMouse()
                    if standBtn(win.checkMouse(), rect4):
                        # check for winner
                        # champ is variable for winner
                        # status is true or false
                        status, champ = winner(sumPlayer, sumDealer)
                        print(status, champ)
                        if status and champ == 'Player Wins' :
                            champ = 'Player Wins'
                            winner_text = Text((winner_box.getCenter()), champ)
                            winner_text.setSize(25)
                            winner_box.draw(win)
                            winner_text.draw(win)
                            sleep(2)
                            winner_box.undraw()
                            winner_text.undraw()
                            Card1_dealer.undraw()
                            Card2_dealer.undraw()
                            Card1_player.undraw()
                            Card2_player.undraw()
                            rectHit.undraw()
                            rectStand.undraw()
                            dealer_lbl.undraw()
                            player_lbl.undraw()
                            Round = 0
                            sumPlayer = 0
                            sumDealer = 0
                            Sentinel2 = True
                            break
                        if status == False :
                            loser = 'Dealer Wins'
                            loser_text = Text((winner_box.getCenter()), loser)
                            loser_text.setSize(25)
                            loser_box.draw(win)
                            loser_text.draw(win)
                            sleep(2)
                            loser_box.undraw()
                            loser_text.undraw()
                            Card1_dealer.undraw()
                            Card2_dealer.undraw()
                            Card1_player.undraw()
                            Card2_player.undraw()
                            Card3_player.undraw()
                            rectHit.undraw()
                            rectStand.undraw()
                            dealer_lbl.undraw()
                            player_lbl.undraw()
                            sumPlayer = 0
                            sumDealer = 0
                            Round = 0
                            Sentinel2 = True
                            break
                        
                        if status and champ == 'PUSH' :
                            champ = 'PUSH'
                            winner_text = Text((winner_box.getCenter()), champ)
                            winner_text.setSize(25)
                            winner_box.draw(win)
                            winner_text.draw(win)
                            sleep(2)
                            winner_box.undraw()
                            winner_text.undraw()
                            Card1_dealer.undraw()
                            Card2_dealer.undraw()
                            Card1_player.undraw()
                            Card2_player.undraw()
                            rectHit.undraw()
                            rectStand.undraw()
                            dealer_lbl.undraw()
                            player_lbl.undraw()
                            Round = 0
                            sumPlayer = 0
                            sumDealer = 0
                            Sentinel2 = True
                            break
                        if status and champ == 'BUST' :
                            loser = 'BUST'
                            loser_text = Text((winner_box.getCenter()), loser)
                            loser_text.setSize(25)
                            loser_box.draw(win)
                            loser_text.draw(win)
                            sleep(2)
                            loser_box.undraw()
                            loser_text.undraw()
                            Card1_dealer.undraw()
                            Card2_dealer.undraw()
                            Card1_player.undraw()
                            Card2_player.undraw()
                            Cardi_player.undraw()
                            rectHit.undraw()
                            rectStand.undraw()
                            dealer_lbl.undraw()
                            player_lbl.undraw()
                            Round = 0
                            sumPlayer = 0
                            sumDealer = 0
                            Sentinel2 = True
                            break
                                            
        
def winner(sumPlayer, sumDealer):
    playerwins = 'Player Wins'
    playerBJ = 'Player Black Jack'
    dealerwins = 'Dealer Wins'
    dealerBJ = 'Dealer Black Jack'
    BUST = 'BUST'
    PUSH = 'PUSH'
    # determine the winner
    #analyze scores
##if hold then The dealer must draw more cards to any total of 16 or
##less and must stand on any total of 17 or "soft" 17 which is a 17
##including an ace or
##aces that could also be counted as a 7
    if sumPlayer > 21 :
        return True, BUST
    elif sumPlayer == sumDealer :
        return True, PUSH
    elif sumPlayer == 21 and sumDealer != 21 :
        return True, playerBJ
    elif sumPlayer != 21 and sumDealer == 21 :
        return True, dealerBJ
    elif sumPlayer == 21 and sumDealer != 21 :
        return True, playerBJ
    elif sumPlayer > sumDealer and sumPlayer <= 21:
        return True, playerwins
    elif sumDealer > 21 and sumPlayer <= 21 :
        return True, playerwins
    else:
        return False, ''
    
    
def quitbtn(btnquit, point5):
    if point5:
        px, py = point5.getX(), point5.getY()

        x0, y0 = btnquit.getP1().getX(), btnquit.getP1().getY()
        x1, y1 = btnquit.getP2().getX(), btnquit.getP2().getY()

        if ((min(x0, x1) <= px <= max(x0, x1)) and
             (min(y0, y1) <= py <= max(y0, y1))):
            return True
        else:
            return False
    else:
            return False
        
def dealbtn(point2, rect2):
    if point2:
        px, py = point2.getX(), point2.getY()

        x0, y0 = rect2.getP1().getX(), rect2.getP1().getY()
        x1, y1 = rect2.getP2().getX(), rect2.getP2().getY()

        if ((min(x0, x1) <= px <= max(x0, x1)) and
             (min(y0, y1) <= py <= max(y0, y1))):
            return True
        else:
            return False
    else:
            return False
        
def click(win):
    # to figure out what coords are
    for i in range(10):
        p = win.getMouse()
        print("You clicked at... ", p.getX(), p.getY())
    

def play_btnClick(point, rect1):
    
    if point:
        px, py = point.getX(), point.getY()

        x0, y0 = rect1.getP1().getX(), rect1.getP1().getY()
        x1, y1 = rect1.getP2().getX(), rect1.getP2().getY()

        if ((min(x0, x1) <= px <= max(x0, x1)) and
             (min(y0, y1) <= py <= max(y0, y1))):
            return True
        else:
            return False
    else:
            return False


def hitBtn(point3, rect3):
    if point3:
        px, py = point3.getX(), point3.getY()

        x0, y0 = rect3.getP1().getX(), rect3.getP1().getY()
        x1, y1 = rect3.getP2().getX(), rect3.getP2().getY()

        if ((min(x0, x1) <= px <= max(x0, x1)) and
             (min(y0, y1) <= py <= max(y0, y1))):
            return True
        else:
            return False
    else:
            return False
    
def standBtn(point4, rect4):
    if point4:
        px, py = point4.getX(), point4.getY()

        x0, y0 = rect4.getP1().getX(), rect4.getP1().getY()
        x1, y1 = rect4.getP2().getX(), rect4.getP2().getY()

        if ((min(x0, x1) <= px <= max(x0, x1)) and
             (min(y0, y1) <= py <= max(y0, y1))):
            return True
        else:
            return False
    else:
            return False
    






        

main()
