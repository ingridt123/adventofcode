import java.io.File;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Scanner;

public class Day4 {

	public static void main(String[] args) {
		
		File file = new File("files/day4.txt");
		ArrayList<String> in = new ArrayList<>();
		
		try {
			Scanner scan = new Scanner(file);
			while (scan.hasNext()) {
				in.add(scan.nextLine());
			}
			scan.close();
			
		}
		catch(Exception e) {
			e.printStackTrace();
		}
		
		// PART 1 //
		int valid1 = 0;
		for (String str : in) {
			String[] temp = str.split(" ");
			boolean same = false;
			for (int i = 0; i < temp.length; i++) {
				for (int j = 0; j < temp.length; j++) {
					if (i != j && temp[i].equals(temp[j])) {
						same = true;
					}
				}
			}
			if (!same) {
				valid1++;
			}
		}
		System.out.println(valid1);
		
		
		// PART 2 //
		int valid2 = 0;
		for (String str : in) {
			String[] temp = str.split(" ");
			for (int i = 0; i < temp.length; i++) {
				char[] tempChar = temp[i].toCharArray();
				Arrays.sort(tempChar);
				temp[i] = new String(tempChar);
			}
			
			boolean same = false;
			for (int i = 0; i < temp.length; i++) {
				for (int j = 0; j < temp.length; j++) {
					if (i != j && temp[i].equals(temp[j])) {
						same = true;
					}
				}
			}
			if (!same) {
				valid2++;
			}
		}
		System.out.println(valid2);
		
	}
	
}
