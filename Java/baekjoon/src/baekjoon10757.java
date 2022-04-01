import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.math.BigDecimal;
import java.util.StringTokenizer;

public class baekjoon10757 {
    public static void main(String[] args)throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st = new StringTokenizer(br.readLine());br.close();
        BigDecimal a_big = new BigDecimal(st.nextToken());
        BigDecimal b_big = new BigDecimal(st.nextToken());
        bw.write(String.valueOf(new BigDecimal(String.valueOf(a_big.add(b_big)))));
        bw.flush();
        bw.close();
    }
}

