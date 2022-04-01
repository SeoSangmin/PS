import java.io.*;
import java.util.ArrayList;

public class baeckjoon11725 {


    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int N = Integer.parseInt(br.readLine());
        ArrayList<ArrayList<Integer>> tree = new ArrayList<>(N+1);
        for(int i=0; i < N+1; i++) {
            tree.add(new ArrayList());
        }

        int[][] box = new int[N-1][2];
        String[] split;
        for(int i = 0; i < N-1; i++){
            split = br.readLine().split(" ");
            for(int j = 0; j < 2; j++){
                box[i][j] = Integer.parseInt(split[j]);
            }
        }
        br.close();

        bw.write("\n");
        for(int i = 0; i < N-1; i++){
            for(int j = 0; j < 2; j++){
                bw.write(String.valueOf(box[i][j]) + " ");
            }
            bw.write("\n");
        }
        bw.flush();
    }
}
