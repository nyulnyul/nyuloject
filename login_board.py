

from ast import Break

from pickle import TRUE


list = [ "add : 데이터 추가",
    "read : 데이터 조회",
    "update : 데이터 수정",
    "delete : 데이터 삭제"]
data=[]

def help():
    for i in range(4):
        print(list[i])        

def add():
    save =input("저장할 값을 입력해주세요 : ")
    data.append(save)
    read() 

def read():
    if coun() == False:
        return
    print("현재 저장되어 있는 값 : {}".format(data)) 

def update():
    if coun() == False:
        return
    lastd = len(data)-1
    read()
    fix = int(input("수정할 인덱스를 정해주세요: "))
    
    if fix > lastd:
        print("올바른 값 입력하세요")
    else:    
        new = str(input("수정할 내용을 입력해주세요 "))
        data[fix] = new
        read()     
        print("수정완료")

def exit():
    print("byebye")

def delete():
    if coun() == False:
        return

    lastd = len(data)-1
    i = int(input("삭제할 값 을 입력해주세요 :"))
    if i> lastd:
        print("{} 아래로 입력해주세요.".format(lastd))      
    else:
        print("{} 값이 제거되었습니다.".format(data[i]))
        del data[i]      
        read()

def coun():
    if not data:
        print("저장된 데이터가 없습니다.")
        return False
    else: True    
'''
^^^게시물 함수  vvv아이디 함수
'''
article1 = {"번호" : 1, "제목" : "소니의 슈팅교실", "내용" : "소니의 축구 강좌", "작성자" : "sony7"}
article2 = {"번호" : 2, "제목" : "데용의 수비교실", "내용" : "데용의 축구 강좌", "작성자" : "dejong21"}
article3 = {"번호" : 3, "제목" : "덕배의 패스교실", "내용" : "덕배의 축구 강좌", "작성자" : "kdb17"}

article_list = [article1, article2, article3] # 게시물 저장소

user1 = {"아이디":"kdb17", "비밀번호" : "1717", "이름" : "케빈 데브라이너"}
user2 = {"아이디":"sony7", "비밀번호" : "7777", "이름" : "손흥민"}
user3 = {"아이디":"dejong21", "비밀번호" : "2121", "이름" : "프랭키 데용"}

user_list = [user1, user2, user3] # 회원 저장소

for user in user_list:
  print(user)

# 문제 구현 시작 ------------------------------

    
def login_current(loginid,loginpw):
    for user in user_list:
        if loginid == user["아이디"] and loginpw == user["비밀번호"] :
                print("{}님 안녕하세요! 게시판 기능을 시작합니다.".format(user["이름"]))
                return True
        elif loginid != user["아이디"]:
            print("잘못 된 아이디 입니다.")
            return False

        elif loginpw != user["비밀번호"]:
            print("비밀번호를 틀렸습니다.")
            return False

def input_idpw():
    loginid = input("아이디를 입력하세요 : ")            
    loginpw = input("비밀번호를 입력하세요 : ")

def board_pro():
    while True:
        cmd =input("명령어를 입력해주세요: ")
        if cmd=="help":
            help()
        elif cmd=="add":
            add()   
        elif cmd=="read":
            read() 
        elif cmd=="update":
            update()     
        elif cmd=="delete":
            delete()   
        elif cmd=="exit":
            exit()
            break   
        else: 
            print("올바른 명령어를 입력해주세요 ")


while True:
    cmd = input("로그인을 하시려면 : login , 종료하시려면 : exit른 선택해주세요\n")
    if cmd == "login":
        loginid = input("아이디를 입력하세요 : ")            
        loginpw = input("비밀번호를 입력하세요 : ")
        check =login_current(loginid,loginpw)
        if check ==True:
            board_pro()
    elif cmd == "exit":
        print("프로그램을 종료하겠습니다.")
        break









# 문제 구현 끝 --------------------------------