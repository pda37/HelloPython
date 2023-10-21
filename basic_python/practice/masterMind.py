def masterMind(solution, guess):
    real, fake = 0, 0
    solution_list = []
    guess_list = []
    for i in range(len(solution)):
        if solution[i] == guess[i]:
            real += 1
        else:
            solution_list.append(solution[i])
            guess_list.append(guess[i])
    print(real, solution_list, guess_list)
    for s in guess_list:
        if s in solution_list:
            fake += 1
            solution_list.remove(s)
    return [real, fake]


print(masterMind("RRWR", "RWRR"))
