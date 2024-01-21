import sys

def maximum_meetings(n, meetings):
    # 회의를 끝나는 시간을 기준으로 정렬
    meetings.sort(key=lambda x: x[1])

    count = 1  # 첫 번째 회의는 항상 선택
    end_time = meetings[0][1]

    # 다음 회의부터 순회하면서 겹치지 않는 회의 선택
    for i in range(1, n):
        if meetings[i][0] >= end_time:
            count += 1
            end_time = meetings[i][1]

    return count

if __name__ == "__main__":
    # input.txt 파일을 읽어옴
    with open("input.txt", "r") as f:
        sys.stdin = f
        n = int(input())  # 회의의 수

        meetings = []
        for _ in range(n):
            start, end = map(int, input().split())
            meetings.append((start, end))

    # 결과 출력
    result = maximum_meetings(n, meetings)
    print(result)
