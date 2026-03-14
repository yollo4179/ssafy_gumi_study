
import java.util.*;
import java.io.*;
public class Main {
    static int map[][] = new int[9][9] ;
    static boolean[][][] sections =new boolean[3][3][10];
    static StringBuilder sb = new StringBuilder();

    static int[][] positions= new int [81][2];
    static int numB =0;
    static boolean [][] rows= new boolean[9][10];
    static boolean [][] cols= new boolean[9][10];
    static void printAll() {
        for(int i = 0 ;i< 9;++i) {
            for(int j = 0 ;j< 9;++j) {
                sb.append(map[i][j]).append(" ");
            }
            sb.append("\n");
        }
    }
    static boolean hasCompleted = false;
    static void back(int lv) {
        if(hasCompleted==true) return;
        if(lv ==numB &&hasCompleted ==false) {
            printAll();
            hasCompleted =true;
            return;
        }
        int[] now = positions[lv];
        for(int i = 1 ;i< 10;++i) {
            if(rows[now[0]][i] ==true) continue;
            if(cols[now[1]][i] ==true) continue;
            if(sections[now[0]/3][now[1]/3][i]==true)continue;
            map[now[0]][now[1]] = i;
            cols[now[1]][i] =true;
            rows[now[0]][i] =true;
            sections[now[0]/3][now[1]/3][i]=true;
            back(1+ lv);
            map[now[0]][now[1]] = 0;
            cols[now[1]][i] =false;
            rows[now[0]][i] =false;
            sections[now[0]/3][now[1]/3][i] = false;
        }

    }
    public static void main(String[] args) throws Exception {
        StringTokenizer st ;
        BufferedReader br = new BufferedReader(new InputStreamReader (System.in));


        for(int i = 0 ;i< 9;++i) {
            st = new StringTokenizer(br.readLine());
            for(int j =0 ;j< 9;++j) {
                map[i][j] = Integer.parseInt(st.nextToken());
                if(map[i][j]== 0) {
                    positions[numB++] = new int[] {i,j};
                }
                else {
                    rows[i][map[i][j]]=true;
                    cols[j][map[i][j]]=true;
                    sections[i/3][j/3][map[i][j]] = true;
                }
            }
        }
        back(0);
        System.out.print(sb);


        // TODO Auto-generated method stub

    }

}