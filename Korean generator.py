from random import randint

def print_menu():
    print("Menu:")
    print("1. Sino-Korean Numbers")
    print("2. Pure Korean Numbers")
    print("3. Weekdays")
    print("4. Months")
    print("5. Quit")


korean_numbers = {
    1: {
        0: "",
        1: "하나",
        2: "둘",
        3: "셋",
        4: "넷",
        5: "다섯",
        6: "여섯",
        7: "일곱",
        8: "여덟",
        9: "아홉",
        },
    2: {
        0: "",
        1: "한",
        2: "두",
        3: "세",
        4: "네",
        5: "다섯",
        6: "여섯",
        7: "일곱",
        8: "여덟",
        9: "아홉",
    },
    10: {
        0: "",
        1: "열",
        2: "스물",
        3: "서른",
        4: "마흔",
        5: "쉰",
        6: "예순",
        7: "일흔",
        8: "여든",
        9: "아흔"
    }
}

chinese_numbers = {
    1: {
        0: "",
        1: "일",
        2: "이",
        3: "삼",
        4: "사",
        5: "오",
        6: "육",
        7: "칠",
        8: "팔",
        9: "구"
    },
    2: {
        0: "",
        1: "십",
        2: "백",
        3: "천",
        4: "만",
        5: "십",
        6: "백",
        7: "천",
        8: "억",
        9: "십",
        10: "백",
        11: "천",
        12: "조",
        13: "십",
        14: "백",
        15: "천",
        16: "경",
        17: "십",
        18: "백",
        19: "천"
    }
}

week_days = {
    "Monday": "월요일",
    "Tuesday": "화요일",
    "Wednesday": "수요일",
    "Thursday": "목요일",
    "Friday": "금요일",
    "Saturday": "토요일",
    "Sunday": "일요일"
}

month = {
        "January": "일월",
        "February": "이월",
        "March": "삼월",
        "April": "사월",
        "May": "오월",
        "June": "육월",
        "July": "칠월",
        "August": "팔월",
        "September": "구월",
        "October": "십월",
        "November": "십일월",
        "December": "십이월"
}

quit = ["QUIT", "quit", "Quit", "q", "Q"] # inputs accepted to return to menu

stop_practice = False
def pure():
    print("Type 'QUIT' to return to menu.")
    myMin = int(input("Enter min number (min: 1): "))
    myMax = int(input("Enter max number (max 99) : "))
    answer = 0
    while answer not in quit:
        randomNo = randint(myMin,myMax)
        tensDigit = randomNo // 10
        onesDigit = randomNo % 10
        print(randomNo)
        answer = input()
        if answer not in quit:
            print(korean_numbers[10][tensDigit] + korean_numbers[1][onesDigit])
            print("-----")
"""
def sino():
    print("Type 'QUIT' to return to menu.")
    myMin = int(input("Enter min number (min: 1): "))
    myMax = int(input("Enter max number (max 9999999999999999999) : "))
    answer = 0
    while answer not in quit:
        out = ""
        randomNo = randint(myMin, myMax) # getting a random number
        print(randomNo)
        answer = input()
        if answer not in quit:
            for i in range(19, -1, -1):
                one = 1
                digit = randomNo // 10**i
                digitPlace = digit * 10**i
                randomNo -= digitPlace # removing first digit
                if digit == 1:
                     one = 0 # 일 is not used for numbers in from of 10, 100 etc.
                if bool(digit): # only add to output if digit is not zero
                    out += chinese_numbers[1][digit*one] + chinese_numbers[10][i] #+ chinese_numbers[1][tensDigit]+ chinese_numbers[10][len(str(tensPlace))] + chinese_numbers[1][onesDigit]
            print(out)
            print("-----")"""

def sino():
    print("Type 'QUIT' to return to menu.")
    myMin = int(input("Enter min number (min: 1): "))
    myMax = int(input("Enter max number (max 9999999999999999999) : "))
    answer = 0
    while answer not in quit:
        out = ""
        randomNo = randint(myMin, myMax) # getting a random number
        print(randomNo)
        answer = input()
        if answer not in quit:
            for i in range(len(str(myMin))-1, len(str(myMax))):
                one = 1
                digit = randomNo % 10 # finds the final digit
                randomNo = randomNo // 10 # removes final digit
                if digit == 1:
                     one = 0 # 일 is not used for numbers in from of 10, 100 etc.
                if bool(digit): # only add to output if digit is not zero
                    out = chinese_numbers[1][digit*one] + chinese_numbers[2][i] + out
            print(out)
            print("-----")

def weekDays():
    print("Type 'QUIT' to return to menu.")
    answer = 0
    while answer not in quit:
        randomNo = randint(0, 6)
        test = list(week_days.keys())[randomNo]
        print(test)
        answer = input()
        if answer not in quit:
            print(week_days[test])
            print("---------------")


def months():
    print("Type 'QUIT' to return to menu.")
    answer = 0
    while answer not in quit:
        randomNo = randint(0, 11)
        test = list(month.keys())[randomNo]
        print(test)
        answer = input()
        if answer not in quit:
            print(month[test])
            print("-----")

selected_quit = False

while not selected_quit:
    print_menu()
    selection = int(input("Enter number: "))
    if selection == 1:
        sino()
    elif selection == 2:
        pure()
    elif selection == 3:
        weekDays()
    elif selection == 4:
        months()
    elif selection == 5:
        selected_quit = True
    else:
        print("Please enter number from menu.")

