package com.utils;

import java.io.EOFException;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.ObjectInputStream;
import java.io.ObjectOutputStream;
import java.util.ArrayList;

import com.models.User;

/**
 * @author felipe
 */
public class File {

    public static void inserir(User usuario) {
        try {
            ArrayList<User> atual = listar();
            atual.add(usuario);
            FileOutputStream fos = new FileOutputStream(Info.PATH_FILE_USERS);
            ObjectOutputStream oos = new ObjectOutputStream(fos);
            oos.writeObject(atual);
            oos.close();
        } catch (IOException ex) {
            System.out.println("Erro ao inserir usuário");
        }
    }

    public static ArrayList<User> listar() {
        ArrayList<User> lista = new ArrayList();
        FileInputStream fis = null;
        try {
            fis = new FileInputStream(Info.PATH_FILE_USERS);
            ObjectInputStream ois = new ObjectInputStream(fis);
            lista = (ArrayList<User>) ois.readObject();
            ois.close();
            return lista;
        } catch (FileNotFoundException e) {
            System.out.println("Arquivo não encontrado");
        } catch (EOFException e) {  // arquivo vazio
            return lista;
        } catch (IOException | ClassNotFoundException e) {

        } finally {
            try {
                fis.close();
            } catch (IOException ex) {
                System.out.println("Erro ao ler arquivo");
            }
        }
        return lista;
    }

}