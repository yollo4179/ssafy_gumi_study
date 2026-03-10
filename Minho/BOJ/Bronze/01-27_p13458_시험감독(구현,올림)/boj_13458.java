import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class Main {

    static String ans = "";

    static BufferedReader br;
    static BufferedWriter bw;
    static int n=0;


    public static void main(String args[]) throws Exception
    {


        br = new BufferedReader(new InputStreamReader(System.in));
        bw = new BufferedWriter (new OutputStreamWriter (System.out));

        n = Integer.parseInt(br.readLine());

        StringTokenizer st = new StringTokenizer(br.readLine());
        int[] arr = new int [n];

        for(int i = 0 ;i< n;++i)
        {
            arr[i]= Integer.parseInt(st.nextToken());
        }
        st= new StringTokenizer(br.readLine());


        int b = Integer.parseInt(st.nextToken());
        int c = Integer.parseInt(st.nextToken());

        long ans = 0 ;
        for(int i = 0 ;i< n;++i)
        {
            ans+=1;
            int k =  (arr[i] -b);

            if(k <= 0) 	continue;



            ans+=(k +c-1)/c;
        }



        bw.write(ans +"\n");
        bw.flush();
        bw.close();
        br.close();

    }
}