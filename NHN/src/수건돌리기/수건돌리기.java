package ���ǵ�����;

import java.util.Scanner;
import java.util.HashMap;

public class ���ǵ����� {
  private static void solution(int numOfAllPlayers, int numOfQuickPlayers, char[] namesOfQuickPlayers, int numOfGames, int[] numOfMovesPerGame){
    // TODO: �̰��� �ڵ带 �ۼ��ϼ���. �߰��� �ʿ��� �Լ��� ���������� �����ؼ� ����ϼŵ� �˴ϴ�.
		int[] count = new int[numOfAllPlayers];
		int[] nowPlayer = new int[numOfAllPlayers-1];
		int[] quickPlyaer = new int[26];
		
		count[0] = 1;
		
		// �ɾ��ִ� �÷��̾� ����
		for (int i = 0; i < numOfAllPlayers-1; i++) {
			nowPlayer[i] = i+1;
		}
		
		// �÷��̾� �̸� �ε�����ȣ�� ġȯ(A:65 ~ Z:90)
		for (int i = 0; i < numOfQuickPlayers; i++) {
			quickPlyaer[(int)namesOfQuickPlayers[i]-65] = 1;
		}
		
		int cur = 0;
		int actor = 0;
		
		for (int i = 0; i < numOfGames; i++) {
			int numOfMove = numOfMovesPerGame[i];
			
			cur += numOfMove;
			
			if (cur < 0) {
				cur += numOfAllPlayers - 1;
			} else if (cur >= numOfAllPlayers-1) {
				cur -= numOfAllPlayers - 1;
			}
			
			if (quickPlyaer[nowPlayer[cur]] == 1) {
				count[actor]++;
			} else {
				int tmp = nowPlayer[cur];
				nowPlayer[cur] = actor;
				actor = tmp;
				
				count[actor]++;
			}
			
		}
		
		for(int i = 0 ; i< nowPlayer.length; i++) {
			int playerNum = nowPlayer[i]; 
			System.out.println((char)(playerNum + 65) + " " + count[nowPlayer[i]]);
		}
		System.out.println((char)(actor + 65) + " " + count[actor]);	
		
  }

  private static class InputData {
    int numOfAllPlayers;
    int numOfQuickPlayers;
    char[] namesOfQuickPlayers;
    int numOfGames;
    int[] numOfMovesPerGame;
  }

  private static InputData processStdin() {
    InputData inputData = new InputData();

    try (Scanner scanner = new Scanner(System.in)) {
      inputData.numOfAllPlayers = Integer.parseInt(scanner.nextLine().replaceAll("\\s+", ""));

      inputData.numOfQuickPlayers = Integer.parseInt(scanner.nextLine().replaceAll("\\s+", ""));
      inputData.namesOfQuickPlayers = new char[inputData.numOfQuickPlayers];
      System.arraycopy(scanner.nextLine().trim().replaceAll("\\s+", "").toCharArray(), 0, inputData.namesOfQuickPlayers, 0, inputData.numOfQuickPlayers);

      inputData.numOfGames = Integer.parseInt(scanner.nextLine().replaceAll("\\s+", ""));
      inputData.numOfMovesPerGame = new int[inputData.numOfGames];
      String[] buf = scanner.nextLine().trim().replaceAll("\\s+", " ").split(" ");
      for(int i = 0; i < inputData.numOfGames ; i++){
        inputData.numOfMovesPerGame[i] = Integer.parseInt(buf[i]);
      }
    } catch (Exception e) {
      throw e;
    }

    return inputData;
  }

  public static void main(String[] args) throws Exception {
    InputData inputData = processStdin();

    solution(inputData.numOfAllPlayers, inputData.numOfQuickPlayers, inputData.namesOfQuickPlayers, inputData.numOfGames, inputData.numOfMovesPerGame);
  }
}