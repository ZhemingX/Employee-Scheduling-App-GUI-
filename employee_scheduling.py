from ortools.sat.python import cp_model
from util import list_split

def schedule_departs(depart_list, num_shifts, num_days, depart_cons):

    # exclude non-use departs
    depart_list_copy = depart_list[:]
    num_departs_copy = len(depart_list_copy)
    depart_list_copy = [depart_list_copy[i] for i in range(num_departs_copy) if len(depart_cons[i]) != num_days]
    depart_cons_copy = [depart_cons[i] for i in range(num_departs_copy) if len(depart_cons[i]) != num_days]
    num_departs = len(depart_list_copy)
    #
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
    # Each depart (constraint days <= 20) has at most one shift every 4 days considering the reality
    for n in all_departs:
        if len(depart_cons_copy[n]) <= 20:
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
        for d in depart_cons_copy[n]:
            for s in all_shifts:
                num_shifts_worked += shifts[(n, d, s)]
        model.Add(num_shifts_worked == 0)
    
    # Each depart (constraint days > 20) has shift in each non-constraint day
    for n in all_departs:
        if len(depart_cons_copy[n]) > 20:
            num_shifts_worked = 0
            for d in all_days:
                for s in all_shifts:
                    num_shifts_worked += shifts[(n, d, s)]
            model.Add(num_shifts_worked == (num_days - len(depart_cons_copy[n])))
    
    # Each depart (no constraint days) has at least 5 shifts each month
    for n in all_departs:
        if len(depart_cons_copy[n]) == 0:
            num_shifts_total = 0
            for d in all_days:
                for s in all_shifts:
                    num_shifts_total += shifts[(n, d, s)]
            model.Add(num_shifts_total >= 5)
            
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
            
        return (True, res, depart_list_copy)
    
    else:
        return (False, [], [])

