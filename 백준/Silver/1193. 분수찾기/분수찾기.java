import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int n = sc.nextInt();
		int pos = 0, i = 1;
		while(true) {
			if(pos + i < n) {
				pos += i;
				i++;
			}
			else break;
		}
		i++;
		if(i%2 == 1) System.out.println((n-pos) + "/" + (i-(n-pos)));
		else System.out.println((i-(n-pos)) + "/" + (n-pos));
		
	}
}