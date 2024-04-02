package empresa;

public class LivroDigitalEx extends Livro {
	public String linkDownload;
	public int tamanhoMB;
	
	public LivroDigitalEx(String livro,String autor) {
		super(livro,autor);
	}
	
	public float imposto() {
		return 0.2f * lucro() + 2;
	}
	
	public float tamanhoPorPagina() {
		return tamanhoMB / (float) paginas;
		
	}
	
}
