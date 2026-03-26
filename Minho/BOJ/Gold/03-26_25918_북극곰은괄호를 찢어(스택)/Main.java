import java.util.*;
import java.io.*;

public class Main {

	static int n;
	static int m;
	static int[] arr;

	public static void main(String[] args) throws Exception {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		// StringTokenizer st = new StringTokenizer(br.readLine());

		n = Integer.parseInt(br.readLine());
		String str = br.readLine();
		Deque<Character> line = new ArrayDeque<Character>();
		for (int i = 0; i < str.length(); ++i) {
			line.add(str.charAt(i));
		}
		// 앞에서부터 없애는 것이 이득
		int ans = 0;
		if (line.size() % 2 == 1) {
			System.out.print(-1);
			return;
		}

		Deque<Character> stack = new ArrayDeque<>();
		for (char c : line) {
			if (!stack.isEmpty()) {
				char top = stack.peek();

				if ((top == '(' && c == ')') || (top == ')' && c == '(')) {
					stack.pop();
					continue;
				}
			}
			stack.push(c);
			ans = Math.max(stack.size(), ans);
		}

		if (0 != stack.size()) {
			ans = -1;
		}
		System.out.print(ans);
	}
}