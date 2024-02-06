def parse_month(month):

        if month == "Januany":
            return "01"
        elif month == "Febuary":
            return "02"
        elif month == "March":
            return "03"
        elif month == "April":
            return "04"
        elif month == "May":
            return "05"
        elif month == "June":
            return "06"
        elif month == "July":
            return "07"
        elif month == "Agust":
            return "08"
        elif month == "September":
            return "09"
        elif month == "October":
            return "10"
        elif month == "November":
            return "11"
        elif month == "December":
            return "12"
        
def day(day):
    if len(day) == 1:
        return f"0{day}"
    else:
        return day
        
def parse_date(user_string):
    list_user_string = user_string.split(" ")
    
    return f"{parse_month(list_user_string[0])}/{day(list_user_string[1][:-1])}/{list_user_string[2]}"

if __name__ == '__main__':
    print(parse_date(input()))
    
    
    