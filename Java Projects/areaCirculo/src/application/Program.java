package application;

import java.util.Locale;
import java.util.Scanner;

import util.Calculator;

public class Program {


	public static void main(String[] args) {
		// TODO Auto-generated method stub

		Locale.setDefault(Locale.US);
		Scanner sc = new Scanner(System.in);
		
		System.out.println("Insira o Raio: ");
		double radius = sc.nextDouble();
		
		double c = Calculator.circumference(radius); //apenas chamando a classe e o metodo estatico
		
		double v = Calculator.volume(radius);		
		
		System.out.printf("Circuferencia:  %.2f%n",c);
		System.out.printf("Volume:  %.2f%n",v);
		System.out.printf("Valor PI:  %.2f%n",Calculator.PI);
				
		sc.close();		
	}

		
}