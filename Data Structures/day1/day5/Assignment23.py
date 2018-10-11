#DSA-Tryout
import random
def generate_cards_per_type(card_type):
    #Remove pass and write your logic here
    lst=[2,3,4,5,6,7,8,9,10,'J','Q','K','A']
    card_list=[]
    for i in lst:
        card_list.append(card_type+str(i))
    return card_list

def generate_card_deck():
    #Remove pass and write your logic here
    lst1=['C','D','H','S']
    new_list=[]
    for i in lst1:
        new_list+=generate_cards_per_type(i)
    return new_list
def shuffle_card_deck(cards_list):
    #Remove pass and write your logic here
    random.shuffle(cards_list)
    return cards_list

def sort_cards_of_each_player(card_list):
    #Remove pass and write your logic here
    return card_list.sort()
    

def allocate_cards_to_players(cards_list):
    #Remove pass and write your logic here
    player1=[]
    player2=[]
    player3=[]
    player4=[]
    
    for i in range(0,len(cards_list),4):
        player1.append(cards_list[i])
        player2.append(cards_list[i+1])
        player3.append(cards_list[i+2])
        player4.append(cards_list[i+3])
    dict1={'player1':player1,'player2':player2,'player3':player3,'player4':player4}
    return dict1
def prepare_cards():
    #Remove pass and write your logic here
    cards_list=generate_card_deck()
    
    dict=allocate_cards_to_players(shuffle_card_deck(cards_list))
    for x,y in dict.items():
        sort_cards_of_each_player(y) 
        if('CA' in y):
            return x

first_player=prepare_cards()
print("The first player is:",first_player)