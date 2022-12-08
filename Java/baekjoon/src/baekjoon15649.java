import java.io.*;
import java.util.StringTokenizer;

public class baekjoon15649 {
    static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    static int n;
    static int m;

    private static void dp(int[] arr, int idx, int[] visited) throws IOException {
        if (idx == m) {
            for (int i = 0; i < m; ++i) {
                bw.write(String.valueOf(arr[i]));
                bw.write(" ");
            }
            bw.write("\n");
            return;
        }

        for (int i = 0; i < n; ++i) {
            if (visited[i] == 0) continue;
            arr[idx] = i + 1;
            visited[i] = 0;
            dp(arr, idx + 1, visited);
            visited[i] = 1;
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(bf.readLine());

        int[] visited;
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        bf.close();
        int[] arr = new int[m];
        visited = new int[n];

        for (int i = 0; i < n; ++i)
            visited[i] = 1;
        dp(arr, 0, visited);
        bw.flush();
        bw.close();
    }
}
