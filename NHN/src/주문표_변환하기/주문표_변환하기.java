package 주문표_변환하기;

import java.util.Scanner;

class 주문표_변환하기 {
	
  private static void solution(int numOfOrder, String[] orderArr) {
    // TODO: 이곳에 코드를 작성하세요. 추가로 필요한 함수와 전역변수를 선언해서 사용하셔도 됩니다.
	  
	  for (int t = 0; t < numOfOrder; t++) {
		  String order = orderArr[t];
		  String queue = new String();
		  for (int i = 0 ; i< order.length(); i++) {
			  char word = order.charAt(i);
			  
			  if (word != ')') {
				  queue += word;
			  }
			  else {
				  String tmp = new String();
				  int idx = i;
				  
				  while(true) {
					  String w = queue.substring(queue.length()-1);
					  queue = queue.substring(0, queue.length()-1);
					  char tmpWord = w.charAt(0);
					  
					  if (Character.isDigit(tmpWord)) {
						  int num = Integer.parseInt(w);
						  String s = tmp;
						  for(int n=0; n< num-1; n++) {
							  tmp += s;
						  }
						  
					  } 
					  
					  else if(tmpWord == '(') {
						  String p = queue.substring(queue.length()-1);
						  queue = queue.substring(0, queue.length()-1);
						  char prior = p.charAt(0);
						  
						  if (Character.isDigit(prior)) {
							  int num = Integer.parseInt(p);
							  String s = tmp;
							  String returnString = new String();
							  for(int n=0; n< num; n++) {
								  returnString += s;
							  }
							  
							  queue += returnString;
							  
						  } else {
							  String returnString = new String();
							  
							  for (int sdx=0; sdx<tmp.length(); sdx++) {
								  String tmpString = String.valueOf(prior)+ String.valueOf(tmp.charAt(sdx));
								  returnString += tmpString;
							  }
							  queue += returnString;
						  }
						  
						  break;
					  }
					  
					  else {
						  tmp = tmpWord + tmp;
					  }
				  }
			  }
		  }
		  
		  System.out.println(queue);
	  }
  }

  private static class InputData {
    int numOfOrder;
    String[] orderArr;
  }

  private static InputData processStdin() {
    InputData inputData = new InputData();

    try (Scanner scanner = new Scanner(System.in)) {
      inputData.numOfOrder = Integer.parseInt(scanner.nextLine().replaceAll("\\s+", ""));

      inputData.orderArr = new String[inputData.numOfOrder];
      for (int i = 0; i < inputData.numOfOrder; i++) {
        inputData.orderArr[i] = scanner.nextLine().replaceAll("\\s+", "");
      }
    } catch (Exception e) {
      throw e;
    }

    return inputData;
  }

  public static void main(String[] args) throws Exception {
    InputData inputData = processStdin();

    solution(inputData.numOfOrder, inputData.orderArr);
  }
}