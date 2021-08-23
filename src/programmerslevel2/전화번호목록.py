# 인터넷참고, 문자열 숫자 sort 는 길이가 아닌 앞자리부터의 숫자크기
def solution(phone_book):
    answer = True
    phone_book.sort()
    for i in range(1, len(phone_book)):
        previous = phone_book[i-1]
        if phone_book[i][:len(previous)] == previous:
            return False
    return answer

print(solution(["12","567","123","1235","88"]))