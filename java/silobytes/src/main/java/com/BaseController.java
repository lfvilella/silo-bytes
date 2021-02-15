package com;

/**
 *
 * @author felipe
 */
import java.io.IOException;
import javafx.fxml.FXML;


public class BaseController {
    @FXML
    private void goToMenu() throws IOException{
        App.setRoot("menu");
    }
    
    @FXML
    private void goToUserCreate() throws IOException{
        App.setRoot("userCreate");
    }
    
    @FXML
    private void goToUserList() throws IOException{
        App.setRoot("userList");
    }
    
    @FXML
    private void quit(){
        System.exit(0);
    }
}
