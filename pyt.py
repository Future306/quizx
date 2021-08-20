str8="What is your name? "
print(str8)
name=input("Enter your name = ")
n8=name
print("Welcome"), print(n8)
str1=("Hii whats up?")
print(str1)
Sid=input("Enter your answer = ")
n2=Sid
str2="Oh!Nice & Whats going on?"
print(str2)
Ans=input("Enter your answer = ") 
n2=Ans
str3='''Can you tell me what's written wrong in this
1,2,3,4,5,7,8,6,9'''
print(str3)
Answer=int(input("Enter your answer = "))
n1=Answer

if n1==6:
    print("Oh! Ya i didn't notice.Thanku very much")
else:
    print("I don't think so its wrong...I think its correct")
    


Str4='''You really have a sharp mind. So can you plz solve this question for me
Solve the given Sets of word I am not able to solve it
KBGSLM  (Hint: Use Atbash cipher)'''
print(Str4)
Atbash=input("Enter your answer = ")
n4=Atbash

if n4.lower()=='python':
    print("You got that right")
else:
    print("Wrong! Try again")


Str5='''Come on lets leave all this and lets play a quiz It just contain 5 Questions
Quiz Starts from here'''

ans=input('Are you ready to play (yes/no): ')
score = 0
total_q = 5

if ans.lower() =='yes':
    ans= input('1. Who is the current PM of United States? ')
    if ans.lower() =='joe biden':
        score += 1
        print('Correct')
    else:
        print('Incorrect')


    ans= input('2. Who has just brought gold medal in olympics for india?') 
    if ans.lower() =='neeraj chopra':
        score += 1
        print('Correct')
    else:
        print('Incorrect')


    ans= input('3. What is it written in code atbash cipher KILTIZNNRMT?')
    if ans.lower() =='programming':
        score += 1
        print('Correct')
    else:
        print('Incorrect')


    ans= input('4.From Where do the gold medalist of india belong?')
    if ans.lower() =='harayana':
        score += 1
        print('Correct')
    else:
        print('Incorrect')


    ans= input('5. What is 2+8+9-1?')
    if ans =='18':
        score += 1
        print('Correct')
    else:
        print('Incorrect')


print('Thanku for playing , you got',score,"questions correct.")
mark=(score/total_q)*100

print("Mark:", str(mark)+'%')
print('Goodbye')




    




