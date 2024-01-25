import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashSet;
import java.util.Set;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new FileReader("D:/CodingTest/src/unclassified/boj10815/input.txt"));

        int N = Integer.parseInt(br.readLine());
        Set<Integer> setN = new HashSet<>();
        StringTokenizer stN = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            setN.add(Integer.parseInt(stN.nextToken()));
        }

        int M = Integer.parseInt(br.readLine());
        Set<Integer> setM = new HashSet<>();
        StringTokenizer stM = new StringTokenizer(br.readLine());
        for (int i = 0; i < M; i++) {
            setM.add(Integer.parseInt(stM.nextToken()));
        }

        for (int i : setM) {
            if (setN.contains(i)) {
                System.out.print(1 + " ");
            } else {
                System.out.print(0 + " ");
            }
        }
        br.close();
    }
}

