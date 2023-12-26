import random
#1~50
#玩家猜5次
#猜對提前離開
#猜錯提示答案
quest=random.randint(1,50)
print(quest)
for i in range(5):
    ans=int(input('guess number(1~50)'))
    if ans==quest:
        print('bingo!') 
        break
    else:
        print('wrong number~')   
    
