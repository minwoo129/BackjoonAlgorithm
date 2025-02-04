import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Scanner;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		String input = br.readLine();
		int sum = 0;
		
		String[][] numArr = {
				{"", "2"},
				{"ABC", "3"},
				{"DEF", "4"},
				{"GHI", "5"},
				{"JKL", "6"},
				{"MNO", "7"},
				{"PQRS", "8"},
				{"TUV", "9"},
				{"WXYZ", "10"},
				{"", "11"}
				};
		for(int i = 0; i < input.length(); i++) {
			char n = input.charAt(i);
			for(int j = 0; j < numArr.length; j++) {
				if(numArr[j][0].indexOf(n+"") != -1) sum += (Integer.parseInt(numArr[j][1]));
			}
		}
		System.out.println(sum);
		
		br.close();
	}
}