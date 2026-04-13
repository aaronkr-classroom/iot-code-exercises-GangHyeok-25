# 5_SayDays.py

class SayDays:
    def_init_(self, year, month, day):
        # 속성 초기화
        self.year = year
        self.month = month
        self.dat = day
    
    def is_leap(self):
        #윤년 여부 확인
        y = self.year
        return ((y % 4 == 0 and y % 100 != 0) or (y % 400 == 0)):
        
    def days(self): # 년의 몇번째 날인가
        # 1월 1일부터 지난 날짜
        days_in_month = [
            31, 29 if self.is_leap() else 28, 31, 30, #2월은 28일일수도, 29일일수도 있다
            31, 30, 31, 31,
            30, 31, 30, 31
            ]
        total = 0
        m = 0
        while m < self.month:
            total += days_in_month[m]
            m += 1
            
        total += self.day
        return total
    def days_left(self): # 년에 남은 일수 (12월 31일 기준)
        total_days = 366 if self.is_leap() else 365
        return total_days - self.days()
    
    def weekday(self): # 숫자로 요일 체크
        y = self.year
        m = self.month
        d = self.day
        
        if m < 3:
            m +=12
            y -= 1
        
        K = y % 100
        J = y // 100 # 정수 필수
        
        h = d + (13 * (m + 1) // 5 + K + K // 4 + J // 4 + 5 * 1) % 7
             return h
             

        
    def weekday_name(self): # 토요일 매핑
        name = [
            "토요일", "일요일", "월요일", "화요일", "수요일", "목요일", "금요일"
            ]
        return names[self.weekday()]
    
 # 클래스 사용하는 프로그램
    while True:
        # 날짜 입력
        year = int(input("년 입력: "))
        month = int(input("월 입력: "))
        day = int(input("일 입력: "))
        
        date = SayDays(year, month, day)
        
        #결과 출력
        print("몇번째 날: ", date.days())
        print("남은 일수: ", date.days_left())
        print("요일 숫자: ", date.weekday())
        print("요일 이름: ", date.weekday_name())
    