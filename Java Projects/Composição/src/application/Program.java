package application;

import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.Locale;
import java.util.Scanner;

import entities.Department;
import entities.HourContract;
import entities.Worker;
import entities.enums.WorkerLevel;

public class Program {

	public static void main(String[] args) throws ParseException {
		
		Locale.setDefault(Locale.US);
		Scanner sc = new Scanner(System.in);
		SimpleDateFormat sdf = new SimpleDateFormat("dd/MM/yyyy");
		
		System.out.print("Informe o departamento: ");
		String departmentName = sc.nextLine();
		
		System.out.println("Informe os dados do funcionario.");
		System.out.print("Informe o nome do funcionario: ");
		String workerName = sc.nextLine();
		System.out.print("Informe o nivel do funcionario: ");
		String workerLevel = sc.nextLine();
		System.out.print("Informe a base salarial do funcionario: ");
		Double workerBaseSalary = sc.nextDouble();		
		Worker worker = new Worker(workerName,WorkerLevel.valueOf(workerLevel),workerBaseSalary,new Department(departmentName));
		
		System.out.println("Quantos contratos o funcionario possui? ");
		int numeroContratos = sc.nextInt();
		
		for(int contagemContrato = 0 ; contagemContrato < numeroContratos ; contagemContrato ++) {
			System.out.println("Informe o contrato " + contagemContrato);
			System.out.print("Data (DD/MM/AA): ");
			Date dataContrato = sdf.parse(sc.next());
			
			System.out.println("Valor por Hora: ");
			double valorHora = sc.nextDouble();
			
			System.out.println("Hora Trabalhado: ");
			int valorHoraTrabalhado = sc.nextInt();
			
			HourContract contract = new HourContract(dataContrato,valorHora,valorHoraTrabalhado);
			
			worker.addContract(contract);
		}
		
		System.out.println();
		System.out.println("Digite o mês/ano para conferir o salario: ");
		String monthAndYear = sc.next();
		int month = Integer.parseInt(monthAndYear.substring(0,2));
		int year = Integer.parseInt(monthAndYear.substring(3));
		System.out.println("Nome: " + worker.getName());
		System.out.println("Departamento: " + worker.getDepartment().getName());
		System.out.println("Salario recebido " + monthAndYear + ": " + String.format("%.2f",worker.income(year,month)));
		
			
		
		sc.close();

	}

}
