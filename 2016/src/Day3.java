import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Scanner;

public class Day3 {
	
	private int count;
	private ArrayList<String> inputString;
	
	/**
	 * main method
	 */
	public static void main (String[] args) {
		ArrayList<String> input = new ArrayList<String>();
		int c = 0;
		
		try {
			File file = new File("day3.txt");
			Scanner scan = new Scanner(file);
			while (scan.hasNext()) {
				input.add(scan.nextLine().trim());
				c++;
			}
		}
		catch (FileNotFoundException e) {
			e.printStackTrace();
		}
		
		Day3 three = new Day3(c, input);
		System.out.println(three.validTrianglesRows());
		System.out.println(three.validTrianglesCols());
	}

	/**
	 * constructor
	 * @param c number of rows
	 * @param input ArrayList of each row
	 */
	public Day3 (int c, ArrayList<String> input) {
		count = c;
		inputString = input;
	}
	
	/**
	 * return number of valid triangles (in rows)
	 */
	public int validTrianglesRows() {
		int[][] sides = createTriangleArray();
		
		return checkTriangles(sides);
	}
	
	/**
	 * return number of valid triangles (in columns)
	 */
	public int validTrianglesCols() {
		int[][] sidesRow = createTriangleArray();
		int[][] sidesCol = new int[count][3];
		
		int arrayRow = 0;
		for (int col = 0; col < 3; col++) {
			int row = 0;
			while (row < count) {
				int[] inputSplit = new int[3];
				int index = 0;
				for (int go = 0; go < 3; go++) {
					inputSplit[index] = sidesRow[row][col];
					index++;
					row++;
				}
				System.out.println(Arrays.toString(inputSplit));
				sidesCol[arrayRow] = inputSplit;
				arrayRow++;
			}
		}
		return checkTriangles(sidesCol);
	}
	
	/**
	 * create array of triangle sides in each row
	 */
	public int[][] createTriangleArray() {
		int[][] sides = new int[count][3];
		for (String sInput : inputString) {
			String[] inputSplit = sInput.split("\\s+");
			int[] inputInt = new int[3];
			int iIndex = 0;
			for (String iInput : inputSplit) {
				int i = Integer.parseInt(iInput);
				inputInt[iIndex] = i;
				iIndex++;
			}
			int index = inputString.indexOf(sInput);
			sides[index] = inputInt;
		}
		return sides;
	}
	
	/**
	 * check how many triangles are valid
	 * @param sides	2D array of triangle sides
	 * @return number of valid triangles
	 */
	public int checkTriangles(int[][] sides) {
		int triangles = 0;
		for (int tri = 0; tri < count; tri++) {
			int side1 = sides[tri][0];
			int side2 = sides[tri][1];
			int side3 = sides[tri][2];
			if (side1 + side2 > side3 && side1 + side3 > side2 && side2 + side3 > side1) {
				triangles++;
			}
		}
		return triangles;
	}
	
}
