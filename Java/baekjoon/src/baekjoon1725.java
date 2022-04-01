import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.io.BufferedReader;
import java.io.BufferedWriter;
public class baekjoon1725 {
    static long histo(int[] v, int a, int b) {
        if(a==b) return v[a];
        int w, h, left, right;
        long max = 0;

        for(int i=0; i<=b; i++) {
            w=1;
            left = 1;
            right = 1;
            h = v[i];
            //if(i==0) {while(v[i+w]>=h) {w++;} max = Math.max(max, h*w);w=1;}
            //if(i==b) {System.out.println(i+" "+w);while(v[i-w]>=h) {w++;} max = Math.max(max, h*w);w=1;}
            while((i-left)>=0 && v[i-left]>=h) {left++;w++;}
            while((i+right)<=b && v[i+right]>=h) {right++;w++;}
            max = Math.max(max, h*w);

        }

        return max;
    }

    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int n = Integer.parseInt(br.readLine());
        int[] v = new int[n*2];
        for(int i = 0;i<n;i++) {
            v[i] = Integer.parseInt(br.readLine());
        }
        long r = histo(v,0,n-1);
        bw.write(String.valueOf(r));
        bw.flush();
        bw.close();
        br.close();
    }
}
