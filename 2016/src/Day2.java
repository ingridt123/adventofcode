import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.Scanner;

public class Day2 {

	private static final String[][] KEYPAD1 = {{"1", "2", "3"}, {"4", "5", "6"}, {"7", "8", "9"}};
	private static final String[][] KEYPAD2 = {{"", "", "1", "", ""},
											   {"", "2", "3", "4", ""},
											   {"5", "6", "7", "8", "9"},
											   {"", "A", "B", "C", ""},
											   {"", "", "D", "", ""}};
	private ArrayList<String> input;
	
	public static void main (String[] args) {
		
		File file = new File("day2.txt");
		ArrayList<String> input = new ArrayList<String>();
		
		try {
			Scanner scan = new Scanner(file);
			while (scan.hasNext()) {
				input.add(scan.nextLine());
			}
			scan.close();
		}
		catch (FileNotFoundException e) {
			e.printStackTrace();
		}
		
		Day2 two = new Day2(input);
		System.out.println(two.findButtons1());
		System.out.println(two.findButtons2());
	}
	
	public Day2 (ArrayList<String> in) {
		input = in;
	}
	
	/**
	 * code for task 1
	 */
	public String findButtons1() {
		String passcode = "";
		int butRow = 1;
		int butCol = 1;
		for (String in : input) {
			for (int i = 0; i < in.length(); i++) {
				String currentIn = in.substring(i, i+1);
				int newRow = butRow;
				int newCol = butCol;
				switch (currentIn) {
					case "U":
						newRow--;
						break;
					case "D":
						newRow++;
						break;
					case "L":
						newCol--;
						break;
					case "R":
						newCol++;
						break;
				}
				if (!(newRow < 0 || newRow > 2 || newCol < 0 || newCol > 2)) {
					butRow = newRow;
					butCol = newCol;
				}
			}
			passcode = passcode + KEYPAD1[butRow][butCol]; 
		}
		return passcode;
	}
	
	/**
	 * code for task 2
	 */
	public String findButtons2() {
		String passcode = "";
		int butRow = 2;
		int butCol = 0;
		for (String in : input) {
			for (int i = 0; i < in.length(); i++) {
				String currentIn = in.substring(i, i+1);
				int newRow = butRow;
				int newCol = butCol;
				switch (currentIn) {
					case "U":
						newRow--;
						break;
					case "D":
						newRow++;
						break;
					case "L":
						newCol--;
						break;
					case "R":
						newCol++;
						break;
				}
				if (!(newRow < 0 || newRow >= KEYPAD2.length || newCol < 0 || newCol >= KEYPAD2[0].length)) {
					if (!(KEYPAD2[newRow][newCol] == "")) {
						butRow = newRow;
						butCol = newCol;
					}
				}
			}
			passcode = passcode + KEYPAD2[butRow][butCol]; 
		}
		return passcode;
	}
	
}
