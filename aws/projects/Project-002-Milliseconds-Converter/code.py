def convertMillis(millis):
    seconds=(millis/1000)//60
    minutes=(millis/(1000*60))//60
    hours=(millis/(1000*60*60))//24
    return seconds, minutes, hours
def main():
    millis=int(input("Enter time in milliseconds "))
    if intmillis < 1000 :
        print("just {0} millisecond/s".format(millisecond)
    elif millis > 1000 :
        con_sec, con_min, con_hour = convertMillis(millis)
        if con_hour == 0 :
            print("{0} minute/s {2} second/s ".format(con_min, con_sec))
        elif con_min == 0 :
            print("{0} hour/s  {1} second/s ".format(con_hour,  con_sec))
        elif con_sec == 0 :
            print("{0} hour/s {1} minute/s ".format(con_hour, con_min))
        
        print("{0} hour/s {1} minute/s {2} second/s ".format(con_hour, con_min, con_sec))

main()