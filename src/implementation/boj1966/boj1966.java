package implementation.boj1966;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.Arrays;

//백준 1966 프린터 큐
public class boj1966 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new FileReader("D:/CodingTest/src/implementation/boj1966/input.txt"));
        // Read from file
        int TC = Integer.parseInt(br.readLine());

        for (int t = 0; t < TC; t++) {
            String[] inputNM = br.readLine().split(" ");
            int N = Integer.parseInt(inputNM[0]);
            int M = Integer.parseInt(inputNM[1]);

            String[] priorityStrings = br.readLine().split(" ");
            int[] Priority = Arrays.stream(priorityStrings).mapToInt(Integer::parseInt).toArray();

            int target = M;
            int count = 0;

            while (true) {
                if (Priority[0] == Arrays.stream(Priority).max().getAsInt()) {
                    if (target == 0) {
                        count++;
                        System.out.println(count);
                        break;
                    } else {
                        Priority = Arrays.copyOfRange(Priority, 1, N);
                        N--;
                        target--;
                        count++;
                    }
                } else {
                    int temp = Priority[0];
                    System.arraycopy(Priority, 1, Priority, 0, N - 1);
                    Priority[N - 1] = temp;
                    target = (target - 1 + N) % N;
                }
            }
        }
        br.close(); // Close the BufferedReader
    }
}







