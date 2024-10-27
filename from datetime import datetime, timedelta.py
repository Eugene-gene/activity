from datetime import datetime, timedelta # import the date and time from libraries

# Get the current date and time
current_time = datetime.now() # datetime.now is function to get the date and time

# Calculate the date and time one week (7 days) from now
one_week_later = current_time + timedelta(weeks=1) # timedelta object is the duration or intervals between two points

# Print the current date and time
print("Current date and time:", current_time)

# Print the date and time one week from now
print("Date and time one week from now:", one_week_later)
