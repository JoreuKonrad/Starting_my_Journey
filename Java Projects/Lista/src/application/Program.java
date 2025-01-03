package application;

import java.util.ArrayList;
import java.util.List;

public class Program {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		List<String> list = new ArrayList<>();
		
		list.add("Maria");
		list.add("Tobby");
		list.add("Marcos");
		list.add("Bob");
		list.add("Ana");
		
		list.add(2,"Smeagol"); //Adicionar nome na segunda posição
		
		System.out.println("----------");
		for(String nome : list) {
			System.out.println(nome);
		}
		
		System.out.println("----------"); // Removendo nomes que começam com B
		list.removeIf(x -> x.charAt(0) == 'B');
		for(String nome : list) {
			System.out.println(nome);
		}
		
		System.out.println("----------");
		System.out.println("Index de Tobby: " + list.indexOf("Tobby")); // Mostrando o index de Tobby
		
		System.out.println("----------");
		String nome = list.stream().filter(x -> x.charAt(0) == 'T').findFirst().orElse(null);
		System.out.println("Priemiro nome com T: " + nome);
				
	}

}
