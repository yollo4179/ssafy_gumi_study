import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class Main {

static String ans = "";
	
	static BufferedReader br;
	static BufferedWriter bw;
	static int n=0;
	static int[] arr=new int [26];
	
	
	public static void main(String args[]) throws Exception
	{
		
			
		
		br = new BufferedReader(new InputStreamReader(System.in));
		bw = new BufferedWriter (new OutputStreamWriter (System.out));
		
		String str= br.readLine().toUpperCase();
		 
		
	
		
		
		for(int i = 0 ;i<str.length();++i)
		{
			
				++arr[ str.charAt(i)-'A']; 
		}
		 
		boolean isNone = false ; 
		char ans = 0;
		int max = 0;
		for(int i = 0 ;i< 26;++i)
		{
			if(max == arr[i]) {
				isNone =true;
			}
			
			if(arr[i]> max ) {
				ans =(char)(i+'A');
				max = arr[i];
				isNone =false;
			}
			
			
			
		}
		if(true == isNone) 
			ans = '?';
		
		 
		bw.write(ans +"\n");
		bw.flush();
		bw.close();
		br.close();
		
	}
}