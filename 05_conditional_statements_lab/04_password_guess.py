#с фразата "s3cr3t!P@ssw0rd".
#При съвпадение да се изведе "Welcome".
#При несъвпадение да се изведе "Wrong password!".

attemp = input()

if attemp == "s3cr3t!P@ssw0rd":
    print("Welcome")
else:
    print("Wrong password!")