package Cofre;

public class Euro extends Moeda{
	public Euro() {
		
	}
	
	public double somarEuro(double valor) {		
		return this.valor += valor;
	}
	
	public double removeEuro(double valor) {		
		return this.valor -= valor;
	}
	
	public void info() {		
		System.out.println("Valor total em Euro: " + this.valor + "\n");
	}
	
	public double converter() {
		return valor * 5.36; 
	}
	
}
