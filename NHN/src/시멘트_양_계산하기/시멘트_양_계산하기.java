package 시멘트_양_계산하기;

import java.util.Scanner;

class 시멘트_양_계산하기 {
  private static void solution(int day, int width, int[][] blocks) {
    // TODO: 이곳에 코드를 작성하세요. 추가로 필요한 함수와 전역변수를 선언해서 사용하셔도 됩니다.
	  int result = 0;
	  int[] building = new int[width];
	  
	  for (int i = 0; i < day; i++ ) {
		  int[] block = blocks[i];
		  
		  // 1. 벽돌쌓기
		  for (int b= 0 ; b< width; b++) {
			  building[b] += block[b];
		  }
		  
		  // 2. 시멘트 바르기
		  for(int idx = 1; idx < width - 1; idx++) {
			  int nowHeight = building[idx];
			  int leftMax = nowHeight;
			  int rightMax = nowHeight;
			  
			  
			  for(int left=idx-1; left >=0; left--) {
				  if (leftMax < building[left]) {
					  leftMax = building[left];
				  }
			  }
			  
			  for(int right=idx+1; right < width; right++) {
				  if(rightMax < building[right]) {
					  rightMax = building[right];
				  }
			  }
			  
			  int realMax = 0;
			  
			  // 더 작은 값을 기준으로 시멘트 채우기
			  if (leftMax < rightMax) {
				  realMax = leftMax;
			  } else {
				  realMax = rightMax;
			  }
			  
			  building[idx] += (realMax - nowHeight);
			  result += (realMax - nowHeight);
			  
		  }
	  }
	  System.out.println(result);
  }
  
  private static class InputData {
    int day;
    int width;
    int[][] blocks;
  }

  private static InputData processStdin() {
    InputData inputData = new InputData();

    try (Scanner scanner = new Scanner(System.in)) {
      inputData.day = Integer.parseInt(scanner.nextLine().replaceAll("\\s+", ""));      
      inputData.width = Integer.parseInt(scanner.nextLine().replaceAll("\\s+", ""));
      
      inputData.blocks = new int[inputData.day][inputData.width];
      for (int i = 0; i < inputData.day; i++) {
        String[] buf = scanner.nextLine().trim().replaceAll("\\s+", " ").split(" ");
        for (int j = 0; j < inputData.width; j++) {
          inputData.blocks[i][j] = Integer.parseInt(buf[j]);
        }
      }
    } catch (Exception e) {
      throw e;
    }

    return inputData;
  }

  public static void main(String[] args) throws Exception {
    InputData inputData = processStdin();

    solution(inputData.day, inputData.width, inputData.blocks);
  }
  
	
	public static void display(int arr[]) {
		for (int i = 0 ; i < arr.length ; i++) {
			System.out.print(arr[i] + " ");
		}
		System.out.println();
	}
}