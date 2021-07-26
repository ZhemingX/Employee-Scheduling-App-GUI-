from ortools.sat.python import cp_model
from util import list_split

depart_cons = [set([]) for i in range(39)]
depart_cons[0] |= set([1,3,5,7])
depart_cons[2] |= set([i for i in range(20)])

#print(depart_cons)

def schedule_departs(num_departs, num_shifts, num_days, depart_cons):

    all_departs = range(num_departs)
    all_shifts = range(num_shifts)
    all_days = range(num_days)
    # Creates the model.
    model = cp_model.CpModel()

    # Creates shift variables.
    # shifts[(n, d, s)]: depart 'n' works shift 's' on day 'd'.
    shifts = {}
    for n in all_departs:
        for d in all_days:
            for s in all_shifts:
                shifts[(n, d, s)] = model.NewBoolVar('shift_n%id%is%i' % (n, d, s))

    # Each shift is assigned to exactly one nurse in the schedule period.
    for d in all_days:
        for s in all_shifts:
            model.Add(sum(shifts[(n, d, s)] for n in all_departs) == 1)

    # Each depart works at most one shift per day.
    for n in all_departs:
        for d in all_days:
            model.Add(sum(shifts[(n, d, s)] for s in all_shifts) <= 1)

    # Try to distribute the shifts evenly

    # each depart works at least 3 times each month
    min_shifts_per_depart = 3
    for n in all_departs:
        num_shifts_worked = 0
        for d in all_days:
            for s in all_shifts:
                num_shifts_worked += shifts[(n, d, s)]
        model.Add(min_shifts_per_depart <= num_shifts_worked)


    # Each depart has at most one shift every 4 days considering the reality
    for n in all_departs:
        for days_split in list_split(all_days, 4):
            num_shifts_worked = 0
            for d in days_split:
                for s in all_shifts:
                    num_shifts_worked += shifts[(n, d, s)]
            model.Add(num_shifts_worked <= 1)

    # Each depart consider its own constraints
    # each depart should not schedule work in any days in its constraints
    for n in all_departs:
        num_shifts_worked = 0
        for d in depart_cons[n]:
            for s in all_shifts:
                num_shifts_worked += shifts[(n, d, s)]
        model.Add(num_shifts_worked == 0)
    
    # Creates the solver and solve.
    solver = cp_model.CpSolver()

    status = solver.Solve(model)
    

    if status == cp_model.OPTIMAL:
        res = []
        for d in all_days:
            row = [0 for i in all_shifts]
            for n in all_departs:
                is_working = False
                for s in all_shifts:
                    if solver.Value(shifts[(n,d,s)]):
                        is_working = True
                        row[s] = n
                if not is_working:
                    continue
            res.append(row)
        
        #print(res)
            
        # for d in all_days:
        #         print('Day %i' % d)
        #         for n in all_departs:
        #             is_working = False
        #             for s in all_shifts:
        #                 if solver.Value(shifts[(n,d,s)]):
        #                     is_working = True
        #                     print('  Nurse %i works shift %i' % (n, s))
        #             if not is_working:
        #                 continue
        
        return (True, res)
    
    else:
        return (False, [])



#schedule_departs(37,6,31,depart_cons)