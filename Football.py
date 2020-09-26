class Football:
        
    def __init__(self, name , pos):
        self.name = name
        self.pos = pos

    def inf(self):
        print( "Игрок -" , self.name,"Позиция -"  ,self.pos )    

def main():
    team =str(input())
    Fp1 = Football(input(),input() )
    Fp2 = Football(input(),input() )
    Fp3 = Football(input(),input() )
    Fp4 = Football(input(),input() )
    Fp5 = Football(input(),input() )
    Fp6 = Football(input(),input() )
    Fp7 = Football(input(),input() )
    Fp8 = Football(input(),input() )
    Fp9 = Football(input(),input() )
    Fp10 = Football(input(),input() )  
    Fp11 = Football(input(),input() )

    print("Команда -",team) 
    Fp1.inf()
    Fp2.inf()
    Fp3.inf()
    Fp4.inf()
    Fp5.inf()
    Fp6.inf()      
    Fp7.inf()
    Fp8.inf()
    Fp9.inf()
    Fp10.inf()
    Fp11.inf()


main()             
