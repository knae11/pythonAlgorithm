'''
기존에 풀었던 방식
def solution(files):
    answer = []
    number='0123456789'
    for file in files:
        numberStart = 0;
        numberEnd = 0;
        for i in range(len(file)):
            if file[i] in number and file[i-1] not in number:
                numberStart = i
            if file[i] in number and (len(file) == i+1 or file[i+1] not in number):
                numberEnd = i
                break
        answer.append((file[:numberStart], file[numberStart:numberEnd+1], file[numberEnd+1:]))
    answer =[ line[0]+line[1]+line[2] for line in sorted(answer, key=lambda x :( x[0].lower(),  int(x[1])) )]
    return answer
'''

def solution(files):
    answer = []
    process = []
    numbers = '0123456789'
    for file in files:
        numberstart_index = 100
        numberend_index = 0
        for i in range(len(file)):
            if file[i] in numbers:
                numberstart_index = i
                for j in range(i, len(file)):
                    if file[j] not in numbers:
                        break
                    numberend_index = j
                break
        process.append(
            (file[:numberstart_index], file[numberstart_index: numberend_index + 1], file[numberend_index + 1:]))
    process.sort(key=lambda x: (x[0].lower(), int(x[1])))
    for item in process:
        answer.append(item[0] + item[1] + item[2])
    return answer


print(solution(["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]))
