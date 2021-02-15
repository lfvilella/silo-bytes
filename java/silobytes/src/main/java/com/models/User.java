package com.models;

/**
 *
 * @author felipe
 */
import java.io.Serializable;

public class User implements Serializable {
    String login;
    String nome;
    String senha; 

    public User() {
        this.login = "";
        this.nome = "";
        this.senha = "";
    }

    public User(String login, String nome, String senha) {
        this.login = login; 
        this.nome = nome;
        this.senha = senha; 
    }

    public String getLogin() {
        return login;
    }

    public void setLogin(String login) {
        this.login = login;
    }

    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public String getSenha() {
        return senha;
    }

    public void setSenha(String senha) {
        this.senha = senha;
    }

    
}