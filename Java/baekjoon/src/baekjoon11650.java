import java.awt.*;
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class baekjoon11650 {
    static boolean compare(Point a, Point b)
    {
        boolean result = true;
        if(a.x == b.x)
        {
            if(a.y < b.y){ result = false;}
        }
        if(a.x < b.x) { result = false;}
        return result;
    }

    static Point[] sortedPoint = new Point[100000];
    static int tempIdx = 0;
    static void mergeSort(Point[] points, int start, int end)
    {
        if(end - start < 1) {
            sortedPoint[start] = points[start]; return;
        }

        int mid = (start + end) / 2;
        int left = start;
        int right = mid + 1;

        mergeSort(points, start, mid);
        mergeSort(points, right, end);

        tempIdx = start;
        while(true)
        {
            if(compare(points[left], points[right])){
                sortedPoint[tempIdx++] = points[right++];
                if( right > end ){
                    for(int i = left; i < mid+1; i++){
                        sortedPoint[tempIdx++] = points[i];
                    }
                    break;
                }
            } else {
                sortedPoint[tempIdx++] = points[left++];
                if( left > mid ){
                    for(int i = right; i < end; i++){
                        sortedPoint[tempIdx++] = points[i];
                    }
                    break;
                }
            }
        }

        for(int i = start; i < end + 1; i++){
            points[i] = sortedPoint[i];
        }
    }
    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int n = Integer.parseInt(br.readLine());
        Point points[] = new Point[n];

        for(int i = 0; i < n; i++)
        {
            String str = br.readLine();
            StringTokenizer st = new StringTokenizer(str);
            int x = Integer.parseInt(st.nextToken());
            int y = Integer.parseInt(st.nextToken());
            Point point = new Point(x, y);
            points[i] = point;
        }
        br.close();

        mergeSort(points, 0, n-1);
        for(int i = 0; i < n; i++){
            bw.write(String.valueOf(points[i].x));
            bw.write(" ");
            bw.write(String.valueOf(points[i].y));
            bw.newLine();
        }
        bw.flush();
        bw.close();
    }
}