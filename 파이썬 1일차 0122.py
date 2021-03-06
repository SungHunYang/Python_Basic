## 출력 ##
print('반갑습니다') #자동 줄바꿈
print('안녕하세요',end='하이\n') #줄바꿈을 안하도록한다. ex) 안녕하세요하이1234
# \ 빽슬래시 n \n하면 그 다음 프린트는 줄바꿈을 한다 ex) 안녕하세요하이
#                                                                                 1234
print(1234)
# 프로그램에세 제외되는 코드를 주석
'''
여러줄 주석
입니다
'''
# 여러줄 주석을 사용하는 다른 방법은
# 원하는 라인 여러개를 드래그 하고
# ALT + 3 --> 드래그를 주석으로 만드는법
# ALT + 4 --> 드래그 했던 여러줄 주석을 푸는법
##print(20) 
##print(10) 

# data type(자료형) -> type() 자료형을 볼수 있는 함
# 정수 int  %d
# 실수 float  %f <-- 형식 지정자
# 문자열 str  %s
a=10
'''
 a라는 공간에 변수10 값(VALUE) 저장
 = 대입 연산자
 '''
type(a)
a=3.14
type(a)
a='apple'
type(a)
'''
포인터 형태로 주소로 저장해서 변수타입을 적어주지 않아도 된다
'''

# 변수명, 식별자 이름 규칙
#1) 띄어쓰기
#2) 특수문자xx
#3) 가급적 소문자 시작 권장
#4) 숫자로 시작 xx
#5) 가급적 상단부에 선언,정의를 권장

a,b=10,20
print(a)
print(b)
# 콤마(,)로 print에서 값을 보여주는법 자바에서 +와 유사하다고 보자
# 콤마(,)를 쓰면 그 부위를 자동 띄어쓰기 한다
print('a=',a,'이고, b=',b,'이다')
# 자바에서 하듯이 + 를 쓸수있다 , +는 자동 띄어쓰기를 하지 않는다.
# 대신! 단! 더하기로 보여주려고 하면 타입이 같아야 된다. 따라서 앞에 str이니까 a도 str이여야 +가능
# 'a='가 str이니까 a='apple'이런식이여야 된다 아니면 10+a+ 면 a가 int 여도 가능
'''
print('a='+a+'이고, b='+b+'이다') 따라서 얘는 안되고
'''
a=10 # 타입은 int
str(a) #하면 str '10'
b='10' # 타입 str
int(b) # 하면 int 10
### 형 변환 (캐스팅)

print('a='+str(a)+'이고, b='+str(b)+'이다') # 이렇게 해야 가능

print('%d %f %s' %(10,3.14,'apple'))
print('{}'.format('apple')) # 중괄호 안에 들어갈걸 넣을게요 .뒤에서 format 안에있는걸
print('{} {}'.format('banana',1234))
'''
순서 지정 가능
첫번째는 0
바나나 0번 1234 1번
'''
print('{1} {0}'.format('banana',1234))

## 입력 ##
'''
정수입력을 보여주고 input으로 값을 받는다
input()은  str 타입으로 입력받음
'''
num=input('정수입력:  ')
print(num)
## 그래서 캐스팅을 해야한다
num=int(input('정수입력: '))
print(num)

# 예제) 1. 문자열 입력: apple --> 그 아래 입력하신 단어는 ____ 라고 알려줬으면
# 예제)2. 정수 1 입력 정수 2입력 두 정수의 합은 ___ 입니다

c=input('문자열 입력: ')
print('입력하신 단어는',c,'입니다')
print('입력하신 단어는 '+c+' 입니다')
d=int(input('정수 1입력: '))
e=int(input('정수 2입력: '))
print('두 정수의 합은 '+str(d+e)+' 입니다')
print('두 정수의 합은',(d+e),'입니다')
      

