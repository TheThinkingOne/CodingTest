package bruteForce.boj2503;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new FileReader("D:/CodingTest/src/bruteForce/boj2503/input.txt"));
        int N = Integer.parseInt(br.readLine()); // 예제에서 N = 4

        List<String[]> candidates = new ArrayList<>();

        for (int i = 1; i <= 9; i++) {
            for (int j = 1; j <= 9; j++) {
                for (int k = 1; k <= 9; k++) {
                    if (i != j && j != k && k != i) {
                        candidates.add(new String[]{Integer.toString(i), Integer.toString(j), Integer.toString(k)});
                    }
                }
            }
        }

        for (int i = 0; i < N; i++) {
            String[] values = br.readLine().split(" ");
            int n = Integer.parseInt(values[0]);
            int s = Integer.parseInt(values[1]);
            int b = Integer.parseInt(values[2]);

            List<String[]> tempCandidates = new ArrayList<>();

            for (String[] num : candidates) {
                int strike = 0;
                int ball = 0;

                String[] numDigits = Integer.toString(n).split(""); // 수정된 부분

                for (int j = 0; j < 3; j++) {
                    if (num[j].equals(numDigits[j])) { // 수정된 부분
                        strike++;
                    } else if (contains(numDigits, num[j])) { // 수정된 부분
                        ball++;
                    }
                }

                if (strike == s && ball == b) {
                    tempCandidates.add(num);
                }
            }

            candidates = tempCandidates;
        }

        System.out.println(candidates.size());
        br.close();
    }

    private static boolean contains(String[] array, String value) {
        for (String element : array) {
            if (element.equals(value)) {
                return true;
            }
        }
        return false;
    }
}


