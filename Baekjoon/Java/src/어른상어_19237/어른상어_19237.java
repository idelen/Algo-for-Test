package 어른상어_19237;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.FileReader;
import java.util.*;

public class 어른상어_19237 {
	private static int TC = 4;
	private static int[] dx = {-1, 1, 0, 0};
	private static int[] dy = {0, 0, -1, 1};	// 위, 아래, 왼쪽, 오른쪽
	
	private static int N;
	private static int M;
	private static int K;
	private static int[][] board;
	private static Smell[][] smellBoard; // {시간, 번호}
	private static HashMap<Integer, int[][]> sharkPriority;
	//private static ArrayList<SharkStatus> sharkStatus;	// {위치x, 위치y}
	private static HashMap<Integer, SharkStatus> sharkStatus;
	
	
	
	static class Smell {
		int time;
		int num;
		
		public Smell(int time, int num) {
			this.time = time;
			this.num = num;
		}
	}
	
	static class SharkStatus {
		int dir;
		int x;
		int y;
		
		public SharkStatus(int dir, int x, int y) {
			this.dir = dir;
			this.x = x;
			this.y = y;
		}
	}
	
	public static void main(String[] args) throws IOException {
		
		FileReader fr = new FileReader("src/InputSource/어른상어_19237.txt");
		BufferedReader br = new BufferedReader(fr);
		
		for (int t=0 ; t < TC ; t++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			
			N = Integer.parseInt(st.nextToken());
			M = Integer.parseInt(st.nextToken());
			K = Integer.parseInt(st.nextToken());
			
			board = new int[N][N];
			sharkStatus = new HashMap<Integer, SharkStatus>();
			smellBoard = new Smell[N][N];
			sharkPriority = new HashMap<Integer, int[][]>();
			
			
			// 격자정보 입력
			for (int i = 0 ; i < N; i++) {
				st = new StringTokenizer(br.readLine());
				for (int j = 0 ; j< N; j++) {
					board[i][j] = Integer.parseInt(st.nextToken());
					
					// 상어있으면 입력
					if (board[i][j] != 0) {
						SharkStatus tmpSS = new SharkStatus(0, i, j);
						sharkStatus.put(board[i][j], tmpSS);
					}
					
					smellBoard[i][j] = new Smell(-1, -1);
				}
			}
			
			// 상어 초기방향
			st = new StringTokenizer(br.readLine());
			for (int i = 0; i< M; i++) {
				SharkStatus tmpSS = sharkStatus.get(i+1);
				tmpSS.dir = Integer.parseInt(st.nextToken());
				sharkStatus.put(i+1, tmpSS);
			}
			
			// 상어 방향 우선순위 입력
			for(int k=0; k< M; k++) {
				int[][] tmpArr = new int[4][4];
				for (int i = 0; i<4; i++) {
					st = new StringTokenizer(br.readLine());
					for (int j = 0 ; j< 4; j++) {
						tmpArr[i][j] = Integer.parseInt(st.nextToken());
					}
				}
				sharkPriority.put(k+1, tmpArr);
			}
			
			int result = simulation();
			System.out.println(result);

		}
	}
	
	public static int simulation() {
		
		int timeCount = 0;
		
		while(timeCount < 1000) {
//			System.out.println(timeCount + "초 Start!!");
//			display_arr(board);
//			display(smellBoard);
//			display(sharkStatus);
			
			
			// #0. 조건확인
			if (sharkStatus.size() == 1 ) {
				return timeCount;
			}
		
			// #1. 냄새 뿌리기
			Set<Map.Entry<Integer, SharkStatus>> nowSS = sharkStatus.entrySet();
			for(Map.Entry<Integer, SharkStatus> shark: nowSS) {
				int num = shark.getKey();
				
				SharkStatus tmpSS = shark.getValue();
				int x = tmpSS.x;
				int y = tmpSS.y;
				
				Smell tmpSmell = new Smell(timeCount+K, num);
				smellBoard[x][y] = tmpSmell;
			}
			
			timeCount++;
			
			ArrayList<Integer> removeNum = new ArrayList<Integer>();
			
			//#2. 상어 이동방향 결정하기
			for(Map.Entry<Integer, SharkStatus> shark: nowSS) {
				int num = shark.getKey();
				
				SharkStatus tmpSS = shark.getValue();
				int dir = tmpSS.dir;
				int x = tmpSS.x;
				int y = tmpSS.y;
				
				
				//System.out.println(num + " " + dir + " " + x + " " + y);
				int[] vector = sharkPriority.get(num)[dir-1];
				
				boolean flag = false;
				ArrayList<int[]> nxMoving = new ArrayList<int[]>();
				board[x][y] = 0;
				
				for (int v = 0 ; v < 4 ; v++) {
					int nx = x + dx[vector[v] - 1];
					int ny = y + dy[vector[v] - 1];
					
					// 밖으로 나가면 패스
					if (isWall(nx, ny)) {
						continue;
					}
					
					// #2-1. 아무냄새가 없는 경우
					if(smellBoard[nx][ny].time < timeCount) {
						// 겹치는 상어가 없는 경우
						if(board[nx][ny] == 0) {
							tmpSS = new SharkStatus(vector[v], nx, ny);
						
							board[nx][ny] = num;	
							sharkStatus.put(num, tmpSS);
						}
						// 이미 있는 상어의 번호가 높은 경우
						else if(board[nx][ny] > num ) {
//							System.out.println(board[nx][ny] + "번 상어 먹고 " + num +"번 상어들어감");
							removeNum.add(board[nx][ny]);
							
							tmpSS = new SharkStatus(vector[v], nx, ny);
							
							board[nx][ny] = num;
							sharkStatus.put(num, tmpSS);
						}
						// 이미 있는 상어의 번호가 낮은 경우
						else {
//							System.out.println(num + "번 상어 못 들어감");
							removeNum.add(num);
						}
						
						flag = true;
						break;
					}
					// #2-2. 자기냄새 찾기
					else if (smellBoard[nx][ny].num == num) {
						int[] tmpNx = {vector[v], nx, ny};
						nxMoving.add(tmpNx);
					}
					else {
//						System.out.println(num + "번 상어 error");
					}
				}
				// 냄새 없는 곳 못 찾을 경우 수행
				if(!flag) {
					int nx = nxMoving.get(0)[1];
					int ny = nxMoving.get(0)[2];
					int ndir = nxMoving.get(0)[0];
					
					if(board[nx][ny] == 0) {
						tmpSS = new SharkStatus(ndir, nx, ny);
					
						board[nx][ny] = num;	
						sharkStatus.put(num, tmpSS);
					}
					// 이미 있는 상어의 번호가 높은 경우
					else if(board[nx][ny] > num ) {
//						System.out.println(board[nx][ny] + "번 상어 먹고 " + num +"번 상어들어감");
						removeNum.add(board[nx][ny]);
						
						tmpSS = new SharkStatus(ndir, nx, ny);
						
						board[nx][ny] = num;
						sharkStatus.put(num, tmpSS);
					}
					// 이미 있는 상어의 번호가 낮은 경우
					else {
//						System.out.println(num + "번 상어 못 들어감");
						removeNum.add(num);
					}

				}
				
			}
			
			// #3. 먹힌 상어 목록에서 제거
			for (int i =0 ; i< removeNum.size(); i++) {
				sharkStatus.remove(removeNum.get(i));
			}
			
		}
		
		return -1;
		
	}

	public static boolean isWall(int x, int y) {
		if(x < 0 || x >= N || y < 0 || y>= N) {
			return true;
		} else {
			return false;
		}
	}
	
	
	public static void display_arr(int arr[][]) {
		for (int i = 0 ; i < arr.length ; i++) {
			for (int j = 0 ; j< arr[i].length; j++) {
				System.out.print(arr[i][j] + " ");
			}
			System.out.println();
		}
		System.out.println();
	}
	
	public static void display(HashMap<Integer, SharkStatus> hashMap) {
		System.out.println("===상어정보===");
		Set<Map.Entry<Integer, SharkStatus>> entries = sharkStatus.entrySet();
		for(Map.Entry<Integer, SharkStatus> entry: entries) {
			int key = entry.getKey();
			SharkStatus value = entry.getValue();
			System.out.println(key + " " + value.dir + " " + value.x + " " + value.y);
		}
		System.out.println("===========");
	}
	
	public static void display(Smell[][] smell) {
		for (int i = 0 ; i< smell.length; i++) {
			for (int j = 0 ; j< smell[i].length; j++) {
				System.out.print("("+ smell[i][j].time + ", " + smell[i][j].num + ")" + " ");
			}
			System.out.println();
		}
	}
}
