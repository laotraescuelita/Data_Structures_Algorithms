def job_sequencing_with_deadlines(jobs):    
    # Sort jobs based on their profits in descending order
    jobs.sort(key=lambda x: x[2], reverse=True)  

    max_deadline = max( jobs, key=lambda x: x[1])[1]    
    schedule = [None] * max_deadline    
    total_profit = 0

    for job in jobs:
        deadline = job[1]
        while deadline > 0 and schedule[deadline - 1] is not None:
            deadline -= 1

        if deadline > 0:
            schedule[deadline - 1] = job[0]
            total_profit += job[2]

    return schedule, total_profit


jobs = [('J1', 2, 20), ('J2', 2, 15), ('J3', 1, 10), ('J4', 3, 5), ('J4', 3, 1)]
schedule, profit = job_sequencing_with_deadlines(jobs)
print("Scheduled Jobs:", schedule)
print("Total Profit:", profit)
