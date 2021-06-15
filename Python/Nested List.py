'''
Given the names and grades for each student in a class of N students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

Note: If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line.
'''

if __name__ == '__main__':
    records = []
    N = int(input())
    for _ in range(N):
        name = input()
        score = float(input())
        records.append([name, score])

    c1, c2 = zip(*records)
    c2 = list(set(c2))
    c2 = sorted(c2)
    temp = []
    for i in range(N):
        if records[i][1] == c2[1]:
            temp.append(records[i][0])

    temp = sorted(temp)
    for i in temp:
        print(i)