import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Scanner;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		String[] inputArr = br.readLine().split(" ");
		int[] arr = new int[inputArr.length];
		
		for(int i = 0; i < inputArr.length; i++) {
			char c1 = inputArr[i].charAt(0), c2 = inputArr[i].charAt(1), c3 = inputArr[i].charAt(2);
			String str = c3+""+c2+""+c1;
			arr[i] = Integer.parseInt(str);
		}
		
		if(arr[0] > arr[1]) System.out.println(arr[0]);
		else System.out.println(arr[1]);
		
		br.close();
	}
}