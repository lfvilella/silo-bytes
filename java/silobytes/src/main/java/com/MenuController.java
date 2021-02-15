package com;

import java.io.IOException;
import javafx.fxml.FXML;

/**
 *
 * @author felipe
 */
public class MenuController {
    @FXML
    private void goToCreateUser() throws IOException{
        App.setRoot("createUser");
    }
    
    @FXML
    private void quit(){
        System.exit(0);
    }
}
