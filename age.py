from datetime import datetime

today = datetime.now()
set_date = input("Enter date.").split("-")
diff = today.year - int(set_date[-1])
if int(set_date[1]) > today.month:
  diff -= 1
elif int(set_date[1]) == today.month:
  diff -= 1 if int(set_date[0]) > today.day else 0
print (diff)
