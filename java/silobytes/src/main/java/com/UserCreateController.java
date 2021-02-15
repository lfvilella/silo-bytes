package com;

/**
 *
 * @author felipe
 */
import com.models.User;
import com.utils.File;
import javafx.fxml.FXML;
import javafx.scene.control.TextField;
import javafx.scene.control.Label;


public class UserCreateController extends BaseController {
    @FXML
    private TextField usernameField;

    @FXML
    private TextField emailField;

    @FXML
    private TextField passwordField;
    
    @FXML
    private Label flashMessageLabel;

    @FXML
    private void create() {
        boolean result = validateFields();
//        System.out.println("usuario ====> ", this.usernameField.getText());
        if (result == false){
            return;
        }
        
        User user = new User();
        user.setUsername(this.usernameField.getText());
        user.setEmail(this.emailField.getText());
        user.setPassword(this.passwordField.getText());
        File.saveUser(user);
        
        this.flashMessageLabel.setText("User created successfully!");
        cleanFields();
    }
    
    @FXML
    private boolean validateFields(){  // do not working... needs be checked this if.
        if (this.usernameField.getText() == ""){
            this.flashMessageLabel.setText("Username must be fill.");
            return false;
        }
        if (this.emailField.getText() == ""){
            this.flashMessageLabel.setText("Email must be fill.");
            return false;
        }
        if (this.passwordField.getText() == ""){
            this.flashMessageLabel.setText("Password must be fill.");
            return false;
        }
        return true;
    }

    
    @FXML
    private void cleanFields(){
        this.usernameField.setText("");
        this.passwordField.setText("");
        this.emailField.setText("");
    }
}
