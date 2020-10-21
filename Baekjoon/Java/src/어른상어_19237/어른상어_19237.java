package 어른상어_19237;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.FileReader;
import java.util.StringTokenizer;
import java.util.ArrayList;

public class 어른상어_19237 {
	private static int TC = 1;
	private static int[] dx = {-1, 0, 1, 0};
	private static int[] dy = {0, -1, 0, 1};
	
	private static int N;
	private static int M;
	private static int K;
	private static int[][] board;
	private static ArrayList<Smell>[][] smellBoard; // {시간, 번호}
	private static int[] shark_dir;
	private static int[][] shark_priority;
	private static ArrayList<int[]> shark_position;	// {상어번호, 위치x, 위치y}
	
	
	static class Smell {
		int time;
		int num;
		
		public Smell(int time, int num) {
			this.time = time;
			this.num = num;
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
			smellBoard = new ArrayList<>()();
			shark_dir = new int[M];
			shark_position = new ArrayList<int[]>(N);
			shark_priority = new int[M][4];
			
			// 격자정보 입력
			for (int i = 0; i < N ; i++) {
				st = new StringTokenizer(br.readLine());

				for (int j = 0; j < N; j++) {
					int temp = Integer.parseInt(st.nextToken());
					board[i][j] = temp;
					if (temp != 0 ) {
						int[] tmpArr = {temp, i, j};
						shark_position.add(tmpArr);
					}
				}
			}
			
			// 상어의 초기방향
			st = new StringTokenizer(br.readLine());
			for (int i = 0 ; i < M; i++) {
				shark_dir[i] = Integer.parseInt(st.nextToken());
			}
			
			// 상어의 방향 우선순위
			for (int i = 0 ; i< M; i++) {
				st = new StringTokenizer(br.readLine());
				for (int j = 0 ; j< 4; j++) {
					shark_priority[i][j] = Integer.parseInt(st.nextToken());
				}
			}
		
		}
	}
	
	
	private static void simulation() {
		// #1. 냄새 뿌리기
		for (int i = 0; i < shark_position.size(); i++) {
			int num = shark_position.get(i)[0];
			int x = shark_position.get(i)[1];
			int y = shark_position.get(i)[2];
			
			Smell tmpSmell = new Smell(num, num);
			
		
		}
	}
}
