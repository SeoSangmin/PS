import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class test {

    public static void main(String[] args) throws NumberFormatException, IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        String strN = br.readLine();
        int cnt = strN.length();
        int n = Integer.parseInt(strN);



        int sum =0;				//합계
        int number=0;

        for(int i= n-9*cnt;i<n;i++) {
            sum = i;
            number =i; 		//while문 내에서 돌릴 number;
            while(number!=0) {
                sum += number%10;
                number =number/10;
            }
            if(sum==n) {
                bw.write(i+"");
                bw.flush();
                bw.close();
                br.close();

                return;
            }
        }
        bw.write(0+"");
        bw.flush();
        bw.close();
        br.close();


    }
}