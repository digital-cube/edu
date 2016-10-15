import java.util.ArrayList;
import java.util.Collection;
import java.util.Collections;

/*A palindromic number reads the same both ways. 
 * The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
 * Find the largest palindrome made from the product of two 3-digit numbers.*/


public class Problem4 {
	
	static int answer;
	static Collection<Integer> list = new ArrayList<>();
	
	public static void main(String[] args) {	
		for(int i=999; i>99; i--){
			for(int j=999; j>99; j--){
				answer = i*j;
				String broj = String.valueOf(answer);
				boolean uslov = true;
				for(int z=0; z<=(int)broj.length()/2; z++){
					if( !(broj.charAt(z)==(broj.charAt(broj.length()-1-z))) ){
						uslov =false;
					}
				}
				if(uslov){
					list.add(answer);
				}
			}
		} 
		System.out.println("Aswer: " + Collections.max(list));
	}
}
