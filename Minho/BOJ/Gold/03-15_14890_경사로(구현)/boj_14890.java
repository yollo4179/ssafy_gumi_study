import java.util.*;
import java.io.*;

public class Main {

    static int len ;
    static int n ;
    static int ans;
    static int[][]area1;
    static int[][]area2;
    //row 기준으로 search
    static boolean checkR(int[][] area, int r ) {
        int prev = area[r][0];
        int sameHeight = 1;
        for(int c = 1 ;c<n ;++c) {
            int now = area[r][c];

            if(now == prev) ++sameHeight;
            else if( now - 1 == prev&& sameHeight >= len) sameHeight = 1;
            else if( now + 1 == prev) {
                int rep =len;
                if( len -1 + c >= n)return false;
                while(rep-->0) {
                    if( area[r][c] != area[r][c +rep]) return false;
                }
                c += len-1;
                sameHeight= 0;
            }
            else return false;
            prev =now;
        }


        return true;
    }
    //사실 입력받을 때, transpose 할 필요없이 입력을 한번에 처리하면 굳이 쓸 필요없다.
    // arr1[i][j]  arr2[j][i]
    static void transpose(final int[][]arr1 ,int[][] arr2) {
        for(int i = 0;i<n;++i)
            for(int j = 0 ;j<n;++j) {
                arr2[i][j] = arr1[j][i];
            }
    }
    static void Search(int[][] area) {
        for(int i = 0 ; i < n ; ++i) {
            if(checkR(area, i)==true)
                ++ans;
        }
    }
    public static void main(String[] args) throws Exception {
        StringTokenizer st ;
        BufferedReader br = new BufferedReader(new InputStreamReader (System.in));


        st = new StringTokenizer( br.readLine());

        n = Integer.parseInt(st.nextToken());
        len = Integer.parseInt(st.nextToken());
        area1 = new int[n][n];
        area2 = new int[n][n];

        for(int i = 0 ;i< n;++i) {
            st = new StringTokenizer(br.readLine());
            for(int j  =0 ; j< n;++j) {
                area1 [i][j] = Integer.parseInt(st.nextToken());
            }
        }
        Search(area1);
        transpose(area1,area2);
        Search(area2);


        System.out.print(ans);


        // TODO Auto-generated method stub

    }

}
