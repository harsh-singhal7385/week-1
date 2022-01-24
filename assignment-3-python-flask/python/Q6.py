from datetime import date

start_date, start_month,start_year = 0,0,0

end_date, end_month,end_year = 0,0,0

print("Enter start year , start month , start date separated by space")
li = list(map(int,input().split()))

start_year, start_month, start_date = li[0] , li[1], li[2]

print("Enter end year , end month , end date separated by space")
li = list(map(int,input().split()))

end_year, end_month, end_date = li[0] , li[1], li[2]

initial_date = date(start_year, start_month, start_date)
final_date = date(end_year, end_month, end_date)
date_ans = final_date - initial_date

print("Nos of days are ",date_ans.days)