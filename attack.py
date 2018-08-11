
def isSurrounded(closeEnemies):
    surroundedThreshold = 2
    return len(closeEnemies) >= surroundedThreshold

def shouldCleave(closeEnemies):
    return isSurrounded(closeEnemies) and hero.isReady("cleave")

def attackSingleEnemy(enemy):
    if(enemy):
        distance = hero.distanceTo(enemy)
        if distance > 20 and hero.isReady("dash"):
            hero.dash(enemy)
        else:
            hero.attack(enemy)
    else:
        hero.moveXY(109,69)

def attackEnemies(closeEnemies, allEnemies):
    if(shouldCleave(closeEnemies)):
        hero.cleave()
    else:
        enemy = hero.findNearest(allEnemies)
        attackSingleEnemy(enemy)

def enemiesCloserThan(enemies, distance):
    return [ enemy for enemy in enemies if hero.distanceTo(enemy) < distance ]

def feelingFearless():
    return hero.health > 200

def moveToward(item):
    if(hero.isReady("dash")):
        hero.dash(item.pos)
    else:
        hero.move(item.pos)

def healUp(nearestItem):
    moveToward(nearestItem.pos)

# Stay alive longer than the enemy hero!
while True:
    allEnemies = hero.findEnemies()
    closeEnemies = enemiesCloserThan(allEnemies, 10)
    item = hero.findNearestItem()
    
    # Devise your own strategy. Be creative
    if(item and not feelingFearless()):
        healUp(item)
    else:
        attackEnemies(closeEnemies, allEnemies)

