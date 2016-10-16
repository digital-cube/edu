import java.util.ArrayList;

/*By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
 * What is the 10 001st prime number?*/


public class Problem7 {
	
	static ArrayList<Integer> list = new ArrayList<>();
	static int broj = 2;
	
	public static void main(String[] args){
			
		while(list.size()!=10001){
			boolean prostBroj=true;
			for(int i=0; i<list.size(); i++){
				if(broj%list.get(i)==0){
					prostBroj=false;
					break;
				}
			}
			if(prostBroj){ 
				list.add(broj);
				System.out.println(list.size()+". "+"Dodat prost broj: " + broj);
			}
			broj++;
		}
		System.out.println("_____________________________");
		System.out.println("Answer: " + list.get(10000));
		System.out.println("_____________________________");
	}
		
	

}
