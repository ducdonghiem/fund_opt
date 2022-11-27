class agriculture():
    # return the sublist of a list
    def sublist(lst):
        if lst == []:
            return [[]]
        else:
            x = agriculture.sublist(lst[1:])
            return x + [[lst[0]] + y for y in x]

    # eliminate unqualified list
    def candidate(k):
        lst = agriculture.sublist(avai_farm[k])
        # constraint of m and M
        for i in lst[1:]:
            d = 0
            for j in i:
                d += production[j - 1]    
            if d < m or d > M:
                lst.remove(i)        
        return lst

    # backtracking
    def solve(k):
        for i in agriculture.candidate(k):
            sol[k] = i
            if k == 4:
                lst_sol.append(sol[:])
            else:
                agriculture.solve(k+1)

    # final elimination    
    def result():
        # check for farms occuring 2 or more.
        for i in lst_sol[:]:
            test = []
            for j in i:
                test += j 
            for l in test[:]:
                if test.count(l) > 1:
                    lst_sol.remove(i)
                    break  
        # check for whether there are enough farms.  
        for i in lst_sol[:]:
            s = 0
            for j in i:
                s += len(j)
            if s != 8:
                lst_sol.remove(i) 
        # calculate the final result.
        lst_opt_sol = []
        lst_val = []
        opt_val = 100
        for i in lst_sol:
            maxsum = 0
            minsum = M
            for j in i:
                sum_ = sum(list(map(lambda x: production[x-1], j)))
                if  sum_ > maxsum:
                    maxsum = sum_
                if sum_ < minsum:
                    minsum = sum_
            value = maxsum - minsum
            if value <= opt_val:
                if value == opt_val:
                    lst_opt_sol.append(i)
                else:
                    opt_val = value
                    lst_opt_sol = []
                    lst_opt_sol.append(i)
            lst_val.append(value)
        return (lst_sol, lst_val, lst_opt_sol, opt_val)


def main():
    global m, M, avai_farm, production, sol, lst_sol
    # available farm in each day
    # avai_farm = [[3, 4, 5, 8],
    #             [1, 3, 4, 5, 7, 8],
    #             [1, 2, 3, 4, 5, 7],
    #             [1, 2, 4, 6, 7],
    #             [4, 6, 7]]
    avai_farm = [[2, 3],
                [1, 2, 3, 6],
                [1, 3, 4, 6, 8],
                [1, 4, 5, 7, 8],
                [5, 7, 8]]
    # production of each farm
    production = [6, 8, 3, 1, 5, 7, 2, 4]
    # production = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    m = 10
    M = 14

    sol = [0]*5
    lst_sol = []

    agriculture.solve(0)
    print('All solutions:')
    print(agriculture.result()[0])
    print('All values:')
    print(agriculture.result()[1])
    print('Optimal solutions:')
    print(agriculture.result()[2])
    print('Optimal value:')
    print(agriculture.result()[3])

main()