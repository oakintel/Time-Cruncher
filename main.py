def add_time(start, duration, day_of_week=False):

    Array_days_of_week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

    Index_days_of_week = {"sunday": 0, "monday": 1, "tuesday":2, "wednesday":3, "thursday":4, "friday":5, "saturday":6}

    # Create a space to partition all the variables of the proposed duration 
    duration_tuple = duration.partition(":")
  
    # print(duration_tuple)
    duration_hours = int(duration_tuple[0])
    duration_minutes = int(duration_tuple[2])

    # Create a space to partition all the sections of the current time
    start_tuple = start.partition(":")
  
    # Since the section after the ':' is OO PM we need to partition it again
    start_minutes_tuple = start_tuple[2].partition(" ")
  
    # Now, we can extract the hour, minutes, and meriddian
    start_hours = int(start_tuple[0])
    start_minutes = int(start_minutes_tuple[0])
    meridian = start_minutes_tuple[2]

    # We create a flip section to continuously transtion from AM to PM as required
    meridian_flip = {"AM":"PM", "PM":"AM"}
    amount_of_days = int(duration_hours / 24)

    # Resolve the Minutes
    total_minutes = start_minutes + duration_minutes
    # If total_minutes>60; we need to increase the hours by 1
    if (total_minutes >= 60):
      start_hours += 1
      total_minutes = total_minutes % 60

    # We need to understand when to flip ams and pms
    amount_of_meridian_flips = int((start_hours + duration_hours)/12)
    end_hours = (start_hours + duration_hours) % 12

    #We add some cosmetic solutions to the problem here
    total_minutes = total_minutes if total_minutes > 9 else "0" + str(total_minutes)
    end_hours = end_hours = 12 if end_hours == 0 else end_hours
    if(meridian == "PM" and start_hours + (duration_hours % 12) >= 12):
      amount_of_days += 1

    #Flip AM and PM depending on the transition of the 12 hour clock
    meridian = meridian_flip[meridian] if amount_of_meridian_flips % 2 == 1 else meridian

    #Return the time we need
    returnTime = str(end_hours) + ":" + str(total_minutes) + " " + meridian

    #Iterate for the days of the week
    if(day_of_week):
      day_of_week = day_of_week.lower()
      Index = int((Index_days_of_week[day_of_week]) + amount_of_days) % 7
      new_day = Array_days_of_week[Index]
      returnTime += ", " + new_day
      
    if(amount_of_days == 1):
      return returnTime + " " + "(next day)"
    elif(amount_of_days > 1):
      return returnTime + " (" + str(amount_of_days) + " days later)"

    return returnTime

#Insert whatever time you are interested in adding and watch the magic happen
print(add_time("3:00 PM", "250:100000000000"))