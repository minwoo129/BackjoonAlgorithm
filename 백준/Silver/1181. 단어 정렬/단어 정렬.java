import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;

public class Main {
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String[] voca = new String[Integer.parseInt(br.readLine())];
		for(int i = 0; i < voca.length; i++) voca[i] = br.readLine();
		Arrays.sort(voca, (v1, v2) -> {
			if(v1.length() == v2.length()) {
				return v1.compareTo(v2);
			}
			else return (v1.length() - v2.length());
		});
		ArrayList<String> voca1 = new ArrayList<>();
		for(String s:voca) {
			if(!voca1.contains(s)) voca1.add(s);
		}
		voca1.forEach(s -> System.out.println(s));
		br.close();
	}
}