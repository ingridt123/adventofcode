import java.math.BigInteger;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;
import java.util.HashMap;

public class Day5 {

	private String doorID;
	private int index;
	
	public static void main (String[] args) {
		Day5 five = new Day5();
//		System.out.println(five.genPassword());
		System.out.println(five.genPassword2());
	}
	
	public Day5() {
		doorID = "reyedfim";
//		doorID = "abc";
		index = 0;
	}
	
	/**
	 * task 1 - get the password from MD5 hashes
	 * @return password
	 */
	public String genPassword() {
		String password = "";
		index = 0; 
		while (password.length() < 8) {
			String newDoorID = doorID + index;
			String digit = "";
			
			try {
				MessageDigest md = MessageDigest.getInstance("MD5");
				md.update(newDoorID.getBytes(), 0, newDoorID.length());
				String hashString = new BigInteger(1, md.digest()).toString(16);
				System.out.println(index + "    " + hashString);
				if (hashString.length() == 27) {
					digit = hashString.substring(0,1);
				}
			}
			catch (NoSuchAlgorithmException e) {
				e.printStackTrace();
			}
			
			password += digit;
			index++;
		}
		return password;
	}
	
	/**
	 * task 2 - 
	 */
	public String genPassword2() {
		String password = "";
		index = 0;
		HashMap<Integer, String> record = new HashMap<Integer, String>();
		while (record.size() < 8) {
			String newDoorID = doorID + index;
			String digits = "";
			String hashString = "";
			
			try {
				MessageDigest md = MessageDigest.getInstance("MD5");
				md.update(newDoorID.getBytes(), 0, newDoorID.length());
				hashString = new BigInteger(1, md.digest()).toString(16);
				if (hashString.length() == 27) {
					digits = hashString.substring(0,2);
				}
				else if (hashString.length() == 26) {
					digits = "0" + hashString.substring(0,1);
				}
				else if (hashString.length() < 26) {
					digits = "00";
				}
			}
			catch (NoSuchAlgorithmException e) {
				e.printStackTrace();
			}
			
			if (digits.length() == 2) {
				int position = Integer.parseInt(digits.substring(0,1), 16);
				if (position < 8 && !record.containsKey(position)) {
					System.out.println(digits + " - " + hashString);
					record.put(position, digits.substring(1));
				}
			}
			index++;
//			System.out.println(record);
		}
		
		for (int i = 0; i < 8; i++) {
			password += record.get(i);
		}
		
		return password;
	}
}
