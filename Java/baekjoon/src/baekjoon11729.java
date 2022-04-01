import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class baekjoon11729 {
    static StringBuilder sb = new StringBuilder();
    public static void move(int from, int to){
        String temp = String.format("%d %d\n",from, to);
        sb.append(temp);
    }
    public static int hanoi(int from, int to, int other, int disks){
        if(disks == 1){
            move(from, to);
            return 1;
        } else {
            return hanoi(from, other, to, disks-1) +
                    hanoi(from, to, other, 1) +
                    hanoi(other, to, from, disks-1) + 1;
        }
    }
    public static void main(String[] args) throws Exception{
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int n = Integer.parseInt(bf.readLine()); // input : number of disks
        bf.close();
        int res = hanoi(1, 3, 2, n);
        bw.write(String.valueOf(res));
        bw.newLine();
        bw.write(sb.toString());
        bw.flush();
        bw.close();
    }
}
