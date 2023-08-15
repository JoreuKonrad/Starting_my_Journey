package empresa;

public class Princiapl {

	public static void main(String[] args) {
		Livro l1 = new Livro("TI1","Smigol");
		
		LivroDigitalEx l2 = new LivroDigitalEx("TI2","Pokemon");
		
		
		l1.imprimirTitulo();
		l2.imprimirTitulo();
		
		System.out.println(l1.titulo);

		
	}

}
