package Cofre;

public class Real extends Moeda{
	
	public Real() {		
	}
	
	public double somarReal(double valor) {		
		return this.valor += valor;
	}
	
	public double removeReal(double valor) {		
		return this.valor -= valor;
	}
	
	public void info() {		
		System.out.println("Valor total em Real: " + this.valor);
	}
	
	public double converter() {
		return valor * 1; 
	}
	
}
