grade_values = {
    'A+': 4.5, 'A0': 4.0, 'B+': 3.5, 'B0': 3.0,
    'C+': 2.5, 'C0': 2.0, 'D+': 1.5, 'D0': 1.0, 'F': 0.0
}

total_credits = 0.0
total_points = 0.0

for _ in range(20):
    _, credits, grade = input().split()
    credits = float(credits)

    if grade != 'P':
        total_credits += credits
        total_points += grade_values[grade] * credits

print(f'{total_points / total_credits:.6f}')