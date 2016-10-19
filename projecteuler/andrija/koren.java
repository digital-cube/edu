package sqrt;

public class koren {
	
	
	
	
	static public double sqrt(double broj, double p){
		double min = 0;
		double max = broj;
		double b=0;
		while(max-min>p){
			b = (max+min)/2;
			if(b*b>broj) {
				max = b;
			} else {
				min = b;
			}
		}

		return b;
	}
	
	public static void main(String[] args){
		
		System.out.println("koren je: " + sqrt(25, 0.001));
		
	}

}
