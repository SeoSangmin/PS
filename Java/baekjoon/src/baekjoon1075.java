import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
public class baekjoon1075{
    public static void main(String[] args) throws Exception{
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        String[] inputs = bf.readLine().split(" "); //A + B == inputs[0] + inputs[1]
        bf.close();
        int aLength = inputs[0].length();
        int bLength = inputs[1].length();
        int sumLength = Math.max(aLength, bLength);
        char sum[] = new char[sumLength];
        int plus = 0; //올림
        for(int i = 1; i<=sumLength; i++){
            int a = 0;
            int b = 0;
            if(aLength-i >= 0){
                a = inputs[0].charAt(aLength-i) - '0';
            }
            if(bLength-i>=0){
                b = inputs[1].charAt(bLength-i) - '0';
            }
            int temp = a + b + plus;
            plus = temp/10;
            sum[sumLength-i] = (char)(temp%10 + '0');
        }
        if(plus > 0){
            bw.write((char)plus+'0');
        }
        bw.write(sum);
        bw.flush();
        bw.close();
    }
}
