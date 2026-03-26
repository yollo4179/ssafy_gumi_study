import java.util.*;
import java.io.*;

public class Main {

	static int n;
	static int m;
	static int[][] arr;
	static int[] dr = { 0, 0, 1, -1 };
	static int[] dc = { 1, -1, 0, 0 };
	static int ans = Integer.MAX_VALUE;
	static boolean[][][] vis;
	static int dist[][];
 
	public static void main(String[] args) throws Exception {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());

		n = Integer.parseInt(st.nextToken());
		m = Integer.parseInt(st.nextToken());
		arr = new int[n][m];
		vis = new boolean[n][m][2];
		for (int i = 0; i < n; ++i) {
			String line = br.readLine();
			for (int j = 0; j < m; ++j) {
				arr[i][j] = line.charAt(j) - '0';
			}
		}
		// dfs(0, 0, 1, 1);
		ArrayDeque<int[]> q = new ArrayDeque<>();
		q.add(new int[] { 0, 0, 1, 1 });// r,c,break,len;
		while (!q.isEmpty()) {
			int[] now = q.poll();

			int r = now[0];
			int c = now[1];
			int through = now[2];
			int len = now[3];
			if (r == n - 1 && c == m - 1) {
				ans = len;
				break;
			}

			for (int i = 0; i < 4; ++i) {
				int nr = r + dr[i];
				int nc = c + dc[i];
				if (nr < 0 || nr >= n || nc < 0 || nc >= m)
					continue;
				if (vis[nr][nc][through] == true)
					continue;
				if (through == 0 && arr[nr][nc] == 1)
					continue;
				int updatethrough = through;
				if (through == 1 && arr[nr][nc] == 1) {
					updatethrough -= 1;
				}
				q.add(new int[] { nr, nc, updatethrough, len + 1 });
				vis[nr][nc][updatethrough] = true;
			}
		}

		if (ans == Integer.MAX_VALUE)
			ans = -1;
		System.out.print(ans);
	}
}