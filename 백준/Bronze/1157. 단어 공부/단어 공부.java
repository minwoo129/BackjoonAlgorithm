import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Scanner;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String input = br.readLine().toUpperCase();
		int[] cntArr = new int[26];
		for(int i = 0; i < cntArr.length; i++) cntArr[i] = 0;
		
		for(int i = 0; i < input.length(); i++) cntArr[(int)input.charAt(i) - 'A']++;
		
		int max = 0, maxCnt = 0, idx = 0;
		for(int i = 0; i < cntArr.length; i++) {
			max = max > cntArr[i] ? max : cntArr[i];
			idx = max > cntArr[i] ? idx : i;
		}
		for(int i = 0; i < cntArr.length; i++) maxCnt += ((max == cntArr[i]) ? 1: 0);
		
		if(maxCnt == 1) System.out.println((char)('A'+idx));
		else System.out.println("?");
		
		br.close();
	}
}