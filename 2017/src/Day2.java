import java.io.File;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Scanner;

public class Day2 {

	public static void main(String[] args) {
		
		File file = new File("files/day2.txt");
		ArrayList<String> in = new ArrayList<>();
		
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
		
		
		// PART 1 //
		int sum1 = 0;
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
			sum1 += (max - min);
		}
		
		System.out.println(sum1);
		
		
		// PART 2 //
		int sum2 = 0;
		for (String str : in) {
			String[] temp = str.split("\t");
			int[] tempInt = new int[temp.length];
			for (int i = 0; i < temp.length; i++) {
				tempInt[i] = Integer.parseInt(temp[i]);
			}
			
			boolean done = false;
			for (int i = 0; i < tempInt.length; i++) {
				for (int j = 0; j < tempInt.length; j++) {
					if (i != j && tempInt[i] % tempInt[j] == 0) {
						sum2 += (tempInt[i] / tempInt[j]);
						done = true;
						break;
					}
				}
				if (done) {
					done = false;
					break;
				}
			}
		}
		
		System.out.println(sum2);
		
	}
	
}
