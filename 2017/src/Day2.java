import java.io.File;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Scanner;

public class Day2 {

	public static void main(String[] args) {
		
		File file = new File("files/day2.txt");
		ArrayList<String> in = new ArrayList<>();
		int sum = 0;
		
		try {
			Scanner scan = new Scanner(file);
			while(scan.hasNext()) {
				in.add(scan.nextLine());
			}
			scan.close();
		}
		catch(Exception e) {
			e.printStackTrace();
		}
		
		for (String str : in) {
			String[] temp = str.split("\t");
			int max = Integer.MIN_VALUE;
			int min = Integer.MAX_VALUE;
			for (int i = 0; i < temp.length; i++) {
				int cur = Integer.parseInt(temp[i]);
				if (cur < min) {
					min = cur;
				}
				else if (cur > max) {
					max = cur;
				}
			}
			sum += (max - min);
		}
		
		System.out.println(sum);
		
	}
	
}
