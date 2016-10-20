package sqrt;

public class koren {
	
	
	
	
	static public double sqrt(double broj, double p){
		double b=0;
		double min = 0;
		double max = broj;
		if(broj>1){
			while(max-min>p){
				b = (max+min)/2;
				if(b*b>broj) {
					max = b;
				} else {
					min = b;
				}
			}
		} else if(broj<1){
			min = broj;
			max = 1;
			while(max-min>p){
				b = (max+min)/2;
				if(b*b>broj) {
					max = b;
				} else {
					min = b;
				}
			}
		} else {
			b=1;
		}

		return b;
	}
	
	public static void main(String[] args){
		
		System.out.println("koren je: " + sqrt(25, 0.001));
		System.out.println("koren je: " + sqrt(0.81, 0.001));
		System.out.println("koren je: " + sqrt(1, 0.001));
		
	}

}
