#От конзолата се четат 3 реда:
#1.	Брой страници в текущата книга – цяло число в интервала [1…1000]
#2.	Страници, които прочита за 1 час – цяло число в интервала [1…1000]
#3.	Броят на дните, за които трябва да прочете книгата – цяло число в интервала [1…1000]

#read user input
pages_book = int(input())
pages_per_hour = int(input())
count_days_for_read = int(input())

#logic
total_time = pages_book // pages_per_hour
needed_time = total_time // count_days_for_read

#print output
print(needed_time)