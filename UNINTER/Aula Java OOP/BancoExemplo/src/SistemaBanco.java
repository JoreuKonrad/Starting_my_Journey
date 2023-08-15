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

// Classe principal do sistema de banco
public class SistemaBanco {
    private Map<String, Usuario> usuarios;

    public SistemaBanco() {
        usuarios = new HashMap<>();
    }

    public void criarUsuario(String nome) {
        Usuario usuario = new Usuario(nome);
        usuarios.put(nome, usuario);
        System.out.println("Usuário " + nome + " criado com sucesso.");
    }

    public void depositar(String nomeUsuario, double valor) {
        Usuario usuario = usuarios.get(nomeUsuario);
        if (usuario != null) {
            usuario.depositar(valor);
        } else {
            System.out.println("Usuário " + nomeUsuario + " não encontrado.");
        }
    }

    public void retirar(String nomeUsuario, double valor) {
        Usuario usuario = usuarios.get(nomeUsuario);
        if (usuario != null) {
            usuario.retirar(valor);
        } else {
            System.out.println("Usuário " + nomeUsuario + " não encontrado.");
        }
    }

    public static void main(String[] args) {
        SistemaBanco sistema = new SistemaBanco();
        
        // Exemplo de uso do sistema
        sistema.criarUsuario("João");
        sistema.depositar("João", 100.0);
        sistema.retirar("João", 50.0);
    }
}
