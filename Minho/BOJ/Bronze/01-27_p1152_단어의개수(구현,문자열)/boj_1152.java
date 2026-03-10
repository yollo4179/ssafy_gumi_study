import java.io.*;
import java.util.*;


//백준에 돌리거나, 파일명과 클래스명을 같도록해야 돌아갑니다.
public class Main {

    static String ans = "";

    static BufferedReader br;
    static BufferedWriter bw;
    
    public static void main(String args[]) throws Exception
    {


        br = new BufferedReader(new InputStreamReader(System.in));
        bw = new BufferedWriter (new OutputStreamWriter (System.out));

        StringTokenizer st= new StringTokenizer(br.readLine());
        int ans =0;



        while(st.hasMoreTokens())
        {
            ++ans;
            st.nextToken();
        }
        bw.write(ans +"\n");
        bw.flush();
        bw.close();
        br.close();

    }
}
