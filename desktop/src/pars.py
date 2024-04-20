# попытка запарсить файл

problem = []

with open('test.txt', 'rt', encoding='utf-8') as src:
    for stroke in src:
        if stroke == '-\n' or stroke == '===\n':
            problem.append(stroke.rstrip())
        else:
            problem.append(stroke)


question = ''
answer = ''
for i in range(0, len(problem)-1):
    try:
        while True:
            if problem[i] == '-':
                print(problem)
                del problem[i]
                print(problem)
                print('-----')
                break
            question = question + problem.pop(i)
        while True:
            if problem[i] == '===':
                print(problem)
                del problem[i]
                print(problem)
                print('=====')
                break
            answer = answer + problem.pop(i)
    except IndexError:
        break
# print(question)
# print(answer)
