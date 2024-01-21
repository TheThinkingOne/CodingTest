package greedyAlgorithm.boj11000;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.io.FileReader;


import java.util.Scanner;
import java.util.LinkedList;

public class boj11000 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int TC = scanner.nextInt();

        for (int t = 0; t < TC; t++) {
            int N = scanner.nextInt();
            int M = scanner.nextInt();
            LinkedList<int[]> queue = new LinkedList<>();

            for (int i = 0; i < N; i++) {
                int priority = scanner.nextInt();
                queue.add(new int[]{i, priority});
            }

            int target = M;
            int count = 0;

            while (true) {
                if (queue.getFirst()[1] == maxPriority(queue)) {
                    if (target == 0) {
                        count++;
                        System.out.println(count);
                        break;
                    } else {
                        queue.poll(); // pop the front element
                        N--; // decrease the size of the queue
                        target = (target - 1 + N) % N; // update the target index
                        count++;
                    }
                } else {
                    queue.addLast(queue.poll()); // rotate the queue
                }
            }
        }
    }

    private static int maxPriority(LinkedList<int[]> queue) {
        int max = Integer.MIN_VALUE;
        for (int[] element : queue) {
            max = Math.max(max, element[1]);
        }
        return max;
    }
}

