import java.util.*;
import java.lang.*;
import java.io.*;
 
/* Name of the class has to be "Main" only if the class is public. */
class Main
{
	public static void main (String[] args) throws java.lang.Exception
	{
		Scanner sc = new Scanner(System.in);
		int h = sc.nextInt(), m = sc.nextInt();
 
		if(m-45 < 0) {
			h = (h == 0) ? 23 : h-1;
			m = 60 - (45-m);
		}
		else m -= 45;
		System.out.println(h + " " + m);
	}
}