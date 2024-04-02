package Cofre;

public class Dolar extends Moeda{
	public Dolar() {
		
	}
	
	public double somarDolar(double valor) {		
		return this.valor += valor;
	}
	
	public double removeDolar(double valor) {		
		return this.valor -= valor;
	}
	
	public void info() {		
		System.out.println("Valor total em Dolar: " + this.valor);
	}
	
	public double converter() {
		return valor * 4.88; 
	}
	
}
