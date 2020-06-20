# 6장 과제

# human 클래스를 만들고,
# 이 클래스를 상속받는 player 클래스, npc 클래스, enemy 클래스를 만들어주세요

# human 클래스에는 이름, HP, MP 속성과 안녕하세요를 출력하는 meet 메소드가 있어야하고
# player 클래스에는 AD 속성과 player 객체의 AD값 - enemy 객체의 DP값 만큼
# enemy 객체의 HP를 감소시키는 att메소드가 있어야합니다.
# enemy 클래스에는 DP 속성이 있어야 합니다.


# 그 다음에는 player, npc, enemy 객체를 자유롭게 1개씩 만들고

# 사용자에게 입력을 받아 1을 입력받으면 player과 npc의 meet 메소드가 실행되고
# 2를 입력받으면 att메소드가 실행되어 enemy객체의 HP가 감소하도록 만들어주세요
# enemy의 HP 값이 0이되면 게임이 종료되어야 합니다.
# att메소드는 반드시 2번 이상 실행되어야 합니다. (공격력이 너무 높아서 한방에 끝나게 하지 말아주세요.)

class human:
    def __init__(self, name, HP, NP):
         self.name=name
         self.HP=HP
         self.NP=NP
    def meet(self):
        printf("안녕하세요")

class player(human):
    def __init__(self, name, HP, NP, AD):
        super().__init__(self, name, HP, NP)
        self.AD=AD
 
    def att(self,enemy):
        if self.HP>=70:
            enemy.HP= enemy.HP-(self.AD - enemy.DP)
            self.NP =NP-70
            print("공격에 성공하셨습니다.")
            print("플레이어의 수치 : ",self.NP)
            print("적의 수치 : ",enemy.HP)

        else:
            print("수치가 적습니다.")
    def meet(self):
        print("만나서 반갑습니다.")

class npc(human):
    pass
class enemy(human):
    DP=70

player1=player('철수', 150, 150)
npc1=npc("영희", 150, 150)
dra1=enemy("드래곤", 150, 150)

while TRUE:
    number=input("npc와 만나고 싶다. : 1, 공격하고 싶다. : 2 둘 중 하나를 고르시오.")

    if number =='1':
        player1.meet()
        npc1.meet()
    elif number =='2':
        player1.att()
        print("이겼다!")
        break
    else:
        print("잘못 입력하셨습니다.")