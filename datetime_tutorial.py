import datetime

print(datetime.date.today())
# error
# today = datetime.date.today().split("-")
today = datetime.date.today()
today = str(today)
todaylist = today.split("-")
print(todaylist)

for i, today in enumerate(todaylist):
    todaylist[i] = today.lstrip("0")
print(todaylist)

print(f"{todaylist[0]}年{todaylist[1]}月{todaylist[2]}日")

print(datetime.datetime.now())
print(datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S"))
