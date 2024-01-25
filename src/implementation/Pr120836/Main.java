package implementation.Pr120836;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

//프로그래머스 120836
public class Main {
    public static void main(String[] args) {
        int N = 20;
        int result = solution(N);
        System.out.println(result);
    }

    public static int solution(int N) {
        int count = 0;
        int[] NList = new int[N];

        for (int i = 1; i <= N; i++) {
            if (N % i == 0) {
                NList[i - 1] = i;
            }
        }

        for (int i = 0; i < NList.length; i++) {
            for (int j = 0; j < NList.length; j++) {
                if (NList[i] * NList[j] == N) {
                    count++;
                }
            }
        }

        return count;
    }
}
//배열돌리기 1
//배열돌리기 2
//배열돌리기 3

