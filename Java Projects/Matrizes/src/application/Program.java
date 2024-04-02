package application;

import java.util.Scanner;

public class Program {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

		Scanner sc = new Scanner(System.in);
		
		int n = sc.nextInt();		
		int[][] mat = new int[n][n]; // Instanciando a matriz de ordem n
		
		for(int i = 0; i<mat.length; i++) {
			for(int j = 0 ; j<mat[i].length; j++) {
				mat[i][j] = sc.nextInt();
			}
		}
	
		
		sc.close();
	}

}
