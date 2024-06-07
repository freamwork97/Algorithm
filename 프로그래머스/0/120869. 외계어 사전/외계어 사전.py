def solution(spell, dic):
    sorted_spell = sorted(spell)

    for w in dic:
        if sorted(w) == sorted_spell:
            return 1

    return 2
