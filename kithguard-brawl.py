# Survive the waves of ogres.
# If you win, the level gets harder, and gives more rewards.
# If you lose, you must wait a day to re-submit.
# Each time you submit gives a new random seed.
while True:
    enemy = hero.findNearestEnemy()
    if not enemy:
        hero.moveXY(40,36)
    elif enemy.type is "thrower":
        hero.attack(enemy)
    elif hero.isReady("cleave") and hero.distanceTo(enemy) < 10:
        hero.cleave(enemy)
    else:
        hero.attack(enemy)
        
