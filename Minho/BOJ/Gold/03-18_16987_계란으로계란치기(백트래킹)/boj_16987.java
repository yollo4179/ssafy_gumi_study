import java.util.*;
import java.io.*;

public class Main {

    static int n ;
    static int[] w;
    static int[] d;
    static boolean [] hasBroken;
    static int ans;
    static void dfs(int lv,int lives) {

        if( lv>=n) {
            ans = Math.max(ans, lives);
            return ;
        }
        if( d[lv] <=0){ dfs(lv+1,lives);return;}
        for(int i = 0 ;i< n ;++i) {
            if( i==lv ||d[i] <= 0 )continue;
            d[lv]-= w[i];
            d[i]-= w[lv];
            int acc= 0;
            if(d[lv]<=0)++acc;
            if(d[i]<=0)++acc;
            dfs(lv+1,lives+acc);
            d[lv]+= w[i];
            d[ i]+= w[lv];
        }
        ans = Math.max(ans, lives);
    }
    public static void main(String[] args) throws Exception {
        StringTokenizer st ;
        BufferedReader br = new BufferedReader(new InputStreamReader (System.in));
        st = new StringTokenizer( br.readLine());
        n = Integer.parseInt(st.nextToken());


        w = new int[n];
        d = new int[n];
        hasBroken =new boolean[n];
        for(int i = 0 ;i<n;++i) {
            st =new StringTokenizer(br.readLine());
            d[i] = Integer.parseInt(st.nextToken());
            w[i] = Integer.parseInt(st.nextToken());
        }

        dfs(0,0);


        System.out.print(ans);
    }

}
