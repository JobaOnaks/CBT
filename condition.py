import time
users = ['ola','bimpbe']
passwords = ['1234','5678']
prompt = input(""""Enter 1 to Log In
       2 to Sign Up
       3 to quit: """)

def login():
    username = input("\nEnter your Username: ")
    while username:
        if username in users:
            password = input("Enter your Password: ")
            if password == passwords[users.index(username)]:
                print("Login successful\n")
                time.sleep(1)
                question()
                break
            else:
                print("Invalid password")
        else:
            print("Invalid Username")
            username = input("\nEnter your Username: ")

def question():
    position = 0
    score = 0
    questions = ['What best explains Kinetic Energy', 'What is formula for force', 'How many forces does newton have']
    options = ['a. Energy that is in use\nb. Energy about to do work\nc. Energy from Electricity','a. f x d \nb. m x a\nc. V = IR','a. 1\nb. 5\nc. 3\n']
    answers = ["a","b","c"]

    for question in questions:
        print(question)
        print(options[position])
        answer = input("\nanswer: \n")
        if answer == answers[position]:
            score += 20
        else:
            score -= 5
        position +=1  
    print(score) 

def signup():
    new_user = input("\nEnter your Username: ")
    users.append(new_user)
    new_password = input("Enter your Password: ")
    confirm_password = input("Confirm Password: ")
    while new_password != confirm_password:
        print("Invalid Password")
        confirm_password = input("Confirm Password: ")
    else:
        passwords.append(new_password)
        print("Successful")
        time.sleep(2)
        login()


while prompt:
    if prompt == "1":
        login()
        break
    elif prompt == "2":
        signup()
        break
    elif prompt == "3":
        print("Have a wondeful day")
        break
    else:
        print("Invalid Option")
        prompt = input(""""Enter 1 to Log In
       2 to Sign Up
       3 to quit: """)

# joba =passwords[users.index("ola")]
# print(joba)