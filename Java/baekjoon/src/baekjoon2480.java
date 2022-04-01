import java.io.*;
import java.util.StringTokenizer;

public class baekjoon2480 {
    private static int a, b, c = -1; // dice
    private static int state = -1;
    private static int maxDiceValue = -1;
    private static int sameValue = -1;

    private static int scoreCheck(int a, int b, int c){
        if( a == b && b == c) {state = 0; sameValue = a; return 0;} // all dice values are same
        if ( a == b || a == c) { sameValue = a; return 1;}
        if( b == c) { sameValue = b; return 1;} // only two dice values are same
        maxDiceValue = Math.max(Math.max(a, b), c);
        return 2; // every dice values are not same
    }

    private static int calculatePrize(){
        if( state == 0) return 10000 + (sameValue * 1000);
        if( state == 1) return 1000 + (sameValue * 100);
        return maxDiceValue * 100;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st = new StringTokenizer(bf.readLine());
        bf.close();
        a = Integer.parseInt(st.nextToken());
        b = Integer.parseInt(st.nextToken());
        c = Integer.parseInt(st.nextToken());
        state = scoreCheck(a, b, c);
        int result = calculatePrize();
        bw.write(String.valueOf(result)+"\n");
        bw.close();
    }
}
