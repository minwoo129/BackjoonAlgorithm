import java.util.Scanner;

public class Main {

	public static int sub = 1;
	public static int num = 1;
	public static void main(String[] args){
		Scanner sc = new Scanner(System.in);
		
		Fact(sc.nextInt());
		System.out.println(sub);
	}
	
	public static void Fact(int n) {
		if(n != 0) {
			sub *= num;
			if(num != n) {
				num++;
				Fact(n);
			}
		}
	}	
}