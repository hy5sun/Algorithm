def solution(bandage, health, attacks):
    full_time = attacks[-1][0]
    full_health = health
    cnt = 0

    for i in range(full_time + 1):
        if health <= 0:
            return -1

        if i == attacks[0][0]:
            health -= attacks[0][1]
            attacks.pop(0)
            cnt = 0
        else:
            health += bandage[1]
            if health > full_health:
                health = full_health
            cnt += 1

        if cnt == bandage[0]:
            health += bandage[2]
            if health > full_health:
                health = full_health
            cnt = 0

    if health <= 0:
        return -1

    return health
