def average(salaries):
    salaries.pop(salaries.index(min(salaries)))
    salaries.pop(salaries.index(max(salaries)))
    
    return sum(salaries) / len(salaries)

average([3000, 2000, 1000])

# we expect average salary ignoring max and min salary value