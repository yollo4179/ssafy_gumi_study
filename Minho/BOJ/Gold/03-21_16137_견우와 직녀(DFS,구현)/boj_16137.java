import java.util.*;
import java.io.*;

public class Main {

    static int[] dr = { -1, 0, 1, 0 };
    static int[] dc = { 0, 1, 0, -1 };
    static int N;
    static int M;
    static int[][] map;
    static int[][] dist;
    //오작교를 설치할 수  있는 계곡인지 조사한다.
    //( 시계 방향으로 연속된 2개의 방향을 조사 ㄱ자 모양의 계곡은 오작교 설치 불가)
    static boolean check(int r,int c) {
        boolean ret = false;
        for (int d = 0; d < 4; ++d) {
            int nxtr = r + dr[(d + 1) % 4];
            int nxtc = c + dc[(d + 1) % 4];
            int nowr = r + dr[d];
            int nowc = c + dc[d];
            if (nxtr < 0 || nxtr >= N || nxtc < 0 || nxtc >= N)
                continue;
            if (nowr < 0 || nowr >= N || nowc < 0 || nowc >= N)
                continue;
            if (!(map[nxtr][nxtc] == 0 && map[nowr][nowc] == 0))
                continue;
            ret = true;
            break;
        }
        return ret;
    }
    static void dfs(int r, int c, int nowTime, int numBridges) {

        if (dist[r][c] <= nowTime)
            return;
        dist[r][c] = Math.min(dist[r][c], nowTime);
        for (int d = 0; d < 4; ++d) {
            int nr = r + dr[d];
            int nc = c + dc[d];
            int nowBridges = numBridges;
            int dur = -1;
            int nextTime = nowTime;

            if (nr < 0 || nr >= N || nc < 0 || nc >= N) continue;
            if (map[r][c] != 1 && map[nr][nc] != 1) continue;
            if (map[nr][nc] == 1) {
                nextTime = nowTime + 1;
            }
            /*연속으로 오작교 건너면 안된다.*/
            else if (map[r][c]==1 && map[nr][nc] > 1) {
                dur = map[nr][nc];
            }
            else if (nowBridges == 0 && map[nr][nc] == 0)
                continue;
            else if (nowBridges == 1 && map[nr][nc] == 0) {
                if(check(nr,nc)==true)continue;
                nowBridges--;
                dur = M;
            }
            //만든거든 이미 있는 거든 오작교 건너려면 DURATION의 배수가 되어야 한다.
            // M초일때 '딱 오작교 위'에 있어야함
            if (dur != -1) {
                nextTime =(nowTime / dur + 1) * dur;
            }


            dfs(nr, nc, nextTime, nowBridges);
        }
    }

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        map = new int[N][N];
        dist = new int[N][N];
        for (int i = 0; i < N; ++i) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < N; ++j) {
                map[i][j] = Integer.parseInt(st.nextToken());
                dist[i][j] = Integer.MAX_VALUE;
            }
        }

        dfs(0, 0, 0, 1);
        System.out.print(dist[N - 1][N - 1]);
    }
}
