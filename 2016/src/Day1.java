import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.HashMap;
import java.util.Scanner;

public class Day1 {

	private static final String[] MAP = {"north", "east", "south", "west"};
	private String direction;
	private HashMap<String, Integer> steps;
	private String[] directions;
	
	public static void main (String[] args) {
		String[] directions;
		String text = "";
		
		File file = new File("day1.txt");
		try {
			Scanner scan = new Scanner(file);
			text = scan.nextLine();
			scan.close();
		}
		catch (FileNotFoundException e) {
			e.printStackTrace();
		}
		
		directions = text.split(", ");
		Day1 one = new Day1(directions);
		
//		System.out.println(one.calBlocks());
		System.out.println(one.firstRepeat());
	}
	
	public Day1(String[] d) {
		direction = "north";
		steps = new HashMap<String, Integer>();
		steps.put("vertical", 0);
		steps.put("horizontal", 0);
		directions = d;
	}
	
	public int iteration(int directionIndex, int i) {
		// check turn direction (left/right)
		if (directions[i].charAt(0) == 'R') {		// turn right
			directionIndex++;
		}
		else {										// turn left
			directionIndex--;
		}
//		System.out.print(directions[i] + "  ");
		
		// check and correct index if necessary
		if (directionIndex < 0) {
			directionIndex = 3;
		}
		else if (directionIndex >= MAP.length) {
			directionIndex = 0;
		}
//		System.out.print(directionIndex + "  ");
		
		// change direction
		direction = MAP[directionIndex];
//		System.out.print(direction + "  ");
		
		// add to direction
		int numSteps = Integer.parseInt(directions[i].substring(1));
		String key = "";
		switch(direction) {
			case "north": 
				key = "vertical";
				break;
			case "south":
				key = "vertical";
				numSteps *= -1;
				break;
			case "east":
				key = "horizontal";
				break;
			case "west":
				key = "horizontal";
				numSteps *= -1;
				break;
		}
		steps.replace(key, steps.get(key) + numSteps);
//		System.out.println(steps.values());
		
		return directionIndex;
	}
	
	/**
	 * Calculates number of blocks from starting position
	 * @return number of blocks from start
	 */
	public int calBlocks() {
		int directionIndex = 0;
		for (int i = 0; i < directions.length; i++) {
			directionIndex = iteration(directionIndex, i);
		}
		
		return Math.abs(steps.get("horizontal")) + Math.abs(steps.get("vertical"));
	}
	
	/**
	 * Determines first location visited twice (could be along path not necessarily an end point)
	 * @return number of blocks from start
	 */
	public int firstRepeat() {
		// saves all points visited
		ArrayList<ArrayList<Integer>> points = new ArrayList<ArrayList<Integer>>();
		ArrayList<Integer> first = new ArrayList<Integer>();
		first.add(0);
		first.add(0);
		points.add(first);
		
		// iterate through directions
		int directionIndex = 0;
		for (int i = 0; i < directions.length; i++) {
			int origX = steps.get("horizontal");
			int origY = steps.get("vertical");
			directionIndex = iteration(directionIndex, i);
			int currX = steps.get("horizontal");
			int currY = steps.get("vertical");
			
			// starting and ending value of adding of points
//			int changeX = 0;
//			int changeY = 0;
			if (origX > currX) {
				origX -= 1;
//				changeX = -1;
			}
			else if (origX < currX) {
				origX += 1;
//				changeX = 1;
			}
			if (origY > currY) {
				origY -= 1;
//				changeY = -1;
			}
 			else if (origY < currY) {
				origY += 1;
//				changeY = 1;
			}
			
			System.out.println("original: " + origX + ", " + origY);
			System.out.println("current: " + currX + ", " + currY);
			
			if (origX >= currX) {
				for (int x = origX; x >= currX; x--) {
					if (origY >= currY) {
						for (int y = origY; y >= currY; y--) {
							ArrayList<Integer> newPoint = new ArrayList<Integer>();
							newPoint.add(x);
							newPoint.add(y);
							if (points.contains(newPoint)) {
								return Math.abs(x) + Math.abs(y);
							}
							points.add(newPoint);
							System.out.println(newPoint.get(0) + " " + newPoint.get(1));
						}
					}
					else {
						for (int y = origY; y <= currY; y++) {
							ArrayList<Integer> newPoint = new ArrayList<Integer>();
							newPoint.add(x);
							newPoint.add(y);
							if (points.contains(newPoint)) {
								return Math.abs(x) + Math.abs(y);
							}
							points.add(newPoint);
							System.out.println(newPoint.get(0) + " " + newPoint.get(1));
						}
					}
				}
			}
			else {
				for (int x = origX; x <= currX; x++) {	
					if (origY > currY) {
						for (int y = origY; y >= currY; y--) {
							ArrayList<Integer> newPoint = new ArrayList<Integer>();
							newPoint.add(x);
							newPoint.add(y);
							if (points.contains(newPoint)) {
								return Math.abs(x) + Math.abs(y);
							}
							points.add(newPoint);
							System.out.println(newPoint.get(0) + " " + newPoint.get(1));
						}
					}
					else {
						for (int y = origY; y <= currY; y++) {
							ArrayList<Integer> newPoint = new ArrayList<Integer>();
							newPoint.add(x);
							newPoint.add(y);
							if (points.contains(newPoint)) {
								return Math.abs(x) + Math.abs(y);
							}
							points.add(newPoint);
							System.out.println(newPoint.get(0) + " " + newPoint.get(1));
						}
					}
				}
			}
		}
		
		return -1;
	}
	
}
