import java.util.Arrays;
import java.util.Scanner;

public class Main {
	public static void main(String[] args){
		Scanner sc = new Scanner(System.in);
		int[][] coord = new int[sc.nextInt()][2];
		for(int i = 0; i < coord.length; i++) {
			coord[i][0] = sc.nextInt();
			coord[i][1] = sc.nextInt();
		}
		Arrays.sort(coord, (n1, n2) -> {
			if(n1[1] == n2[1]) {
				return (n1[0] - n2[0]);
			}
			else return (n1[1] - n2[1]);
		});
		
		for(int[] c:coord) {
			System.out.println(c[0] + " " + c[1]);
		}
	}
}