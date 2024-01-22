package greedyAlgorithm.boj11000;

import java.io.BufferedReader; //외부 파일 불러오는 모듈
import java.io.FileReader;
import java.io.IOException;
import java.util.PriorityQueue; //우선순위 큐 구현
import java.util.StringTokenizer;

public class boj11000 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new FileReader("D:/CodingTest/src/greedyAlgorithm/boj11000/input.txt"));
        StringTokenizer st; //문자열을 토큰으로 분리

        //수업 정보 저장하는 N과 2차원 배열 선언
        int N = Integer.parseInt(br.readLine());
        int[][] list = new int[N][2];

        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            list[i][0] = Integer.parseInt(st.nextToken());
            list[i][1] = Integer.parseInt(st.nextToken());
        }

        // 시작 시간을 기준으로 정렬
        java.util.Arrays.sort(list, (a, b) -> Integer.compare(a[0], b[0]));
        // 수업 끝나는 시간을 저장하는 우선순위 큐 room 선언
        PriorityQueue<Integer> room = new PriorityQueue<>();

        for (int i = 0; i < N; i++) {
            if (room.isEmpty() || room.peek() > list[i][0]) {
                // 현재 수업의 시작 시간이 이전 수업의 끝나는 시간보다 빠르면 새로운 강의실 필요
                //isEmpty(): 비어있으면 참 반환, 아니면 false 반환
                //peek(): 가장 작은 값을 반환하는 메서드(파이썬의 min 메서드와 비슷함)
                room.offer(list[i][1]);
            } else {
                // 현재 수업의 시작 시간이 이전 수업의 끝나는 시간보다 늦으면 강의실 재활용 가능
                room.poll();
                room.offer(list[i][1]);
                //poll():가장 작은 요소(혹은 가장 큰)를 제거하고 반환하는 메서드
                //offer(): 요소를 추가하는 메서드(파이썬의 append, add와 비슷함)
            }
        }

        System.out.println(room.size());

        br.close();
    }
}


