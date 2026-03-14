
# [BOJ] 2580 - 스도쿠 (Java)

## 🔗 문제 링크
[백준 2580번: 스도쿠](https://www.acmicpc.net/problem/2580)


---
## 📊 성능 분석 (Performance)

| 메모리 (Memory) | 시간 (Time) | 언어 (Language) | 코드 길이 (Code Length) |
| :---: | :---: | :---: | :---: |
| **18572 KB** | **260 ms** | **Java 11** | **1787 B** |


## 📌 문제 개요
📖9 x 9 크기의 스도쿠가 주어진다. 스도쿠는 풀 수 있는 경우만 주어지며, 채워진 공간과 빈 공간의 정보가 주어진다. 빈공간은 0으로 채워지고 각 공간은 1~9까지의 숫자를 부여받는다
스도쿠는 3 x 3로 분할된 부분 배열, 각 열, 각 행 마다 1~9까지의 숫자가 반드시 하나 씩 존재하도록 숫자를 채워넣어야 한다.     
---

## 💡 해결 프로세스

 1. 빈 공간의 위치를 저장할 2차원 배열을 만들고, 0이 입력으로 주어지면 그 빈 공간의 위치를  따로 저장합니다.
 2. 행과 열 단위로 3 등분한 3*3 섹션과 1~9 행, 1~9 열에 대해 1~9까지의 숫자가 체크 되었는지를 확인하기 위해서, 방문 배열을 만듦니다.  
 3. 0이 아니면 자신이 위치에 속하느 영역에 대해서 sections[ 0~3 등분 행 ][ 0~3 등분 열 ][1-9 숫자], rows[0~8 행 ][1-9 숫자],cols[0~8 행 ][1-9 숫자] 배열을 체크합니다. 
 4. 빈공간에 숫자를 하나씩 넣어보면서 백트래킹을 수행합니다.
---

## 💻 코드 구조 상세 (Core Logic)


🔍 백트래킹 구현
```Java
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
```

🔍 기본 세팅 및 방문 배열 초기화
```Java
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
```


---
⚠️ 주의 및 회고
 N 퀸 문제와 유사한 전형적인 백트래킹 문제였습니다. 
