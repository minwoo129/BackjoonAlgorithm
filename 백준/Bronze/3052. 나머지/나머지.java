import java.util.ArrayList;
import java.util.Scanner;

class Main {
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    
    int[] arr = new int[10];
    for(int i = 0; i < arr.length; i++) arr[i] = sc.nextInt();

    ArrayList<Integer> remArr = new ArrayList<>();

    for(int i = 0; i < arr.length; i++) {
      if(!remArr.contains(arr[i]%42)) remArr.add(arr[i]%42); 
    }

    System.out.println(remArr.size());
  }
}