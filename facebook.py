Facebook={"Ashik":{"hrithik_don","hacker_venkat","bharathi_SWEET","captain_SP","leader_raja","police_ravi","animal_dinesh","friendly_maha"},
"Salman":{"coder_ashik","hacker_venkat","finance_vidhya","C_J","IT_guy","Football_guy","bharathi_SWEET","leader_raja","animal_dinesh"},
"Dinesh":{"hacker_venkat","arnolad_arun","snake_sneha","bharathi_SWEET","leader_raja","animal_dinesh","bolt_ritesh","J_D","photo_rv"}}

class Fb:
    print("*************HELLO ALL****************")

    def __init__(self):
        print("List Of Friends :")
        print("*****************")
        print("1.Ashik")
        print("2.Salman")
        print("3.Dinesh")
        print("*****************")
        self.friendname=input("choose the friend : ")
        
        print("*****************")

    def menu(self):
        if isinstance(self.friendname,str):
            if self.friendname in Facebook:
                friend=self.friendname
                value=Facebook.get(self.friendname)
                for i in value:
                    print(f"{i} ")

            else :
                raise ValueError("data not present")
        else:
            raise TypeError("invalid datatype")

    def common(self):
        
         print("*****************")
         inpt=input("Do you want to see the common friends : yes or no ? ")
         if(inpt=='y'):
             count=0
             name=input("Enter the name:")
             for i in Facebook:
                 if(name in Facebook[i]):
                     count=count+1
             print("The Number Of Common Friends:",count)
                     

mutual=Fb()
mutual.menu()
mutual.common()
         
