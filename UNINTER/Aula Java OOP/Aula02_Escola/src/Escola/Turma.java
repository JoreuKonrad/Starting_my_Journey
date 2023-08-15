package Escola;
import java.util.ArrayList;

public class Turma {	

	ArrayList<Aluno> listaAlunos = new ArrayList();
	Professor orientador;
	String sala;
	
	void adicionarAluno(Aluno aluno) {
		listaAlunos.add(aluno);
	}
}


