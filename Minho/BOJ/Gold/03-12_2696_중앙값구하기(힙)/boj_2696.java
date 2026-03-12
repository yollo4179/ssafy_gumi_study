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
class Heap {
    int[] heap;
    int size = 0;
    boolean isMin;
    Heap(boolean isMin, int capacity) {
        this.isMin = isMin;
        heap = new int[capacity + 1];
    }
    boolean cmp(int parent, int child) {
        if (isMin) return heap[parent] > heap[child];
        else return heap[parent] < heap[child];
    }
    void swap(int a, int b) {
        int t = heap[a];
        heap[a] = heap[b];
        heap[b] = t;
    }
    void push(int x) {
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