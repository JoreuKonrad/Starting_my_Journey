package Principal;

import java.util.HashMap;
import java.util.Map;

// Classe para representar o usuário
class Usuario {
    private String nome;
    private double saldo;

    public Usuario(String nome) {
        this.nome = nome;
        this.saldo = 0.0;
    }

    public String getNome() {
        return nome;
    }

    public double getSaldo() {
        return saldo;
    }

    public void depositar(double valor) {
        saldo += valor;
        System.out.println("Depósito de " + valor + " realizado para o usuário " + nome);
    }

    public void retirar(double valor) {
        if (saldo >= valor) {
            saldo -= valor;
            System.out.println("Retirada de " + valor + " realizada para o usuário " + nome);
        } else {
            System.out.println("Saldo insuficiente para realizar a retirada.");
        }
    }
}