def leap_year(year):
    return True if (year%4 == 0 and year%100 != 0) or year%400 == 0 else False

# print(leap_year(2000))
#c
def Day(year, month):
    ping_year = [31,28,31,30,31,30,31,31,30,31,30,31]
    if leap_year(year):
        ping_year[1] = 29
    return ping_year[month-1]

# print(Day(2019,11))
#d
def how_day(year,month):
    day = 0
    for i in range(1900,year):
        day += 366 if leap_year(i) else 365
    for j in range(1, month):
        day += Day(year, j)
    return day

print(how_day(1900,2))
#e
def month_day(year, month):
    days = 0
    ping_year = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    for i in range(1,month):
        if leap_year(year):
            ping_year[1] = 29
            days = days + ping_year[i-1]
        else:
            days = days +ping_year[i-1]
    return days
# print(month_day(2020,5))
#f
def zong_day(year, month):
    sum2 = how_day(year, month)
    return sum2
# print(zong_day(2020,11))

#G
def week(year, month):
    WEEK = ["星期日","星期一","星期二","星期三","星期四","星期五","星期六"]
    return WEEK[(how_day(year,month)+1)%7]

# print(week(2020,10))
#G-1
def cut_it(hour):
    hour_cut = 0 #切完回傳回去的
    if hour<=2:
       hour_cut=hour*(4/3)
    elif hour<=9:
       hour = hour - 2
       hour_cut = (8/3)+hour*(5/3)
    else:
       hour = hour - 9
       hour_cut = (8/3)+(10)+hour*(8/3)
    return hour_cut

#H
def show():
    year = int(input("輸入年份："))
    month = int(input("輸入月份："))
    print("星期日\t星期一\t星期二\t星期三\t星期四\t星期五\t星期六")
    msum_day=how_day(year,month)
    mweek=(msum_day + 1) % 7
 #-----------------------------
    normal_d=0 #常日班天數
    duty_h=0 #值班時數
    snack_money = 0
    snack_money_d = 0
    work_c=(msum_day + 1) % 12
    print(work_c,"#")
    if work_c >=5:
      work_c=work_c-5
    else:
      work_c=work_c+7
    print(work_c)
    #弄出值班規律
#------------------------------------
    mmonth_day=Day(year, month)
    for j in range(mweek):
        print('\t',end="")
    for i in range(1,mmonth_day+1):
 #------------------------------------------
        work_c123=(work_c+i)%12
        if work_c123==4 or work_c123== 11 or work_c123==0:
           work_c123=0
           hour=0
           snack_money_d = 0
        elif work_c123 == 1:
           work_c123 = 3
           hour = 8.5
           snack_money_d = 250
        elif work_c123 == 7:
           work_c123 = 2
           hour = 6.5
           snack_money_d = 0
        elif work_c123<=3:
           work_c123=3
           hour=7
           snack_money_d = 250
        elif work_c123<=7:
           work_c123=2
           hour = 8
           snack_money_d = 0
        else:
           work_c123=1
           hour = 9
           snack_money_d = 400
        duty_h = duty_h + hour
        snack_money = snack_money + snack_money_d
 #弄出123值 跟 時數
#-------------------------------------------------------
#------------------------------------------------------
        if (mweek + i) %7 == 0 or (mweek+i)%7==1:
            normal_d=normal_d
        else:
            normal_d=normal_d+1
 #常日班天數
 #-------------------------------------------
        if (mweek + i) %7 == 0:
            print(str(i),work_c123,"\t",end="")
            print()
        else:
            print(str(i),work_c123,"\t",end="")

    normal_h=normal_d*8#乘8小時
    cut_12_h = duty_h-normal_h


    if cut_12_h<=0:      #要切的
       cut_12=0          #切完的
    else:
       if cut_12_h//12<=0:
         cut_12 = cut_it(cut_12_h)
       else:
         cut_12 = (cut_12_h//12)*(70/3)+cut_it(cut_12_h%12)

    print()
    print()
    print("保養上班時數",normal_h)
    print("值班上班時數",duty_h)
    print("12切時數",cut_12)
    print("點心費",snack_money)

show()
