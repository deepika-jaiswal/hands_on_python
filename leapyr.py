y=int(input())
if((y%400==0 or y%4==0) and y%100!=0):
  print("year is leap")
else:
  print("not leap year")
