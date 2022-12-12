import java.io.*;
import static java.lang.Math.abs;

public class baekjoon9663 {
    static int ret = 0;
    static int n;
    static int[] arr;
    static boolean check(int idx) {
        for (int i = 0; i < idx; ++i) {
            if (arr[i] == arr[idx])
                return false;
            if (abs(arr[i] - arr[idx]) == idx - i)
                return false;
        }
        return true;
    }
    static void recursion(int idx) {
        int value = 1;
        if (idx == n) {
            ret++;
            return;
        }
        while (value <= n) {
            arr[idx] = value;
            if (check(idx))
                recursion(idx + 1);
            else
                arr[idx] = 0;
            value++;
        }
    }
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        n = Integer.parseInt(br.readLine());
        arr = new int[n];
        recursion(0);
        bw.write(String.valueOf(ret));
        bw.flush();
        bw.close();
        br.close();
    }
}
