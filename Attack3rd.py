import random
plyrin = input("Your character: Magic/Physical/Defender ")
PlayerPower = plyrin
PlayerDamage = 0
PlayerHp = 100
PlayerDefense = PlayerHp
enemyhp = 100

enemyAttack = random.randint(1, 10)

def Magic():
    return 10
      
def Physical():
    return 10

def Defender():
    return 10
    
if PlayerPower == "Magic":
    print("You have Magic Power now!!")
    PlayerDamage += Magic()
elif PlayerPower == "Physical":
    print("Physical Power")
    PlayerDamage += Physical()
elif PlayerPower == "Defender":
    print("You are now a defender")
    PlayerDefense += Defender()
else:
    print("Pick a valid option")         

while enemyhp > 0:
    PlayerAttack = input("Attack or Defend? ")
    if PlayerAttack == "attack":
        enemyhp -= PlayerDamage
        print("Enemies Hp is: "+str(enemyhp))
        PlayerHp -= enemyAttack
        print("your hp is: "+str(PlayerHp))
    elif PlayerAttack == "defend":
        PlayerDefense += 10
    else:
        print("Invalid action")

print("Enemy died")