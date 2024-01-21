package implementation.boj1966;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.io.FileReader;

public class Main {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new FileReader("D:/CodingTest/src/implementation/boj1966/input.txt"));
        int TC = Integer.parseInt(br.readLine());

        for (int t = 0; t < TC; t++) {
            String[] inputNM = br.readLine().split(" ");
            int N = Integer.parseInt(inputNM[0]);
            int M = Integer.parseInt(inputNM[1]);

            String[] priortityStrings = br.readLine().split(" ");
            int[] priortiy = Arrays.stream(priortityStrings).mapToInt(Integer::parseInt).toArray();
        }

    }
}
