def format_date(date_str):
    
    months = {
        "01": "January",
        "02": "February",
        "03": "March",
        "04": "April",
        "05": "May",
        "06": "June",
        "07": "July",
        "08": "August",
        "09": "September",
        "10": "October",
        "11": "November",
        "12": "December"
    }

    try:
        month, day, year = date_str.split("/")

        if month not in months:
            return "Invalid month."

        if not 1 <= int(day) <= 31:
            return "Invalid day."

        if len(year)!= 4:
            return "Invalid year."

        human_readable_date = f"{months[month]} {int(day)}, {year}"

        return human_readable_date
    except ValueError:
        return "Invalid date format. Please use mm/dd/yyyy."

date_input = input("Enter the date (mm/dd/yyyy): ")

formatted_date = format_date(date_input)
print("Date Output:", formatted_date)