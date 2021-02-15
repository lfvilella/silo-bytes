package com;

import com.models.User;
import com.utils.File;
import javafx.fxml.FXML;
import javafx.scene.control.TextField;

/**
 *
 * @author felipe
 */
public class CreateUserController {
    @FXML
    private TextField usernameField;

    @FXML
    private TextField completeNameField;

    @FXML
    private TextField passwordField;

    @FXML
    private void create() {
        User user = new User();
        user.setLogin(this.usernameField.getText());
        user.setNome(this.completeNameField.getText());
        user.setSenha(this.passwordField.getText());
        File.inserir(user);
        
        cleanFields();
    }
    
    @FXML
    private void cleanFields(){
        this.usernameField.setText("");
        this.passwordField.setText("");
        this.completeNameField.setText("");
    }
}
