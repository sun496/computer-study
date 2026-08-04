# 변수,자료형,print,계산하기




print("Hello, World!")
print('안녕하세요')
print('컴퓨터공학과')
# print(2026)

### 변수 선언
name ='은선' 
age = 20
major = '컴퓨터공학과'

print('이름:', name)
print('나이:', age)
print('전공:', major)

### 자료형 확인
print(type(name))
print(type(age))
print(type(major))

###계산하기
a = 50
b = 30

print('a + b =', a + b)
print('a - b =', a - b)
print('a * b =', a * b)
print('a / b =', a / b)
print('a // b =', a // b)
print('a % b =', a % b)


#문제 자기소개 출력
name = '은선'
major = '컴퓨터공학과'
print('제 이름은', name, '입니다.')
print('제 전공은', major, '입니다.')


#문제 나이 계산 
n=int(input('몇년뒤에 나이를 계산할까요? '))
age = 20
print('n년뒤의 나이:', age + n)


#사칙연산 계산기
a = int(input('첫 번째 숫자를 입력하세요: '))
b = int(input('두 번째 숫자를 입력하세요: '))
print('a + b =', a + b)
print('a - b =', a - b)
print('a * b =', a * b)
print('a / b =', a / b)
print('a // b =', a // b)   
print('a % b =', a % b)


## 문제 1. 사용자 정보 데이터 처리
name = "Kim"
student_id = 20260101
major = "Computer Engineering"
python_score = 85
c_score = 92
average=(python_score + c_score) / 2

print('학생명=',name)
print('학번=',student_id)
print('전공=',major)
print('Python 점수=',python_score)
print('C 점수=',c_score)
print('평균=',average)


##문제 2. 단위 변환 프로그램
byte = 1048576
kilobyte = byte //1024
megabyte = kilobyte // 1024 

print('Byte:', byte,'B')
print('Kilobyte:', kilobyte,'KB')        
print('Megabyte:', megabyte,'MB')

##문제 3. 문자열 데이터 분석
sentence = "Computer Engineering"
print("전체 글자 수:", len(sentence))
print("첫 번째 글자:", sentence[0])
print("마지막 글자:", sentence[-1])
#인덱스 사용
print('Engineer의 시작 위치:', sentence.find('Engineer'))
print('Engineer의 시작 위치:', sentence.index('Engineer'))
#### find() 함수는 문자열에서 특정 문자열이 처음으로 나타나는 위치를 반환합니다. 만약 찾는 문자열이 없으면 -1을 반환합니다.
#인덱스	내가 위치를 알고 있을 때 글자를 가져옴
#find()	글자를 찾아서 위치를 알려줌

