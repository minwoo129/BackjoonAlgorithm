import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;

public class Main {
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(br.readLine());
		ArrayList<Person> person = new ArrayList<>();
		for(int i = 0; i < n; i++) person.add(new Person(br.readLine()));
		Collections.sort(person);
		for(int i = 0; i < n; i++) System.out.println(person.get(i).getData());
		
		br.close();
	}
}
class Person implements Comparable<Person>{
	private String data;
	private int age;
	private String name;
	
	public Person(String data) {
		this.data = data;
		
		String[] d = data.split(" ");
		this.age = Integer.parseInt(d[0]);
		this.name = d[1];
	}
	
	@Override
	public int compareTo(Person o) {
		// TODO Auto-generated method stub
		if(this.age == o.age) {
			return 0;
		}
		else return (this.age > o.age) ? 1 : -1;
	}

	public String getData() {
		return data;
	}
	public void setData(String data) {
		this.data = data;
	}
	
}