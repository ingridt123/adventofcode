import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.Collection;
import java.util.Collections;
import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

public class Day6 {

	private String[][] input;
	private int rows;
	private int columns;
	
	public static void main(String[] args) {
		File file = new File("day6.txt");
		ArrayList<String> initialInput = new ArrayList<String>();
		
		try {
			Scanner scan = new Scanner(file);
			while (scan.hasNext()) {
				initialInput.add(scan.nextLine());
			}
			scan.close();
		}
		catch (FileNotFoundException e) {
			e.printStackTrace();
		}
		
		Day6 six = new Day6(initialInput);
		System.out.println(six.decryptMessageLeast());
	}
	
	/**
	 * constructor
	 * @param initialInput ArrayList of input
	 */
	public Day6(ArrayList<String> initialInput) {
		rows = initialInput.size();
		columns = initialInput.get(0).length();
		input = new String[rows][columns];
		
		for (int i = 0; i < rows; i++) {
			String in = initialInput.get(i);
			for (int j = 0; j < columns; j++) {
				input[i][j] = in.substring(j, j+1);
			}
		}
	}
	
	/**
	 * task 1 - find most repeated word
	 */
	public String decryptMessage() {
		String message = "";
		for (int j = 0; j < columns; j++) {
			HashMap<String, Integer> count = new HashMap<String, Integer>();
			for (int i = 0; i < rows; i++) {
				String current = input[i][j];
				if (count.containsKey(current)) {
					int num = count.get(current);
					count.replace(current, num+1);
				}
				else {
					count.put(current, 1);
				}
			}
			Collection<Integer> nums = count.values();
			int max = Collections.max(nums);
			
			for (Map.Entry<String, Integer> entry : count.entrySet()) {
				if (entry.getValue() == max) {
					message += entry.getKey();
					break;
				}
			}
		}
		return message;
	}
	
	/**
	 * task 2 - find least repeated word
	 */
	public String decryptMessageLeast() {
		String message = "";
		for (int j = 0; j < columns; j++) {
			HashMap<String, Integer> count = new HashMap<String, Integer>();
			for (int i = 0; i < rows; i++) {
				String current = input[i][j];
				if (count.containsKey(current)) {
					int num = count.get(current);
					count.replace(current, num+1);
				}
				else {
					count.put(current, 1);
				}
			}
			Collection<Integer> nums = count.values();
			int min = Collections.min(nums);
			
			for (Map.Entry<String, Integer> entry : count.entrySet()) {
				if (entry.getValue() == min) {
					message += entry.getKey();
					break;
				}
			}
		}
		return message;
	}
	
}
