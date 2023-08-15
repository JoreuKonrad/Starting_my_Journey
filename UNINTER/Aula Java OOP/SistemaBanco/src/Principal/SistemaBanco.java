package Principal;

import java.util.HashMap;
import java.util.Map;


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
        sistema.criarUsuario("Joao");
        sistema.depositar("Joao", 100.0);
        sistema.retirar("Joao", 50.0);
    }
}
