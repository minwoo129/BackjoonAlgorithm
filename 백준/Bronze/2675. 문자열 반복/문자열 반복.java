import java.util.Scanner;

public class Main {

	public static void main(String[] args){
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		String[] resArr = new String[n];
		for(int i = 0; i < n ; i++) {
			
			int cnt = sc.nextInt();
			String str = sc.next(), res = "";
			for(int j = 0; j < str.length(); j++) {
				for(int k = 0; k < cnt; k++) res += (str.charAt(j)+"");
			}
			resArr[i] = res;
		}
		for(String res:resArr) System.out.println(res);
	}
}