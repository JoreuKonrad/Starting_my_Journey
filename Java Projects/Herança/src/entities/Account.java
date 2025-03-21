package entities;

public class Account {
	
	private Integer number;
	private String holder;
	protected double balance;
	
	public Account() {
		
	}
	
	public Account(Integer number, String holder, double balance) {
		this.number = number;
		this.holder = holder;
		this.balance = balance;
	}


	public Integer getNumber() {
		return number;
	}


	public void setNumber(Integer number) {
		this.number = number;
	}


	public String getHolder() {
		return holder;
	}


	public void setHolder(String holder) {
		this.holder = holder;
	}


	public double getBalance() {
		return balance;
	}


	/* Setter removido do auto genereate. Motivo: Regra de negocio
	 * public void setBalance(double balance) {
	 
		this.balance = balance;
	}
	*/
	
	public void withdraw(double amount) {
		balance -= amount;
	}
	
	public void deposit(double amount) {
		balance += amount;
	}
	
	
}
