#DSA-Assgn-12

#This assignment needs DataStructures.py file in your package, you can get it from resources page

from res.DataStructures import Stack, Queue

class Ball:
    def __init__(self,color,name):
        self.__color=color
        self.__name=name

    def __str__(self):
        return (self.__color+" "+self.__name)

    def get_color(self):
        return self.__color

    def get_name(self):
        return self.__name

class Game:
    def __init__(self,ball_stack):
        self.ball_container=ball_stack
        self.red_balls_container=Stack(2)
        self.green_balls_container=Stack(2)
        self.blue_balls_container=Stack(2)
        self.yellow_balls_container=Stack(2)
    def grouping_based_on_color(self):
        while not self.ball_container.is_empty():
            ele=self.ball_container.pop()
            if(ele.get_color()=='Red'):
                self.red_balls_container.push(ele)
            elif(ele.get_color()=='Blue'):
                self.blue_balls_container.push(ele)
            elif(ele.get_color()=='Green'):
                self.green_balls_container.push(ele)
            elif(ele.get_color()=='Yellow'):
                self.yellow_balls_container.push(ele)
    def rearrange_balls(self,color):
        if(color=='Red'):
            red_list=[]
            while not self.red_balls_container.is_empty():
                red_list.append(self.red_balls_container.pop())
            red_list.sort(key=lambda nam:nam.get_name(), reverse=False)
            for i in red_list[::-1]:
                self.red_balls_container.push(i)
        elif(color=='Blue'):
            blue_list=[]
            while not self.blue_balls_container.is_empty():
                blue_list.append(self.blue_balls_container.pop())
            blue_list.sort(key=lambda nam:nam.get_name(), reverse=False)
            for i in blue_list[::-1]:
                self.blue_balls_container.push(i)
        elif(color=='Green'):
            green_list=[]
            while not self.green_balls_container.is_empty():
                green_list.append(self.green_balls_container.pop())
            green_list.sort(key=lambda nam:nam.get_name(), reverse=False)
            for i in green_list[::-1]:
                self.green_balls_container.push(i)
        elif(color=='Yellow'):
            yellow_list=[]
            while not self.yellow_balls_container.is_empty():
                yellow_list.append(self.yellow_balls_container.pop())
            yellow_list.sort(key=lambda nam:nam.get_name(), reverse=False)
            for i in yellow_list[::-1]:
                self.yellow_balls_container.push(i)
                
    def display_ball_details(self,color):
        pass
#Implement Game class here

#Use different values to test your program
ball1=Ball("Red","A")
ball2=Ball("Blue","B")
ball3=Ball("Yellow","B")
ball4=Ball("Blue","A")
ball5=Ball("Yellow","A")
ball6=Ball("Green","B")
ball7=Ball("Green","A")
ball8=Ball("Red","B")
ball_list=Stack(8)
ball_list.push(ball1)
ball_list.push(ball2)
ball_list.push(ball3)
ball_list.push(ball4)
ball_list.push(ball5)
ball_list.push(ball6)
ball_list.push(ball7)
ball_list.push(ball8)

#Create objects of Game class, invoke the methods and test the program