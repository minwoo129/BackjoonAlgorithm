import java.util.*;
import java.lang.*;
import java.io.*;
 
/* Name of the class has to be "Main" only if the class is public. */
class Main
{
	public static void main (String[] args) throws java.lang.Exception
	{
		Scanner sc = new Scanner(System.in);
		int score = sc.nextInt();
 
		if((score >= 90)&&(score <= 100)) System.out.println("A");
        else if((score >= 80)&&(score < 90)) System.out.println("B");
        else if((score >= 70)&&(score < 80)) System.out.println("C");
        else if((score >= 60)&&(score < 70)) System.out.println("D");
        else System.out.println("F");
	}
}