import java.util.Scanner;

class Main {
  public static void main(String[] args)  {
    Scanner sc = new Scanner(System.in);
    int[] arr = new int[9];
    int max = 0, idx = 0;

    for(int i = 0; i < arr.length; i++) arr[i] = sc.nextInt();

    for(int i = 0; i < arr.length; i++) {
      if(i == 0) {
        max = arr[i];
        idx = i;
      }
      else {
        max = (max > arr[i]) ? max : arr[i];
        idx = (max > arr[i]) ? idx : i;
      }
    }
    System.out.println(max);
    System.out.println(idx+1);
  }
}