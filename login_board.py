 

from ast import Break

from pickle import TRUE




article1 = {"번호" : 1, "제목" : "소니의 슈팅교실", "내용" : "epl 득점왕", "작성자" : "sony7"}
article2 = {"번호" : 2, "제목" : "데용의 수비교실", "내용" : "바르샤 종신", "작성자" : "dejong21"}
article3 = {"번호" : 3, "제목" : "덕배의 패스교실", "내용" : "패스마스터", "작성자" : "kdb17"}

article_list = [article1, article2, article3] # 게시물 저장소

user1 = {"아이디":"kdb17", "비밀번호" : "1717", "이름" : "케빈 데브라이너"}
user2 = {"아이디":"sony7", "비밀번호" : "7777", "이름" : "손흥민"}
user3 = {"아이디":"dejong21", "비밀번호" : "2121", "이름" : "프랭키 데용"}
user4 = {"아이디":"0", "비밀번호" : "0", "이름" : "마스터키"}

user_list = [user1, user2, user3, user4] # 회원 저장소

for user in user_list:
  print(user)

list = [ "add : 게시물 추가",
    "read : 게시물 목록 조회",
    "update : 게시물 수정",
    "delete : 게시물 삭제",
    "detail : 상세 보기",
    "repl : 댓글달기",
    "exit : 종료"
    ]
data=article_list
lastnum = 3

def help():#도움말 함수
    for i in range(7):
        print(list[i])   

def add(loginid): #게시물 추가 함수 + 번호 lsatnum이 마지막 번호를 가르키게
    global lastnum
    subtitle =input("제목을 입력해주세요 : ")
    write = input("내용을 입력해주세요 : ")
    for user in user_list:
        if user["아이디"]==loginid:
            name = user["이름"]
    article = {
        "번호" : lastnum +1,
        "제목" : subtitle,
        "내용" : write,
        "작성자" : name
    }
    article_list.append(article)
    lastnum+=1
    read() 

def read(): #게시된 게시물들 확인 함수
    print("==========게시물 목록==========")
    for article in article_list: 
        print("번호: {}, 제목 : {}, 작성자 : {}".format(article["번호"],article["제목"],article["작성자"]))
    print("==============================")

def update(loginid): #게시물 수정 함수 + 자기 게시물이 아니면 수정 안되게
    i = int(input("수정할 게시물 번호를 입력주세요: "))
    for user in user_list:
        if user["아이디"]==loginid:
            name = user["아이디"]
    for article in article_list:
        if article["번호"] == i: 
            newtitle = str(input("제목 : "))
            newbody = str(input("내용 : "))
            article ={
                "제목" : newtitle,
                "내용" : newbody,
                "작성자" : name
            }
            article_list[i-1].update(article)
            read()     
            print("수정이 완료되었습니다.")
            return
    print("없는 게시물입니다.")
    return

def exit():#종료 함수
    print("byebye")

def delete():#게시물 삭제 함수
    i = int(input("삭제할 게시물 번호를 입력해주세요 :"))
    for article in article_list:
        if article["번호"] == i :
            article_list.remove(article)
            print("삭제가 완료되었습니다.")        
            read() 
            return       
    print("없는 게시물 입니다.")     
    return 


def detail():#상세정보 열람 함수
    i = int(input("상세보기 할 게시물 번호 입력 : "))
    for article in article_list:
        if article["번호"] == i :
            print("========{}번 게시물 조회========".format(i))
            print(" 번호: {},\n 제목 : {},\n 내용 : {},\n 작성자 : {}".format(article["번호"],article["제목"],article["내용"],article["작성자"]))
            print("---------- 댓글 ----------")
            for reply in repl_list:
                print(reply)
            print("===========================")
repl_list = []
reply_num = 0

def reply(loginid):#게시물 댓글 달기 함수
    global reply_num
    repl = input("댓글 내용을 입력해주세요 : ")
    re = {
        "댓글 번호" : reply_num+1,
        "댓글 내용" : repl,
        "댓글 작성자" : loginid
    }
    repl_list.append(re)
    print("댓글이 등록되었습니다.")
    reply_num +=1
    return
'''
                                                                ^^^게시물 함수  vvv아이디 함수
'''
def login_current(loginid,loginpw):
    for user in user_list:
        if loginid == user["아이디"]:
            if loginpw == user["비밀번호"] :
                print("{}님 안녕하세요! 게시판 기능을 시작합니다.".format(user["이름"]))
                return True
            else:
                print("비밀번호가 틀렸습니다.")
                return False
    print("잘못된 아이디 입니다.")
    return False        

def input_idpw():
    loginid = input("아이디를 입력하세요 : ")            
    loginpw = input("비밀번호를 입력하세요 : ")

def board_pro(loginid):
    while True:
        cmd =input("명령어를 입력해주세요: ")
        if cmd=="help":
            help()
        elif cmd=="add":
            add(loginid)   
        elif cmd=="read":
            read() 
        elif cmd=="update":
            update(loginid)
        elif cmd=="delete":
            delete()   
        elif cmd=="detail":
            detail() 
            yn= input("댓글을 작성하시겠습니까? y/n : " )
            if yn == "y":
                reply(loginid)
            else:
                print("타이틀로 돌아갑니다.")
                continue    
        elif cmd=="exit":
            exit()
            break   
        # elif cmd=="reply":   
        else: 
            print("올바른 명령어를 입력해주세요 ")

while True:
    cmd = input("로그인을 하시려면 : login , 종료하시려면 : exit를 선택해주세요\n")
    if cmd == "login" or "0":
        loginid = input("아이디를 입력하세요 : ")            
        loginpw = input("비밀번호를 입력하세요 : ")
        check =login_current(loginid,loginpw)
        if check ==True:
            board_pro(loginid)
    elif cmd == "exit":
        print("프로그램을 종료하겠습니다.")    
        break
    else:
        print("login 혹은 exit 만 입력해주세요")
        continue








