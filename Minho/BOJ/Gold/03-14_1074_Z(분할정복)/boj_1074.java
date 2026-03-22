import java.util.*;
import java.io.*;

public class Main {

    static int N,R,C;
    static int cnt;
    static int ans =-1;
    static int dq(int r, int c, int s) {
        int ret = 0 ;
        if(ans != -1 )return 0;
        if( s == 1 )  return 1;

        int half = s >>1;
        int val =half*half;

        if( r <half && c>=half) ret+= val;
        if( r >=half && c<half) ret+= val*2;
        if( r >=half && c>=half) ret+= val*3;
        int newR = (r>=half)? r-half: r;
        int newC = (c>=half)? c-half: c;
        ret += dq(newR,newC, half);



        return ret ;

    }

    public static void main(String[] args) throws Exception {
        StringTokenizer st ;
        BufferedReader br = new BufferedReader(new InputStreamReader (System.in));


        st = new StringTokenizer( br.readLine());

        N = Integer.parseInt(st.nextToken());
        R = Integer.parseInt(st.nextToken());
        C = Integer.parseInt(st.nextToken());

        ans = dq(R,C, 1<<N )-1;

        System.out.print(ans);


        // TODO Auto-generated method stub

    }

}
