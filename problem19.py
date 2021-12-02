'''
Problem19


You are given the following information, but you may prefer to do some research for yourself.

    1 Jan 1900 was a Monday.
    Thirty days has September,
    April, June and November.
    All the rest have thirty-one,
    Saving February alone,
    Which has twenty-eight, rain or shine.
    And on leap years, twenty-nine.
    A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.

How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

'''

jan = 31
feb = 28
mar = 31
apr = 30
may = 31
jun = 30
jul = 31
aug = 31
sep = 30
okt = 31
nov = 30
dec = 31

months = [
  jan, 
  feb, 
  mar, 
  apr, 
  may, 
  jun, 
  jul, 
  aug, 
  sep, 
  okt, 
  nov, 
  dec
]

def jorge():
  listy = []
  listbi = []
  for i in range(1901, 2001):
    if i % 4 == 0:
      listbi.append(i)
    else:
      listy.append(i)
  return listy, listbi



print(jorge())
# print(months)



# totalbi = len(listbi)
# total = len(listy)

# sundays = (366*totalbi + 365*total)//7

# print(listbi)
# print(listy)
# print(sundays)