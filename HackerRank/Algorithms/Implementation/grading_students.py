def grading_students(grades):
    for i in range(len(grades)):
        if grades[i] <= 37:
            continue
        
        needed = 5 - (grades[i] % 5)
        if needed <= 2:
            grades[i] += needed

    return grades

if __name__ == "__main__":
    n = int(input())
    grades = []
    for _ in range(n):
        grades.append(int(input()))

    result = grading_students(grades)

    print(*result, sep='\n')