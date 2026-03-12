
# [BOJ] 2696 - 중앙값 구하기 (Java)

## 🔗 문제 링크
[백준 2696번: 중앙값 구하기](https://www.acmicpc.net/problem/2696)


---
## 📊 성능 분석 (Performance)

| 메모리 (Memory) | 시간 (Time) | 언어 (Language) | 코드 길이 (Code Length) |
| :---: | :---: | :---: | :---: |
| **15556 KB** | **160 ms** | **Java 11** | **2460 B** |


## 📌 문제 개요
📖 문제 설명어떤 수열을 읽고, 홀수 번째 수를 읽을 때마다 지금까지 입력받은 값의 중앙값을 출력하는 프로그램을 작성하시오.예를 들어, 수열이 1, 5, 4, 3, 2이면:1번째 수(1)를 읽었을 때: 중앙값 13번째 수(4)를 읽었을 때: {1, 5, 4} 중 중앙값 45번째 수(2)를 읽었을 때: {1, 5, 4, 3, 2} 중 중앙값 3📥 입력 형식첫째 줄에 테스트 케이스의 개수 $T$ ($1 \le T \le 1,000$)가 주어진다.각 테스트 케이스:첫째 줄: 수열의 크기 $M$ ($1 \le M \le 9,999$, $M$은 홀수)둘째 줄부터: 수열의 원소가 차례대로 주어진다. (한 줄에 10개씩 나누어 입력됨)원소는 32비트 부호 있는 정수이다.📤 출력 형식각 테스트 케이스에 대해:첫째 줄: 출력하는 중앙값의 개수둘째 줄부터: 홀수 번째 수를 읽을 때마다 구한 중앙값을 차례대로 공백으로 구분하여 출력 (한 줄에 10개씩 출력)
---

## 💡 해결 프로세스

 1. 최소힙과 최대힙을 만들어 놓고 입력값을 번갈아 삽입합니다.
 2. **값을 삽입하고** 나서는 **top의 값을 비교**합니다. 최소힙에는 중앙값보다 큰 값이, 최대 힙에는 중앙값보다 작거나 같은 값이 들어가도록 합니다. 
 3. 삽입 후 top의 교환 조건은 현재 **최대 힙의 top 값**이 최소 힙의 top 값보다 **크면** 서로의 값을 바꿉니다.
 4. 중앙값은 항당 최대 힙의 top값에 위치합니다(그리디)
---

## 💻 코드 구조 상세 (Core Logic)


🔍 힙 구현
```Java
    class Heap {
    int[] heap;
    int size = 0;
    boolean isMin;
    Heap(boolean isMin, int capacity) {
        this.isMin = isMin;
        heap = new int[capacity + 1];
    }
    boolean cmp(int parent, int child) {
        //부모가 크면 자식과 바꾼다(minHeap)
        //부모가 작으면 자식과 바꾼다(maxHeap)
        if (isMin) return heap[parent] > heap[child];
        else return heap[parent] < heap[child];
    }
    void swap(int a, int b) {
        int t = heap[a];
        heap[a] = heap[b];
        heap[b] = t;
    }
    void push(int x) {
         //좌하단으로부터 부모로 비교해나간다.
        heap[++size] = x;
        int idx = size;
        while (idx > 1) {
            int parent = idx / 2;
            if (!cmp(parent, idx)) break;
            swap(parent, idx);
            idx = parent;
        }
    }
    int poll() {
         //좌하단 값을 루트로 두고 자신의 위치를 찾아나간다
        //ex minHeap ( 부모 -좌자식 -우자식 중 제일 작은 값을 가진 녀석이 부모가되도록 스왑한다.
        //스왑당한 노드는 다음 서브트리를 조사할 때 부모가 된다.
        //자신의 위치를 찾을때까지 반복- 스왑없이 부모가 제일 작을때까지 
        int ret = heap[1];
        heap[1] = heap[size--];
        int parent = 1;
        while (true) {
            int left = parent * 2;
            int right = parent * 2 + 1;
            int target = parent;
            if (left <= size && cmp(target, left))
                target = left;
            if (right <= size && cmp(target, right))
            	target = right;
            if (target == parent) break;
            swap(parent, target);
            parent = target;
        }
        return ret;
    }
    int top() {
        return heap[1];
    }
}
```

🔍 회전 함수 
```Java
  import java.util.*;
import java.io.*;

public class Main {
    static int n;
    static int[] ans;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        StringBuilder sb = new StringBuilder();
        int TC = Integer.parseInt(br.readLine());
        for (int t = 1; t <= TC; t++) {
            n = Integer.parseInt(br.readLine());
            ans = new int[n / 2 + 1];
            Heap minHeap = new Heap(true,2 * n + 1);
            Heap maxHeap = new Heap(false ,2 * n + 1); 
            int numMids = 0;
            st = new StringTokenizer(br.readLine());
            for (int i = 1; i <= n; ++i) {
                int now = Integer.parseInt(st.nextToken());
                if (i % 2 == 1) maxHeap.push(now);
                if (i % 2 == 0) minHeap.push(now);
                if (i>=2 &&   maxHeap.top() > minHeap.top()) {
                    int max = maxHeap.poll();
                    int min = minHeap.poll();
                    maxHeap.push(min);
                    minHeap.push(max);
                }
                if (i % 2 == 1) ans[numMids++] = maxHeap.top();
                if( i % 10==0)st = new StringTokenizer(br.readLine());
            }
            sb.append(numMids).append("\n");
            for(int i = 0 ;i<numMids;++i) sb.append(ans[i]).append(" ");
            sb.append("\n");
        }
        System.out.print(sb);
    }

}
```


---
⚠️ 주의 및 회고
 공부 차원에서 힙을 직접 구현해 보았습니다. 처음에는 최소힙과 최대힙을 분리하여 구현하였는데 comperator 방식으로 비교 조건을 타입에 따라 구분하여 하나로 표현할 수있었습니다.생성자에 비교 조건 및 제네릭 타입 제공이 유지보수에 도움이 된다는 것을 알았습니다.  
