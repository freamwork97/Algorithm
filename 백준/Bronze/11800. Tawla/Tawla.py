T = int(input())
dice_name = {1: 'Yakk', 2: 'Doh', 3: 'Seh',
             4: 'Ghar', 5: 'Bang', 6: 'Sheesh'}
double_dice_name = {1: 'Habb Yakk', 2: 'Dobara', 3: 'Dousa',
                    4: 'Dorgy', 5: 'Dabash', 6: 'Dosh'}

for test_case in range(1, T + 1):
    a, b = map(int, input().split())
    if a == b:
        print(f'Case {test_case}: {double_dice_name[a]}')
    elif (a, b) == (6, 5) or (a, b) == (5, 6):
        print(f'Case {test_case}: Sheesh Beesh')
    else:
        print(f'Case {test_case}: {dice_name[max(a, b)]} {dice_name[min(a, b)]}')