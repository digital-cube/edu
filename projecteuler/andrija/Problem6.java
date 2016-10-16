/*The sum of the squares of the first ten natural numbers is,
 * 12 + 22 + ... + 102 = 385
 * The square of the sum of the first ten natural numbers is,
 * (1 + 2 + ... + 10)2 = 552 = 3025
 * Hence the difference between the sum of the squares of the first ten natural numbers 
 * and the square of the sum is 3025 − 385 = 2640.
 * Find the difference between the sum of the squares of the first one hundred natural numbers 
 * and the square of the sum.*/

public class Problem6 {
	
	static int sum1;
	static int sum2;
	static int answer;
	
	public static void main(String[] args){
		
		for(int i=1; i<=100; i++){
			sum1 += i;
			sum2 += Math.pow(i, 2);
		}
		answer = (int)(Math.pow(sum1,2)-sum2);
		System.out.println("Answer: " + answer);
	}
}
