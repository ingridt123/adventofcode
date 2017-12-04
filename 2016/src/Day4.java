import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

public class Day4 {

	private ArrayList<String> input;
	
	public static void main (String[] args) {
		
		File file = new File("day4.txt");
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
		
		Day4 four = new Day4(input);
		System.out.println(four.checkID());
		System.out.println(four.decipher());
	}
	
	/**
	 * constructor
	 * @param in	ArrayList<String> input from file
	 * @param c		number of IDs to be checked
	 */
	public Day4(ArrayList<String> in) {
		input = in;
	}
	
	/**
	 * task 1 -- check if IDs are real
	 * @return	sum of sector IDs of real rooms
	 */
	public int checkID() {
		int sum = 0;
		
		// split id into different parts
		for (String id : input) {
			String[] dashSplit = id.split("-");
			String end = dashSplit[dashSplit.length-1];
			String dash = "";
			for (int i = 0; i < dashSplit.length-1; i++) {
				dash += dashSplit[i];
			}
			int sectorID = Integer.parseInt(end.substring(0, 3));
			String checkSum = end.substring(4, end.length()-1);
			
			// count number of letters in each
			HashMap<Character, Integer> occurrences = new HashMap<Character, Integer>();
			ArrayList<Integer> max = new ArrayList<Integer>();
			for (int let = 0; let < dash.length(); let++) {
				char current = dash.charAt(let);
				if (!occurrences.containsKey(current)) {
					int countLet = 0;
					for (int check = 0; check < dash.length(); check++) {
						if (dash.charAt(check) == current) {
							countLet++;
						}
					}
					occurrences.put(current, countLet);
					max.add(countLet);
				}
			}
			
			// sort and then check with checksum
			Collections.sort(max, Collections.reverseOrder());
			
			char[] maxChar = new char[5];
			int maxIndex = 0;
			for (int index = 0; index < 5; index++) {
				int maxNum = max.get(index);
				ArrayList<Character> chars = new ArrayList<Character>();
				for (Map.Entry<Character, Integer> entry : occurrences.entrySet()) {
					if (entry.getValue() == maxNum) {
						chars.add(entry.getKey());
					}
				}
				Collections.sort(chars);
				for (char current : chars) {
					if (maxIndex >= 5) {
						break;
					}
					maxChar[maxIndex] = current;
					occurrences.remove(current);
					maxIndex++;
				}
			}
			String check = new String(maxChar);
			
			// if same as checksum, add sectorID to sum
			if (check.equals(checkSum)) {
				sum += sectorID;
			}
		}
		
		return sum;
	}
	
	/**
	 * task 2 - decipher IDs
	 */
	public int decipher() {
		int sectorID = 0;
		
		for (String id : input) {
			// split id into different parts
			String[] dashSplit = id.split("-");
			String end = dashSplit[dashSplit.length-1];
			String dash = "";
			for (int i = 0; i < dashSplit.length-1; i++) {
				dash += dashSplit[i];
			}
			sectorID = Integer.parseInt(end.substring(0, 3));
			String checkSum = end.substring(4, end.length()-1);
		
			// shift letters
			int shift = sectorID % 26;
			String deciphered = "";
			for (int i = 0; i < dash.length(); i++) {
				char character = dash.charAt(i);
				int ascii = character;
				ascii += shift;
				if (ascii > 122) {
					ascii = ascii - 123 + 97;
				}
				character = (char)(ascii);
				deciphered += character;
			}
			
			// find "North Pole objects"
			if (deciphered.equals("northpoleobjectstorage")) {
				break;
			}
		}
		
		return sectorID;
	}
}
