//// 시간초과..
//import java.io.*;
//import java.util.StringTokenizer;
//
//public class baekjoon18870 {
//    private static int n = -1;
//    private static int[] arr;
//    private static int[] removedArr;
//    static int[] removeDuplicate(int[] arr){
//        for(int i = 0; i < arr.length; i++){
//            for(int j = i+1; j < arr.length; j++){
//                if(arr[i] == arr[j]) removedArr[j] = Integer.MAX_VALUE;
//            }
//        }
//        return removedArr;
//    }
//    static int XapostropheNum(int[] removedArr, int X) {
//        int res = 0;
//        for(int j = 0; j < removedArr.length; j++){
//            if(removedArr[j] < X) res++;
//        }
//        return res;
//    }
//    public static void main(String[] args) throws IOException {
//        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
//        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
//
//        n = Integer.parseInt(bf.readLine());
//        arr = new int[n];
//        removedArr = new int[n];
//        StringTokenizer st = new StringTokenizer(bf.readLine());
//        bf.close();
//        for(int i = 0; i < n; i++) {
//            arr[i] = Integer.parseInt(st.nextToken());
//            removedArr[i] = arr[i];
//        }
//        removedArr = removeDuplicate(arr);
//        for(int i = 0; i < n; i++){
//            int temp = XapostropheNum(removedArr, arr[i]);
//            bw.write(String.valueOf(temp)+" ");
//        }
//        bw.flush();
//        bw.close();
//    }
//}

import java.util.Arrays;
import java.io.*;
import java.util.HashMap;
import java.util.StringTokenizer;

public class baekjoon18870 {
    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        HashMap<Integer, Integer> rankingMap = new HashMap<Integer, Integer>();

        int n = Integer.parseInt(bf.readLine());
        int[] arr = new int[n];
        int[] sorted = new int[n];
        int rank = 0;

        StringTokenizer st = new StringTokenizer(bf.readLine());
        for(int i = 0; i < n; i++){
            arr[i] = Integer.parseInt(st.nextToken());
            sorted[i] = arr[i];
        }
        bf.close();
        Arrays.sort(sorted);
        // code here

        for(int v : sorted) {
            /*
             *  이 때 만약 앞선 원소가 이미 순위가 매겨졌다면
             *  중복되면 안되므로, 원소가 중복되지 않을 때만
             *  map에 원소와 그에 대응되는 순위를 넣어준다.
             */
            if(!rankingMap.containsKey(v)) {
                rankingMap.put(v, rank);
                rank++;		// map에 넣고나면 다음 순위를 가리킬 수 있도록 1을 더해준다.
            }
        }

        for(int i = 0; i < n; i++){
            bw.write(String.valueOf(rankingMap.get(arr[i])));
            bw.write(" ");
        }
        bw.flush();
        bw.close();
    }
}