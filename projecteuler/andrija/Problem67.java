import java.awt.List;
import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.Scanner;

public class Problem67 {
	public static void main(String[] args) throws FileNotFoundException {
		
		ArrayList<Integer> niz = new ArrayList<>();
		String token = "";
		Scanner sc = new Scanner(new File("C://p067_triangle.txt"));
		while(sc.hasNext()){
			token = sc.next();
			niz.add(Integer.parseInt(token));
		}
		
		int[][] p = new int[100][100];
		
		int z =0;
		for(int i=0; i<100; i++){
			for(int j=0; j<=i; j++){
				p[i][j]= niz.get(z);
				System.out.println("Niz: " + niz.get(z) + " - " + " P ["+i+"]["+j+"]");
				z++;
			}
		}
		
		for(int i=0; i<100; i++){
			for(int j=0; j<=i; j++){
				
				if(j==0 && i==0){
					System.out.println(" P ["+i+"]["+j+"]" + p[i][j]);
				}
				else if(j==0 && i>0) {
					p[i][j]+=p[i-1][j];
				} else {
					if(p[i-1][j-1]>p[i-1][j]){
						p[i][j]+=p[i-1][j-1];
					} else {
						p[i][j]+=p[i-1][j];
					}
				}
				System.out.println(" P ["+i+"]["+j+"]" + p[i][j]);
				
			}
		}
		
		int answer = 0;
		for(int j=0; j<100; j++){
			if(p[99][j]>answer)	answer = p[99][j];
		}
		
		System.out.println("Answer: " + answer);
		
		
	
		
	
		

	}


}
