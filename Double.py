total_time_minutes = 0
    total_time_hours = 0
    individual_times = []

    for _ in range(applicants):
        PORTAL_time_avg = random.randint(60, 90)
        PORTAL_total_minutes = PORTAL_time_avg / 60
        total_time_minutes += PORTAL_total_minutes
        individual_times.append(PORTAL_time_avg)

    PORTAL_total_time_hours = total_time_minutes / 60

    try:
        Portal_TimeConsume = (PORTAL_total_time_hours / float(Portal))

        # Convert Portal_TimeConsume into hours and minutes
        hours = int(Portal_TimeConsume)
        minutes = int((Portal_TimeConsume - hours) * 60)

        print("Total Portal Time: {} hours and {} minutes".format(hours, minutes))

        # Print individual times
        for i, time_avg in enumerate(individual_times, 1):
            individual_seconds = time_avg
            individual_minutes = individual_seconds // 60
            individual_seconds = individual_seconds % 60


            #Print each individual TimeFrame
            # print("Applicant {}: {} seconds ({} minutes and {} seconds)".format(i, time_avg, individual_minutes,individual_seconds))

    except ValueError:
        Portal_TimeConsume = (PORTAL_total_time_hours / 1)

        # Convert Portal_TimeConsume into hours and minutes
        hours = int(Portal_TimeConsume)
        minutes = int((Portal_TimeConsume - hours) * 60)

        print("Total Portal Time: {} hours and {} minutes".format(hours, minutes))

    except ZeroDivisionError:
        Portal_TimeConsume = (PORTAL_total_time_hours / 1)

        # Convert Portal_TimeConsume into hours and minutes
        hours = int(Portal_TimeConsume)
        minutes = int((Portal_TimeConsume - hours) * 60)

        print("Total Portal Time: {} hours and {} minutes".format(hours, minutes))
