package empresa;

public class Aluno {
	String Nome;
	int Matricula;
	String cpf;
	static int valorEstatico = 5;
	int valorVariavel = 2;
	
	public void info() {
		System.out.println("Nome: " + Nome);
		System.out.println("Matricula: " + Matricula);
		System.out.println("CPF: " + cpf);
		System.out.println("vEst: " + valorEstatico);
		System.out.println("vVar: " + valorVariavel+"\n");		
		
	}
	
	public Aluno(int pMatricula,String pNome,String pCpf){
		this.Matricula = pMatricula;
		this.Nome = pNome;
		this.cpf = pCpf;
		
	}
	
	Aluno(){
		
	}
	

	
}
