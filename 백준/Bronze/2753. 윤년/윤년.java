import java.util.*;
import java.lang.*;
import java.io.*;
 
/* Name of the class has to be "Main" only if the class is public. */
class Main
{
	public static void main (String[] args) throws java.lang.Exception
	{
		Scanner sc = new Scanner(System.in);
		int year = sc.nextInt();
        year = ((year%4 == 0)&&(year%100 != 0)||(year%400 == 0)) ? 1: 0;
		System.out.println(year);
	}
}