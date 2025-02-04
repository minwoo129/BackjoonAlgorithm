import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		int n = Integer.parseInt(br.readLine());

		for(int i = 1; i <= n; i++) {
			String str = "";
			for(int j = 1; j <= (n-i); j++) str += " ";
			for(int j = 1; j <= i; j++) str += "*";
			bw.write(str + "\n");
		}
		br.close();
		bw.close();
	}
}