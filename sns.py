import hashlib


class Member:
    def __init__(self, name, username, password):
        self.name = name
        self.username = username
        m = hashlib.sha256()
        m.update('password.encode'.encode('utf-8'))
        self.password = m.hexdigest()
    def display(self):
        print(f"{self.name}님의 id는{self.username}입니다.")
class Post:
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author
    def display(self):
        print(f"{self.title}\n{self.content}\n{self.author}")

M1 = Member('홍길동', 'hong', '1670')
M2 = Member('김미미', 'meme', '7580')
M3 = Member('박철수', 'soosoo', '7580')

# print(M1.password)

member_list = []
member_list.append(M1)
member_list.append(M2)
member_list.append(M3)

for member in member_list:
    print(member.name)

P1 = Post('홍길동의 게시글 입니다.','홍길동입니다.',M1.username)
P2 = Post('김미미의 게시글 입니다.','김미미입니다.',M2.username)
P3 = Post('박철수의 게시글 입니다.','박철수입니다.',M3.username)

post_list = []
post_list.append(P1)
post_list.append(P2)
post_list.append(P3)

while True:
    com = input("id검색: i, 키워드검색: k, id등록:n, 게시글등록:c :")
    if com == "i":
        search_user= input("id를 입력해주세요:")
        found = False
        for post in post_list:
            if post.author ==search_user:
                print(f"{search_user}:\n{post.title}")
                found = True
        if found == False:
                print("id검색 결과가 없습니다.")
    elif com=="k":
        search_keyword=input("키워드를 입력하세요:")
        found = False
        for post in post_list:
            if search_keyword in post.content:
             print(post.title)
             found = True 
        if found == False:
            print("키워드검색결과가 없습니다.")  
    elif com=="n":
        new_name=input("이름을 입력하세요 :")
        new_username=input("id를 입력하세요 :")
        new_password=input("비밀번호를 입력하세요 :")
        member_list.append(Member(new_name, new_username, new_password))
        print("축하합니다.가입이 완료되었습니다.")
    elif com=="c":
        new_title=input("제목을 입력하세요 :")
        new_content=input("내용을 입력하세요 :")
        new_author=input("작성자를 입력하세요 :")
        found = False
        for m in member_list:
            # found = False
            if(new_author==m.username):
                print("게시물 등록이 완료되었습니다. ")
                # found = False
                post_list.append(Post(new_title, new_content, new_author))
                found =True
        if found == False:
            print("존재하지 않는 작성자입니다.")
    else:
        print("잘못된 입력입니다.")


