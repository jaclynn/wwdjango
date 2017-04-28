#cookie.py

#Create an object called Cookie
#It's standard to capitalize object names
class Cookie:
    #This function is aka constructor, generator, factory...
    def __init__(self,shape,type,toppings,calories):
        self.shape = shape
        self.type = type
        self.toppings = toppings
        self.calories = calories
        self.eaten = False
    #Override the string function so it looks good when
    #we pass a cookie into the print() function
    def __str__(self):
        return "I am a "+self.shape+" "+self.type+" cookie with "+self.toppings
    #Getters and setters abstract the program so that
    #properties/attributes are not accessed directly
    def getShape(self):
        return self.shape

    def getType(self):
        return self.type

    def getToppings(self):
        return self.toppings

    def getCalories(self):
        return self.calories

    def isEaten(self):
        return self.eaten

    def eat(self):
        self.eaten = True

#Create CookieJar Object
class CookieJar:
    def __init__(self, capacity):
        self.capacity = capacity
        self.numOfCookies = 0
        self.empty = True
        self.listOfCookies = []

    def __str__(self):
        if self.empty==True:
            return "empty cookie jar"
        else:
            return "full cookie jar"

    #Fill the cookie jar with random cookies
    def fillJar(self):
        from random import choice,randint
        print(self.capacity)
        for i in range(randint(1,self.capacity)):
            type = choice(["choc chip","sugar","oatmeal","nobake"])
            toppings = choice(["sprinkles","chips","frosting","nuts","candy","raisins"])
            shape = choice(["round","square","star","triangle"])
            calories = randint(40,80)
            c = Cookie(shape,type,toppings,calories)
            self.listOfCookies.append(c)
        self.numOfCookies = len(self.listOfCookies)
        self.empty=False

    #display the cookies in a friendly way
    def showCookies(self):
        for cookie in self.listOfCookies:
            print(cookie)

    #use the list pop() method to extract the last cookie added
    def takeACookie(self):
        if len(self.listOfCookies)==0:
            return "No more cookies!"
        else:
            return self.listOfCookies.pop()

#main program
#This code only runs if cookie.py is run directly
#If this file is imported by another program, this code
#is ignored
if __name__=="__main__":
    cj = CookieJar(20)
    print(cj)
    cj.fillJar()
    print(cj)
    cj.showCookies()
    print("\n\nNOW TAKING A COOKIE:\n")
    print(cj.takeACookie())
