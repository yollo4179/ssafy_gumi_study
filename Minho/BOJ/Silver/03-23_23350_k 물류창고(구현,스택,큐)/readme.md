# [BOJ] 23350 - K 물류창고 (Java)

## 🔗 문제 링크

[백준 23350: K 물류창고](https://www.acmicpc.net/problem/23350)

---

## 📊 성능 분석 (Performance)

| 메모리 (Memory) | 시간 (Time) | 언어 (Language) | 코드 길이 (Code Length) |
| :-------------: | :---------: | :-------------: | :---------------------: |
|  **14296 KB**   | **108 ms**  |   **Java 11**   |       **2172 B**        |

## 📌 문제 개요

<h2>문제</h2>
<hr>
<pre>
K사의 물류창고를 운영하는 도커 씨는 오늘 발주를 처리하기 위해 N 개의 컨테이너들을 적재해야 한다. 도커씨는 이 일을 하나의 로봇을 이용해 처리하려 한다. 로봇은 컨테이너를 옮길 때마다 컨테이너의 무게만큼 비용을 발생시킨다.

컨테이너마다 우선순위가 있는데 우선순위는 1 이상 M 이하의 정수로 표현된다. 우선순위가 1에 가까울 수록 높은 우선순위를 가지고, M에 가까울 수록 낮은 우선순위를 가진다. M개의 각 우선순위에 대하여 해당 우선순위를 갖는 컨테이너가 적어도 하나 존재한다.

컨테이너는 레일을 통해 하나씩 오고, 우선순위가 낮은 컨테이너를 먼저 적재한다. 낮은 우선순위의 컨테이너들이 모두 적재되지 않은 상태에서 높은 우선순위의 컨테이너가 온다면 레일의 처음으로 보낸다. 레일의 처음으로 보낼 때, 컨테이너의 무게만큼 비용이 발생한다. 낮은 우선순위의 컨테이너가 온다면, 무조건 적재한다.

컨테이너의 우선순위가 같을 땐, 무게가 무거운 컨테이너를 아래에 위치시킨다.

컨테이너의 우선순위가 같으면서 무게도 같은 경우는 어느 것이 위에 있어도 상관없다.

우선순위는 같으나, 무게가 가벼운 컨테이너가 먼저 적재돼 있을 경우, 가벼운 컨테이너가 무거운 컨테이너 위로 갈 수 있도록 컨테이너를 빼내고 다시 적재한다. 이 과정을, 가벼운 컨테이너가 모두 빠질 때까지 반복한다. 이 과정에서 컨테이너를 뺄 때와 적재될 때 컨테이너의 무게만큼 비용이 발생한다.

작업이 모두 끝난 후 도커 씨가 부담해야 할 비용을 출력하자.

</pre>

<hr>
<h2>입력</h2>

첫째 줄엔 컨테이너의 개수 $N$과 우선순위의 종류 $M$이 주어진다. ($1 \le M \le N \le 100$)
2번째 줄부터 $N + 1$번째 줄까지는 컨테이너들의 우선순위 $P$ ($1 \le P \le M$), 무게 $W$ ($1 \le W \le 100$)가 순서대로 주어진다.

- 레일에 배치되는 순서는 입력으로 주어지는 컨테이너의 순서와 동일하다.
- 모든 입력은 1 이상의 정수이다.

<hr>
<h2>출력</h2>
<p>입력에서 0이 주어진 횟수만큼 답을 출력한다. 만약 배열이 비어 있는 경우인데 가장 큰 값을 출력하라고 한 경우에는 0을 출력하면 된다.</p>
<hr>

## 💡 해결 프로세스

1. 우선 순위 빈도 기록하기
2. 큐에서 원소를 꺼내고 현재 우선순위와 같다면 적재,
3. 적재할 때, 현재 stack의 top보다 무겁다면, stack에 있는 거 다 임시 스택에 담은 후에 원본에 적재.
4. 현재 우선 순위의 박스를 다 담았다면 `stack을 비운` 다음에 다음 우선순위의 상자들을 적재(이전에 쌓아놓은 박스들이 무게조건에 의해 우선순위 조건이 망가지는 것을 방지)

---

## 💻 코드 구조 상세 (Core Logic)

🔍 시물레이션 구현 카운팅-> 우선순위 카운팅-> 스택 핑퐁

```Java

for(int i = 0; i < n; ++i) {
			st = new StringTokenizer(br.readLine());
			items[i][0] = Integer.parseInt(st.nextToken()); // 우선순위
			items[i][1] = Integer.parseInt(st.nextToken()); // 무게
			que.add(items[i]);
			++priorities[items[i][0]];
		}

		int ans = 0;
		while(!que.isEmpty()) {

			// 2. 현재 우선순위를 다 처리했으면, 다음(더 높은) 우선순위로 이동
			if(nowPriority >= 1 && priorities[nowPriority] == 0) {
				nowPriority--;
				stk.clear(); // : 우선순위가 바뀌었으므로 비교용 스택을 비워줌
			}
			if(nowPriority == 0) break;

			// 가중치(우선순위)가 다른 경우 -> 뒤로 보내기
			if(que.getFirst()[0] != nowPriority) {
				int[] now = que.pollFirst();
				ans += now[1];
				que.offerLast(now);
				continue;
			}

			// 가중치(우선순위)가 같은 경우 (적재)
			priorities[nowPriority]--;
			int nowWeight = que.pollFirst()[1];

			if(stk.isEmpty() || stk.peek() >= nowWeight) {
				stk.push(nowWeight);
				ans += nowWeight;
				continue;
			}

			// stack의 top이 현재 무게보다 가벼운 경우 빼기
			while(!stk.isEmpty() && stk.peek() < nowWeight) {
				ans += stk.peek();
				tmp.push(stk.pop());
			}

			stk.push(nowWeight);
			ans += nowWeight;

			// tmp에 빼둔 것들 다시 올리기
			while(!tmp.isEmpty()) {
				ans += tmp.peek();
				stk.push(tmp.pop());
			}
		}
```

🔍 세팅(사전 준비)

```Java
 	public class Main {
    static int n;

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
		//...Logic

    }
}

```

⚠️ 주의 및 회고
우선순위 조건이 무게조건 때문에 망가질 수 있으므로 일단 스택을 비운다.
