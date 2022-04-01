import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
public class baekjoon2292 {
    public static void main(String[] args)throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int n = Integer.parseInt(br.readLine());
        br.close();
        if(n==1){
            bw.write(String.valueOf(1));
        } else {
            bw.write(String.valueOf(((int)(Math.sqrt((n-(5.0/4))/3.0)+(3.0/2)))));
        }
        bw.flush();
        bw.close();
    }
}
