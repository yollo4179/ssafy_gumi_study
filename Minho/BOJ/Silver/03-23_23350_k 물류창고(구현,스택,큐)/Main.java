import java.util.*;
import java.io.*;

public class Main {

	static int n;
	static int m;
	static int[][] items;
	static int[] priorities = new int[101];

	public static void main(String[] args) throws Exception {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());

		n = Integer.parseInt(st.nextToken());
		m = Integer.parseInt(st.nextToken());
		items = new int[n][2];

		// 1. 가장 낮은 우선순위인 m부터 시작하여 1까지 내려갑니다.
		int nowPriority = m;

		ArrayDeque<int[]> que = new ArrayDeque<>();
		ArrayDeque<Integer> stk = new ArrayDeque<>();
		ArrayDeque<Integer> tmp = new ArrayDeque<>();

		for (int i = 0; i < n; ++i) {
			st = new StringTokenizer(br.readLine());
			items[i][0] = Integer.parseInt(st.nextToken()); // 우선순위
			items[i][1] = Integer.parseInt(st.nextToken()); // 무게
			que.add(items[i]);
			++priorities[items[i][0]];
		}

		int ans = 0;
		while (!que.isEmpty()) {

			// 2. 현재 우선순위를 다 처리했으면, 다음(더 높은) 우선순위로 이동
			if (nowPriority >= 1 && priorities[nowPriority] == 0) {
				nowPriority--;
				stk.clear(); // : 우선순위가 바뀌었으므로 비교용 스택을 비워줌
			}
			if (nowPriority == 0)
				break;

			// 가중치(우선순위)가 다른 경우 -> 뒤로 보내기
			if (que.getFirst()[0] != nowPriority) {
				int[] now = que.pollFirst();
				ans += now[1];
				que.offerLast(now);
				continue;
			}

			// 가중치(우선순위)가 같은 경우 (적재)
			priorities[nowPriority]--;
			int nowWeight = que.pollFirst()[1];

			if (stk.isEmpty() || stk.peek() >= nowWeight) {
				stk.push(nowWeight);
				ans += nowWeight;
				continue;
			}

			// stack의 top이 현재 무게보다 가벼운 경우 빼기
			while (!stk.isEmpty() && stk.peek() < nowWeight) {
				ans += stk.peek();
				tmp.push(stk.pop());
			}

			stk.push(nowWeight);
			ans += nowWeight;

			// tmp에 빼둔 것들 다시 올리기
			while (!tmp.isEmpty()) {
				ans += tmp.peek();
				stk.push(tmp.pop());
			}
		}

		System.out.print(ans);
	}
}