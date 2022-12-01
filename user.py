class User:
    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0

jesse = User("Jesse", "Clise", "jesse@bark.com", 4)
'''
display_info(self) - Have this method print 
all of the users' details 
'''

def display_info(self):
    print(f"User information: First Name: {self.first_name} Last Name: {self.last_name} Email: {self.email} Age: {self.age}")

display_info(jesse)

'''
enroll(self) - Have this method change the user's
member status to True and set their gold card points to 200
'''
def enroll(self):
    self.gold_card_points = 200
    print(f"{self.first_name} has a gold card points balance of: {self.gold_card_points}")

enroll(jesse)

#Make 2 more instances of the User class.
lily = User("Lily", "Clise", "lily@imeowat4am@gmail.com", 4)
richard = User("Richard", "Hendrix", "rhend@piedpiper.com", 35)

#Implement the spend_points(self, amount) method
#Have the first user spend 50 points
'''
spend_points(self, amount) - have this method 
decrease the user's points by the amount specified.
'''
def spend_points(self, amount):
    new_balance = self.gold_card_points - (amount)
    self.gold_card_points = new_balance
    if amount >= self.gold_card_points:
        print("Insufficient funds")
    if amount < self.gold_card_points:
        print(f"{self.first_name} has a gold card points balance of {new_balance}")

enroll(lily)
spend_points(lily, 300)

#Have the second user enroll. Have the second user spend 80 points.

enroll(richard)
spend_points(richard, 80)

display_info(jesse)
display_info(lily)
display_info(richard)








