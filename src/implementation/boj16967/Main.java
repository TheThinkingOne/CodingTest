package implementation.boj16967;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.PriorityQueue;
import java.util.StringTokenizer;
import java.io.InputStreamReader;
public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer nums = new StringTokenizer(br.readLine());

        String[] inputHWXY = br.readLine().split(" ");
        int H = Integer.parseInt(inputHWXY[0]);
        int W = Integer.parseInt(inputHWXY[1]);
        int X = Integer.parseInt(inputHWXY[2]);
        int Y = Integer.parseInt(inputHWXY[3]);

        int[][] MyMap = new int[H+X][W+Y];

        for (int i=0; i<H+X; i++) {
            nums = new StringTokenizer(br.readLine());
            for (int j=0; j < W+Y; j++) {
                MyMap[i][j] = Integer.parseInt(nums.nextToken());
            }
        }

        for (int i=X; i<H; i++) {
            for (int j=Y; j<W; j++) {
                MyMap[i][j] -= MyMap[i-X][j-Y];
            }
        }

        for (int y=0; y<H; y++) {
            for (int x=0; x<W; x++) {
                System.out.println(MyMap[y][x] + " ");
            }
            System.out.println();
        }
    }
}
