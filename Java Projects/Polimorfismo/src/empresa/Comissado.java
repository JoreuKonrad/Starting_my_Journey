package empresa;

public class Comissado extends Funcionario {
	float vendas;
	float comissao;
	
	public Comissado(String nome, float vendas, float comissao) {
		super(nome);
		this.vendas = vendas;
		this.comissao = comissao;
		
	}
	
	public float pagamento() {
		return vendas * comissao;
		
	}
	
}
