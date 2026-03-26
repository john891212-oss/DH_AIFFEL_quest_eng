import math  # math 모듈 임포트 - ** 연산할 때 math.pow() 쓰려고 가져옴
# 나중에 다른 수학 함수도 쓸 수 있으니까 일단 넣어둠


def run(): # 계산기 실행 함수, 이 함수를 호출하면 계산기가 시작됨 import sansu 하고 sansu.run() 이렇게 쓰면 됨
   
    print("==== 계산기 시작 ====")

    while True: # while True 로 뺑뺑이 돌리고 나중에 break로 ㅌㅌ        
        # for문은 범위가 정해져 있어서 여기선 while이 더 맞는 것 같음
        # 첫번째 숫자 입력받기
        # input()은 항상 문자열로 받아오기 때문에 int()로 변환해줘야 함
        # 안그러면 1 + 2 = 12 이런식으로 문자열 연결이 되어버림
        a = input("정수를 입력하세요. : ")
        try:
            a = int(a)
            # int()로 변환 시도
            # "123" 같은 문자열은 변환이 됨
            # "abc" 나 "12.5" 같은건 ValueError 발생함
            # 12.5는 float이라서 int()로 바로 못 바꿈 주의
        except ValueError:
            print("정수를 입력하라고요, 정수를")
            # 오류 메시지 출력하고 continue로 while 처음으로 돌아감
            continue

        # 연산자 입력받기
        # 지원하는 연산자는 +, -, *, /, ** 다섯가지임
        # .strip() 붙이면 공백 제거해줌 - 혹시 스페이스 입력해도 괜찮게
        op = input("오른쪽의 연산자 중 하나만 고르시오. (+, -, *, /, **): ")

        # 두번째 숫자 입력받기
        # 첫번째 숫자 받을 때랑 똑같이 처리함
        # 나중에 함수로 만들면 더 깔끔할 것 같긴 한데 일단 이렇게
        b = input("다음 정수를 입력하세요 : ")
        try:
            b = int(b)
        except ValueError:
            print("정수만 입력 받습니다.")
            continue

        # 연산자 종류에 따라 다르게 계산하기
        # if elif elif ... 로 하나씩 비교함
        if op == '+':
            # 더하기
            result = a + b
            print(f"결과: {a} + {b} = {result}")

        elif op == '-':
            # 빼기
            result = a - b
            print(f"결과: {a} - {b} = {result}")

        elif op == '*':
            # 곱하기
            # 파이썬에서 곱하기 기호는 x 아니고 * 임
            result = a * b
            print(f"결과: {a} * {b} = {result}")

        elif op == '/':
            # 나누기 트롤러 방지용
            # b가 0이면 ZeroDivisionError 발생하니까 미리 체크해줌
            # try except 써도 되는데 if로 먼저 걸러주는게 더 직관적인 것 같음
            if b == 0:
                print("나눌 때'0'좀 넣지마라.")
            else:
                result = a / b
                print(f"결과: {a} / {b} = {result}")

        elif op == '**':
            # 제곱 연산
            # math.pow() 쓰면 결과가 float으로 나옴 예를들어 3**2 = 9.0
            # 9.0 보다 9 가 더 보기 좋아서 int()로 한번 더 변환해줌
            # 근데 소수점 결과가 나오는 경우엔 잘릴 수도 있음 - 일단 정수만 쓰니까 괜찮을듯
            result = math.pow(a, b)
            result = int(result)
            print(f"결과: {a} ** {b} = {result}")

        else:
            # 위에서 정의한 연산자 다섯개 말고 다른거 입력하면 여기로 옴
            # 예를들어 % 나 // 같은거 입력했을 때
            print(f"오류: '{op}'가 보기 안에 있던 연산자 입니까?")

        # 계속 계산할지 물어보기
        # yes 입력하면 while 루프 처음으로 돌아가고
        # yes 가 아니면 break 로 루프 탈출 -> 계산기 종료
        again = input("계속 계산할까요? (yes / no): ")
        if again != 'yes':
            print("끝")
            break
