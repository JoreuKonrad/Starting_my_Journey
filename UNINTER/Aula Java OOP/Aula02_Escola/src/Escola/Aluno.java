package Escola;

public class Aluno {
	String nome;
	String cpf;
	int matricula;
	
	Aluno(String nome, int matricula,String cpf){
		this.nome = nome;
		this.matricula = matricula;
		this.cpf = cpf;
				
	}
	
	Aluno(String nome){
		this.nome = nome;
		
	}
	
	Aluno(){
		System.out.println("Construtor sem parametro");
	}
	

}
