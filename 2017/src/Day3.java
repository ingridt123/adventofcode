import java.util.Arrays;

public class Day3 {

	public static void main(String[] args) {
	
		int input = 368078;
//		int input = 8;
		int curPos = input;
		int steps = 0;
		
		// get next largest perfect square (odd number) for dimensions
		double sqrt = Math.sqrt(input);
		int sqrtInt = (int) Math.ceil(sqrt);
		if (sqrtInt % 2 == 0) {
			sqrtInt++;
		}
		
		int[][] spiral = new int[sqrtInt][sqrtInt];
		int midpoint = (int) sqrtInt / 2;
		
		int value = 1;
		int x = midpoint;
		int y = midpoint;
		spiral[y][x] = value;
		value++;
		
		while (value <= (sqrtInt * sqrtInt)) {
			// right
			x++;
			spiral[y][x] = value;
			value++;
			
			// up
			while (spiral[y][x-1] != 0) {
				y--;
				spiral[y][x] = value;
				value++;
			}
			
			// left
			while (spiral[y+1][x] != 0) {
				x--;
				spiral[y][x] = value;
				value++;
			}
			
			// down
			while (spiral[y][x+1] != 0) {
				y++;
				spiral[y][x] = value;
				value++;
			}
			
			// right
			while (spiral[y-1][x] != 0 && value <= (sqrtInt * sqrtInt)) {
				x++;
				if (y == 607 || x == 607) {
					continue;
				}
				spiral[y][x] = value;
				value++;
			}
		}
		
		while (curPos != 1) {
			
			
			
			steps++;
			
		}
		
		System.out.println(steps);
		
	}
	
}
