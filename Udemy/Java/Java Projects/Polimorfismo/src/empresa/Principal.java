package empresa;

public class Principal {

	public static void main(String[] args) {
		Funcionario funcionarios[] = {new Assalariado("Mario",4000),
									new Horista("Luigi",100,50.3f),
									new Comissado("Yoshi",50000,0.5f)};
		float SomaPagamentos = 0;
		Funcionario f;
		for(int i=0; i<funcionarios.length; i++) {
			f = funcionarios[i];
			System.out.println(f.nome + " Salario: " + f.pagamento());
			
			SomaPagamentos += f.pagamento();
		}
		
		System.out.println("Pagamento Total: " + SomaPagamentos);

	}

}
