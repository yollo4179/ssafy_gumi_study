
# [BOJ] 1021 - 회전하는 큐 (Java)

## 🔗 문제 링크
[백준 1021: 회전하는 큐](https://www.acmicpc.net/problem/1021)


---
## 📊 성능 분석 (Performance)

| 메모리 (Memory) | 시간 (Time) | 언어 (Language) | 코드 길이 (Code Length) |
| :---: | :---: | :---: | :---: |
| **14248 KB** | **108 ms** | **Java 11** | **1168 B** |


## 📌 문제 개요
<h2>문제</h2>
<hr>
<pre>
지민이는 N개의 원소를 포함하고 있는 양방향 순환 큐를 가지고 있다. 지민이는 이 큐에서 몇 개의 원소를 뽑아내려고 한다.

지민이는 이 큐에서 다음과 같은 3가지 연산을 수행할 수 있다.

첫 번째 원소를 뽑아낸다. 이 연산을 수행하면, 원래 큐의 원소가 a1, ..., ak이었던 것이 a2, ..., ak와 같이 된다.
왼쪽으로 한 칸 이동시킨다. 이 연산을 수행하면, a1, ..., ak가 a2, ..., ak, a1이 된다.
오른쪽으로 한 칸 이동시킨다. 이 연산을 수행하면, a1, ..., ak가 ak, a1, ..., ak-1이 된다.
큐에 처음에 포함되어 있던 수 N이 주어진다. 그리고 지민이가 뽑아내려고 하는 원소의 위치가 주어진다. (이 위치는 가장 처음 큐에서의 위치이다.) 이때, 그 원소를 주어진 순서대로 뽑아내는데 드는 2번, 3번 연산의 최솟값을 출력하는 프로그램을 작성하시오.
</pre>

<hr>
<h2>입력</h2>
<p>첫째 줄에 큐의 크기 N과 뽑아내려고 하는 수의 개수 M이 주어진다. N은 50보다 작거나 같은 자연수이고, M은 N보다 작거나 같은 자연수이다. 둘째 줄에는 지민이가 뽑아내려고 하는 수의 위치가 순서대로 주어진다. 위치는 1보다 크거나 같고, N보다 작거나 같은 자연수이다.</p>
<hr>
<h2>출력</h2>
<p>첫째 줄에 문제의 정답을 출력한다.</p>
<hr>

## 💡 해결 프로세스

 1. 디큐를 배열로 관리한다.
 2. front가 원하는 값이 아니라면 양옆으로 전진하며 원하는 값을 조사한다.   
 3. 더 짧은 시간안에 도달한 길이만큼 답에 더한다.
 4. 1,2,3 과정을 모든 타겟을 뽑을때까지 반복한다.
---

## 💻 코드 구조 상세 (Core Logic)


🔍 투포인터
```Java
   for(int t=0; t<m ; t++) {
			int now = Integer.parseInt(st.nextToken());
			while(q[idx] == -1) {
                idx = (idx + 1) % n;
            }
			int l=idx;
			int r= idx ;
			int lenL = 0;
			int lenR = 0;
			//search
			while(q[l]!=now) {
				l= (n+l -1)% n;
				if(q[l]!=-1)++lenL;
			};
			while(q[r]!=now) {
				r= (r +1)% n;
				if(q[r]!=-1)++lenR;
			}
			if( lenL <lenR) {
				ans+=lenL; 
				idx = (l+1)%n;
				q[l]=-1;
			}
			else {
				ans+=lenR;
				idx = (r + 1) % n;
				q[r]=-1;
			}
		}
		System.out.print(ans+"");
```
🔍 세팅(사전 준비)
```Java
 	static int n ; 
	static int m ;
	static int[] pos;
	static int numEls;
	static int idx;
	static int[] q;
	public static void main(String[] args) throws Exception {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st= new StringTokenizer( br.readLine());
		n = Integer.parseInt(st.nextToken());
		m = Integer.parseInt(st.nextToken());
		
		pos = new int[m];
		q = new int[n];
		for(int i = 0 ;i< n;++i) {
			q[i]=i+1;
		}
		int ans =0;
		st= new StringTokenizer( br.readLine());
		//..........로직
}

```

⚠️ 주의 및 회고
배열보다 진짜  deque로 처리해서 타겟의 위치를 조사한 후 len/2 길이 안에 타겟이 있으면 오른쪽, 그렇지 않다면 왼쪽으로 가는 방식을 사용하면 좀더 연산을 줄일 수 있다. 
