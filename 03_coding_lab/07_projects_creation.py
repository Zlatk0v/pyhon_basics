#constant
TIME_PER_PROJECT = 3

# #reaad user input
name = input()
number_of_projects = int(input())


#logic
result = f'The architect {name} will need {number_of_projects * TIME_PER_PROJECT} hours to complete {number_of_projects} project/s.'

#print output
print(result)

