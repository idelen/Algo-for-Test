package ����_19237;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.FileReader;
import java.util.*;

public class ����_19237 {
	private static int TC = 4;
	private static int[] dx = {-1, 1, 0, 0};
	private static int[] dy = {0, 0, -1, 1};	// ��, �Ʒ�, ����, ������
	
	private static int N;
	private static int M;
	private static int K;
	private static int[][] board;
	private static Smell[][] smellBoard; // {�ð�, ��ȣ}
	private static HashMap<Integer, int[][]> sharkPriority;
	//private static ArrayList<SharkStatus> sharkStatus;	// {��ġx, ��ġy}
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
		
		FileReader fr = new FileReader("src/InputSource/����_19237.txt");
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
			
			
			// �������� �Է�
			for (int i = 0 ; i < N; i++) {
				st = new StringTokenizer(br.readLine());
				for (int j = 0 ; j< N; j++) {
					board[i][j] = Integer.parseInt(st.nextToken());
					
					// ��������� �Է�
					if (board[i][j] != 0) {
						SharkStatus tmpSS = new SharkStatus(0, i, j);
						sharkStatus.put(board[i][j], tmpSS);
					}
					
					smellBoard[i][j] = new Smell(-1, -1);
				}
			}
			
			// ��� �ʱ����
			st = new StringTokenizer(br.readLine());
			for (int i = 0; i< M; i++) {
				SharkStatus tmpSS = sharkStatus.get(i+1);
				tmpSS.dir = Integer.parseInt(st.nextToken());
				sharkStatus.put(i+1, tmpSS);
			}
			
			// ��� ���� �켱���� �Է�
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
//			System.out.println(timeCount + "�� Start!!");
//			display_arr(board);
//			display(smellBoard);
//			display(sharkStatus);
			
			
			// #0. ����Ȯ��
			if (sharkStatus.size() == 1 ) {
				return timeCount;
			}
		
			// #1. ���� �Ѹ���
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
			
			//#2. ��� �̵����� �����ϱ�
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
					
					// ������ ������ �н�
					if (isWall(nx, ny)) {
						continue;
					}
					
					// #2-1. �ƹ������� ���� ���
					if(smellBoard[nx][ny].time < timeCount) {
						// ��ġ�� �� ���� ���
						if(board[nx][ny] == 0) {
							tmpSS = new SharkStatus(vector[v], nx, ny);
						
							board[nx][ny] = num;	
							sharkStatus.put(num, tmpSS);
						}
						// �̹� �ִ� ����� ��ȣ�� ���� ���
						else if(board[nx][ny] > num ) {
//							System.out.println(board[nx][ny] + "�� ��� �԰� " + num +"�� ����");
							removeNum.add(board[nx][ny]);
							
							tmpSS = new SharkStatus(vector[v], nx, ny);
							
							board[nx][ny] = num;
							sharkStatus.put(num, tmpSS);
						}
						// �̹� �ִ� ����� ��ȣ�� ���� ���
						else {
//							System.out.println(num + "�� ��� �� ��");
							removeNum.add(num);
						}
						
						flag = true;
						break;
					}
					// #2-2. �ڱ⳿�� ã��
					else if (smellBoard[nx][ny].num == num) {
						int[] tmpNx = {vector[v], nx, ny};
						nxMoving.add(tmpNx);
					}
					else {
//						System.out.println(num + "�� ��� error");
					}
				}
				// ���� ���� �� �� ã�� ��� ����
				if(!flag) {
					int nx = nxMoving.get(0)[1];
					int ny = nxMoving.get(0)[2];
					int ndir = nxMoving.get(0)[0];
					
					if(board[nx][ny] == 0) {
						tmpSS = new SharkStatus(ndir, nx, ny);
					
						board[nx][ny] = num;	
						sharkStatus.put(num, tmpSS);
					}
					// �̹� �ִ� ����� ��ȣ�� ���� ���
					else if(board[nx][ny] > num ) {
//						System.out.println(board[nx][ny] + "�� ��� �԰� " + num +"�� ����");
						removeNum.add(board[nx][ny]);
						
						tmpSS = new SharkStatus(ndir, nx, ny);
						
						board[nx][ny] = num;
						sharkStatus.put(num, tmpSS);
					}
					// �̹� �ִ� ����� ��ȣ�� ���� ���
					else {
//						System.out.println(num + "�� ��� �� ��");
						removeNum.add(num);
					}

				}
				
			}
			
			// #3. ���� ��� ��Ͽ��� ����
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
		System.out.println("===�������===");
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
