# [BOJ] 25918 - 북극곰은 괄호를 찢어 (Java)

## 🔗 문제 링크

[백준 25918: 북극곰은 괄호를 찢어](https://www.acmicpc.net/problem/25918)

---

## 📊 성능 분석 (Performance)

| 메모리 (Memory) | 시간 (Time) | 언어 (Language) | 코드 길이 (Code Length) |
| :-------------: | :---------: | :-------------: | :---------------------: |
|  **21936 KB**   | **240 ms**  |   **Java 11**   |       **1012 B**        |

## 📌 문제 개요

<h2>문제</h2>
<hr>
<pre>
극지 연구소에서 연구 중인 협이는 새로운 북극곰의 특성을 발견했다. 그것은 바로 북극곰이 
O와 X를 보면 ()와 )(로 찢어버린다는 것이다.

협이는 이러한 북극곰의 특성을 이용하여 길이 N의 괄호 문자열 S를 만들고자 한다. 북극곰은 낮에 활동을 하기 때문에 낮에 돌아다니는 것은 위험하다. 때문에 협이는 매일 밤마다 활동할 수 있다. 밤에 협이는 문자열이 있으면 그 위에 O 또는 X를 원하는 만큼 놓을 수 있다. 그러면 낮에 북극곰이 와서 문자들을 모두 찢어 놓는다.

예를 들어 이미 문자열
()()가 있다고 생각해보자. 밤에 문자를
(O)X(O) 다음과 같이 놓아둔다면 하루가 지나
(()))((()) 와 같은 문자열이 된다.

이때 원하는 문자열을 만들려면 최소 며칠이 걸리는지 계산해보자.

</pre>

<hr>
<h2>입력</h2>
 
<p>N</p>
<p>S</p>

<hr>
<h2>출력</h2>
<p>
원하는 문자열을 만들기 위해 걸리는 최소 일수를 구하라.
원하는 문자열을 만들 수 없다면 -1을 출력한다.</p>
<hr>
<h2>제한</h2>
<p>
1<=N <= 200,000 
</p>
<p>
S는 '(' 또는 ')'로 이루어져 있다.
</p>
<hr>

## 💡 해결 프로세스

1. 괄호쌍문제와 유사하게 현재 stack의 top과 현재 관찰 중인 문자가 괄호쌍을 만족한다면, stack을 팝하고 넘어간다. continue
2. top과 괄호쌍을 이루지 않는다면 stack에 현재 문자를 적재한다.
3. 문자를 적재하면서 ,현재 괄호쌍이 몇 층으로 겹쳐있는지(스택의 사이즈)를 기록한다. [([([) (])])]-> 3층 적재
4. 과정을 마친 후 스택이 비어있지 않다면 괄호쌍을 만들 수 없느 경우이므로 -1을 출력한다.

---

## 💻 코드 구조 상세 (Core Logic)

🔍 괄호 쌍 쌓기 -> 문자를 쌓을 때마다, 스택사이즈 (몇 겹인지) 기록

```Java

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
		if (0 !=  stack.size())
		{
			ans = -1;
		}
		System.out.print(ans);
```

🔍 세팅(사전 준비)

```Java
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
		//...Logic
}

```

⚠️ 주의 및 회고
스택의 괄호쌍 문제와 유사하나 규칙을 발견하지 못하고 2중 for 문으로 접근하면 시간초과 난다. (((((((((((((......))))))))))))) while문안에서 계속 반복문 돌리면 10만 \*10만이어서 매우 효율이 안좋다.
