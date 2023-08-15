package empresa;

import java.util.Scanner;

public class Principal {

	public static void main(String[] args) {
		// TODO Auto-generated method stub		
		String nome = "Joreu";	
		int idade = 22;
		
		Scanner teclado = new Scanner(System.in);
		
		
		
		System.out.println("** Teste **");
		System.out.println(nome);
		System.out.println(idade);
		
		if (idade== 22) {
			System.out.println("Se fudeu");
		}
		
		for(int i = 0;i<5;i++) {
			System.out.println(i);
		}
		
		//Criando uma lista		
		int listanumerica[] = {11,234,34};
		
		System.out.println(listanumerica[2]);
		
		int numeros[] = new int[200]; // Cria uma lista com 200 posições, mas sem valor
		

	}

}