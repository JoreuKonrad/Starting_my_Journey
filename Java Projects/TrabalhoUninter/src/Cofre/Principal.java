/*
 * Trabalho - Programação Orientado a Objetos
 * Feito por: Joréu V. Konrad
 * RU: 3630044
 * 
 */



package Cofre;
import java.util.InputMismatchException;
import java.util.Scanner;

public class Principal {
	public static Double sysInputDouble() {
		Scanner scanner = new Scanner(System.in);
		try {
			Double s1 = scanner.nextDouble();
			
			return s1;
							
		} catch(InputMismatchException e){
			// Sistema caso usuario digite 
			// qualquer valor diferente de um numero
			scanner.nextLine();	
			return 0.0;
		}
	}
	
	public static int sysInputInt() {
		Scanner scanner = new Scanner(System.in);
		try {
			int s1 = scanner.nextInt();
			
			return s1;
							
		} catch(InputMismatchException e){
			// Sistema caso usuario digite 
			// qualquer valor diferente de um numero
			scanner.nextLine();	
			return 0;
		}
	}
	
	
	public static void main(String[] args) {		
		Scanner scanner = new Scanner(System.in);
		Real r1 = new Real();
		Euro e1 = new Euro();
		Dolar d1 = new Dolar();
		
		
		
		
		int runn = 1; // Loop para execução do programa		
		do {
			System.out.println("\nESCOLHA UMA OPCAO:");
			System.out.println("1- Adicionar Moeda;");
			System.out.println("2- Remover Moeda;");
			System.out.println("3- Listar Moedas;");
			System.out.println("4- Calcular Total em Real;");
			System.out.println("5- Sair;");
		

			
			int resp = sysInputInt();
			
			// Add moedas
			if(resp == 1) {
				System.out.println("Selecione em qual moeda deseja DEPOSITAR:");			
				System.out.println("1- Real;");			
				System.out.println("2- Dolar;");			
				System.out.println("3- Euro");			
				
				int resp2 = sysInputInt();
				
				// Real
				if(resp2 == 1) {
					System.out.println("(Real) Digite a quantidade:");			
					
					double vDepositado = sysInputDouble();
					r1.somarReal(vDepositado);				
					
				}
				// Dolar
				else if(resp2 == 2) {
					System.out.println("(Dolar) Digite a quantidade:");			
					
					double vDepositado = sysInputDouble();
					d1.somarDolar(vDepositado);				
					
				}
				// Euro
				else if(resp2 == 3) {
					System.out.println("(Euro) Digite a quantidade:");			
					
					double vDepositado = sysInputDouble();
					e1.somarEuro(vDepositado);			
					
				}
				
				
				
			}
			
			// Remove moedas
			else if(resp == 2) {
				System.out.println("Selecione em qual moeda deseja RETIRAR:");			
				System.out.println("1- Real;");			
				System.out.println("2- Dolar;");			
				System.out.println("3- Euro");			
				
				int resp2 = sysInputInt();
				
				if(resp2 == 1) {
					System.out.println("(Real) Digite a quantidade:");			
					
					double vRetirado = sysInputDouble();
					r1.removeReal(vRetirado);				
					
				}
				else if(resp2 == 2) {
					System.out.println("(Dolar) Digite a quantidade:");			
					
					double vRetirado = sysInputDouble();
					d1.removeDolar(vRetirado);				
					
				}
				else if(resp2 == 3) {
					System.out.println("(Euro) Digite a quantidade:");			
					
					double vRetirado = sysInputDouble();
					e1.removeEuro(vRetirado);			
					
				}				
				
				
			}
			// Listar moedas
			else if(resp == 3) {
				r1.info();
				d1.info();
				e1.info();
			}
			
			// Calcular total
			else if(resp == 4) {
				double vReal = r1.converter();
				double vDolar = d1.converter();
				double vEuro = e1.converter();
				
				System.out.println("Valor Total convertido em real:");
				System.out.println(vReal + vDolar + vEuro);
				

			}			
			
			// Sair do programa
			else if(resp == 5) {
				runn = 0;
				System.out.println("Programa Encerrado!");
			}
			
			// Indicando comando errado
			else{
				System.out.println("Commando incorreto!");
			}
			
		}while(runn == 1);
		

	}

}
