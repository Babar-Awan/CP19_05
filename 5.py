#Question 5
#chatbot

variable="quit"
condition="abc"
while((condition)!=variable):
    question=input("Ask any Question : ")
    if(question.find("your name")!=-1):
        print("My name is Arsalan Ahmed")
    elif(question.find("country name")!=-1):
        print("My country name is Pakistan")
    elif(question.find("city name")!=-1):
        print("My city name is Karachi")
    elif(question.find("university name")!=-1):
        print("My university name is Muhammad Ali Jinnah University")
    elif(question.find("who are you")!=-1):
        print("I'am Arsalan Ahmed, The Student of BSSE program at Muhammad Ali Jinnah University")
    elif(question.find("your age")!=-1):
        print("I'am 18 years old")
    elif(question.find("email")!=-1):
        print("sp19bsse0018@maju.edu.pk")
    elif(question.find("favourite game")!=-1):
        print("My favourite game is cricket")
    elif(question.find("number")!=-1):
        print("My personal mobile number is 03320270677")
    elif(question.find("id")!=-1):
        print("SP19-BSSE-0018")
    else:
        print("Sorry! Please ask another Question")
        
    condition=input("type quit to exit : ")


    