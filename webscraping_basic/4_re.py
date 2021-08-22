# Regular expression 정규식
import re


# . : 하나의 문자를 의미 s.x -> sax, sbx, scx ... 두글자는 안됨
# ^ : 문자열의 시작 ^kor  -> kor로 시작하는 애들은 다 매칭 ex korea, korple, kor_save 등
# $ : 문자열의 끝 se$ : case, base 등 se로 끝나는 애들 매칭

p = re.compile("ca.e") # ca.e에 해당하는애들을 컴파일함

def print_match(m):
    if m:
        print("m.group(): ", m.group()) # 일치하는 문자열을 반환해줌
        print("m.string: ", m.string) # 입력받은 문자열을 반환해줌. 함수가 아니라 변수기 때문에 괄호없이 사용.
        print("m.start(): ", m.start()) # 입력받은 문자열의 시작 index
        print("m.end(): ", m.end()) # 일치하는 문자열의 끝 index
        print("m.span(): ", m.span()) # 일치하는 문자열싀 시작과 끝 index
    else:
        print("매칭되지 않음")

# m = p.match("caffe") # 매칭되지 않음
# print_match(m)

# m = p.match("careless") # 매칭됨 -> 주어진 문자열의 처음부터 읽어들이면서 일치하는지 확인하기 때문
# print_match(m)

# m = p.search("good care") # 매칭됨 -> 주어진 문자열 중에 일치하는게 있는지 확인
# print_match(m)

# m = p.search("nothing") # 매칭안됨
# print_match(m)

# lst = p.findall("good care cafe") # findall : 일치하는 모든것을 리스트 형태로 반환
# print(lst)



## p = re.compile("원하는 정규식") 원하는 정규식 형태를 p에 저장 -> p에서 각종 함수들로 원하는 결과값 반환가능

## m = p.match("비교할 문자열") : 주어진 문자열의 처음부터 일치하는지 확인하여 결과를 m에 저장
# 반환된 값은 group, string 등 여러개 함수 및 변수를 가지고 있는 객체. 일치하지 않으면 false값 가짐.
# 일치해서 반환된 객채가 가진 함수 및 변수호출해서 원하는 값 얻을 수 있음.
## m = p.search("비교할 문자열") : 주어진 문자열 중 일치하는게 있는지 확인
## lst = p.match("비교할 문자열") : 일치하는 모든 것을 리스트 형태로 반환

## m = p.match("비교할 문자열") : 주어진 문자열의 처음부터 일치하는지확인