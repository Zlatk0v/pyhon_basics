# input
username = input()
password = input()

attempt = input()

# logic
while attempt != password:
    # print('wrong password')
    attempt = input()

print(f'Welcome {username}!')
