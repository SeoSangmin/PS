import java.io.*;
import java.util.StringTokenizer;

public class baekjoon15650 {
    static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    static int n, m;

    static void dp(int[] arr, int idx) throws IOException {
        int value = idx == 0 ? 1 : arr[idx - 1] + 1;

        if (idx == m) {
            for (int i = 0; i < m; ++i) {
                bw.write(String.valueOf(arr[i]));
                bw.write(String.valueOf(" "));
            }
            bw.write("\n");
            return;
        }
        while (value <= (n - m + idx + 1)) {
            arr[idx] = value++;
            dp(arr, idx + 1);
        }
    }
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        br.close();
        int[] arr = new int[m];
        dp(arr, 0);
        bw.flush();
        bw.close();
    }
}

