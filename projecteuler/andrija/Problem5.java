/*2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
 * What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?*/


public class Problem5 {


	public static void main(String[] args) {
		
		int broj = 2520;
		boolean uslov1 = true;
		int niz[] = {11,12,13,14,15,16,17,18,19,20};
		
		while(uslov1){
			
			boolean uslov2=true;
			for(int i=0; i<niz.length; i++){
				if(broj%niz[i]!=0) {
					uslov2=false;
					System.out.println("Proverava se broj: " + broj);
					break;
				}
			}
			if(uslov2){
				uslov1=false;
			} else {
				broj+=10;
			}
		}
		System.out.println("_________________");
		System.out.println("Answer: " + broj);   //Na odgovor je neophodno sacekati proracun koji je kod mene trajao oko 10 min
		System.out.println("_________________");
		
	}

}
