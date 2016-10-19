import java.util.ArrayList;

/*The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ? */

public class Problem3 {
	
	public static long broj = 600851475143L ;
	static ArrayList<Integer> list = new ArrayList<Integer>();
	static int answer = 0;
	
	
	public static int prime(long g){
		int q = (int) Math.sqrt(g);
		for(int i=q; i>0; i--) {
				if(g%i==0) {
					list.add(i);
					System.out.println("Prime: " + i);
				}
		}
		
		if(list.size()==1) {answer=(int)g;} //u slucaju da je ulazni parametar g prost btoj
		
		for(int i=0; i<(list.size()-1); i++){
			boolean uslov = true;
			for(int j=i+1; j<(list.size()-2); j++){
				if(list.get(i)%list.get(j)==0){
					uslov = false;
				}
			}
			if(uslov){	
				answer = list.get(i);
				return answer;
			}
		}
		return 1;
	}
	
	public static void main(String[] args) {
		prime(broj);
		System.out.println("Answer: " + answer);
	}
}
