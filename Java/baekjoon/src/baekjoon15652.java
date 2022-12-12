import java.io.*;
import java.util.StringTokenizer;

public class baekjoon15652 {
    static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    static int n;
    static int m;
    static void recursion(int[] arr, int idx) throws IOException {
        int v = idx == 0 ? 1 : arr[idx - 1];
        if (idx == m) {
            for (int i = 0; i < m; ++i)
                bw.write(String.valueOf(arr[i]) + " ");
            bw.write("\n");
            return;
        }
        while (v <= n) {
            arr[idx] = v++;
            recursion(arr, idx + 1);
        }
    }
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        int[] arr = new int[m];
        recursion(arr, 0);
        bw.flush();
        bw.close();
    }
}
