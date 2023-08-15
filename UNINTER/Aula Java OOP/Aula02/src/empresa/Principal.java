package empresa;

import empresa.Aluno;
import Outro.Teste; 

public class Principal {public static void main(String[] args){
			Aluno mario = new Aluno();
			mario.cpf = "111.111.111-11";
			mario.Nome = "Super Mario"; 
			mario.Matricula = 1001;
			//mario.valorEstatico = 6;
			mario.valorVariavel = 1;
			
			Aluno luigi = new Aluno();
			luigi.cpf = "222.222.222-22";
			luigi.Nome = "Super Luigi";
			luigi.Matricula = 1002;
			//luigi.valorEstatico = 0;
			luigi.valorVariavel = 2;
			
			Aluno yoshi = new Aluno();
			yoshi.cpf = "333.333.333-33";
			yoshi.Nome = "Super Yoshi";
			yoshi.Matricula = 1003;
			//yoshi.valorEstatico = 22;
			yoshi.valorVariavel = 3;
			
			
			Aluno antigo;
			if (mario.Matricula < luigi.Matricula) {
				antigo = mario;
			}
			else {
				antigo = luigi;
			}
			
			//System.out.println("Aluno mais antigo: "+antigo.Nome);			
			//System.out.println(yoshi.Nome + ": " + yoshi.Matricula);
			
			mario.info();			
			luigi.info();
			yoshi.info();
			
			Teste.teste();	
			
			
	}
}