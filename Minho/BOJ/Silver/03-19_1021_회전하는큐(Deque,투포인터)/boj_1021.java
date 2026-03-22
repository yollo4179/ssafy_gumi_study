import java.util.*;
import java.io.*;

public class Main {


    static int n ;
    static int m ;
    static int[] pos;
    static int numEls;
    static int idx;
    static int[] q;
    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st= new StringTokenizer( br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        pos = new int[m];
        q = new int[n];
        for(int i = 0 ;i< n;++i) {
            q[i]=i+1;
        }
        int ans =0;
        st= new StringTokenizer( br.readLine());
        for(int t=0; t<m ; t++) {
            int now = Integer.parseInt(st.nextToken());

            while(q[idx] == -1) {
                idx = (idx + 1) % n;
            }

            int l=idx;
            int r= idx ;
            int lenL = 0;
            int lenR = 0;
            //search
            while(q[l]!=now) {
                l= (n+l -1)% n;
                if(q[l]!=-1)++lenL;
            };
            while(q[r]!=now) {
                r= (r +1)% n;
                if(q[r]!=-1)++lenR;
            }
            if( lenL <lenR) {
                ans+=lenL;
                idx = (l+1)%n;
                q[l]=-1;
            }
            else {
                ans+=lenR;

                idx = (r + 1) % n;

                q[r]=-1;
            }
        }
        System.out.print(ans+"");


    }
}
