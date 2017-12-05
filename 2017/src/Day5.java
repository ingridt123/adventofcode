import java.io.File;
import java.util.ArrayList;
import java.util.Scanner;

public class Day5 {

	public static void main (String[] args) {
		
		File file = new File("files/day5.txt");
		
		// PART 1 //
		ArrayList<Integer> input = new ArrayList<>();
		try {
			Scanner scan = new Scanner(file);
			while (scan.hasNext()) {
				input.add(Integer.parseInt(scan.next()));
			}
			scan.close();
		}
		catch (Exception e) {
			e.printStackTrace();
		}
		
		boolean outside1 = false;
		int steps1 = 0;
		int index1 = 0;
		while (!outside1) {
			
			try {
				
				int current = input.get(index1);
				input.set(index1, current+1);
				index1 += current;
				steps1++;
				
			}
			catch (IndexOutOfBoundsException e) {
				outside1 = true;
			}
			
		}
		System.out.println(steps1);
		
		
		// PART 2 //
		input = new ArrayList<>();
		try {
			Scanner scan = new Scanner(file);
			while (scan.hasNext()) {
				input.add(Integer.parseInt(scan.next()));
			}
			scan.close();
		}
		catch (Exception e) {
			e.printStackTrace();
		}
		
		boolean outside2 = false;
		int steps2 = 0;
		int index2 = 0;
		while (!outside2) {
			
			try {
				
				int current = input.get(index2);
				if (current >= 3) {
					input.set(index2, current-1);
				}
				else {
					input.set(index2, current+1);
				}
				index2 += current;
				steps2++;
				
			}
			catch (IndexOutOfBoundsException e) {
				outside2 = true;
			}
			
		}
		System.out.println(steps2);
	}
	
}
