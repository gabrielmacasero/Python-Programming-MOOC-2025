"""
Please write a function named list_years(dates: list) which takes a list of date type objects as its argument.
The function should return a new list, which contains the years in the original list in chronological order, from earliest to latest.

An example of the function in action:

years = list_years([date1, date2, date3])
print(years)
Sample output
[1993, 2006, 2019]

"""

def list_years(dates: list):
    years = []
    for date in dates:
        years.append(date)
    years.sort()
    return years

if __name__ == "__main__":
    years = list_years([1892, 1900, 1965, 2002, 2010, 2018, 1999, 1937, 2015])
    print(years)
