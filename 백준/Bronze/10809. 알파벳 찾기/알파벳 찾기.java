import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String input = br.readLine();
		int[] idxArr = new int[26];
		for(int i = 0; i < idxArr.length; i++) idxArr[i] = -1;
		
		for(int i = 0; i < input.length(); i++) {
			char c = input.charAt(i);
			int idx = (int)c - 'a';
			if(idxArr[idx] == -1) idxArr[idx] = i;
		}
		for(int idx: idxArr) System.out.print(idx + " ");
		System.out.println();
		br.close();
	}
}