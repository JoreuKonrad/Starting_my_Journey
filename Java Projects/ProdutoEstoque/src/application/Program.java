package application;

import java.util.Locale;
import java.util.Scanner;

import entities.Product;

public class Program {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

		Locale.setDefault(Locale.US);
		Scanner sc = new Scanner(System.in);
		
		Product product = new Product();
		
		System.out.println("Insira dados do Produto:");
		System.out.println("Nome");
		product.name = sc.nextLine();
		
		System.out.println("Insira Quantidade");
		product.quantity = sc.nextInt();
		
		System.out.println("Insira Preço");
		product.price = sc.nextDouble();
		
		System.out.println("Produto info: " + product);	
		
		System.out.println("Insira a soma de Estoque:");
		int quantity = sc.nextInt();
		product.addProducts(quantity);		
		System.out.println("Produto info: " + product);	
		
		
		System.out.println("Insira a retirada de Estoque:");
		quantity = sc.nextInt();
		product.removeProducts(quantity);
		System.out.println("Produto info: " + product);	
		
		
		sc.close();
		
	}

}