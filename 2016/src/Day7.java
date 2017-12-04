import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.Scanner;
import java.util.Stack;

public class Day7 {

	private ArrayList<String> input;
	
	public static void main (String[] args) {
		File file = new File("day7.txt");
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
	}
	
	/**
	 * constructor
	 * @param in	ArrayList of input
	 */
	public Day7 (ArrayList<String> in) {
		input = in;
	}
	
	/**
	 * check IPs if they support TLS
	 * @return number of IPs that support TLS
	 */
	public int supportTLS() {
		int count = 0;
		for (String ip : input) {
			int sqIndex1 = ip.indexOf("[");
			int sqIndex2 = ip.indexOf("]");
			String square = ip.substring(sqIndex1, sqIndex2+1);
			ip = ip.substring(0,sqIndex1) + " " + ip.substring(sqIndex2+1);
			
			// check for palindromes
			// (none in square + yes outside -- if character is space then reset checks for after)
//			Stack<String> letters = ne
			}
//		}
		
		return count;
	}
	
}
