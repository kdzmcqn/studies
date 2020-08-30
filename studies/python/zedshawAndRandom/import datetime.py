import datetime

print(datetime.date.today())

print(datetime.date.today().year)
print(datetime.date.today().month)
print(datetime.date.today().day)

print(datetime.date.isoformat(datetime.date.today()))
# isoformat converts to string

right_this_minute = datetime.today().minute
# today() returns a time object which contains pieces of information about current time
#thus are the current time attributes:  .minute
#we appended .minute

#det current time
time_now = datetime.today()
#extract the minute
right_this_minute = time_now.minute
