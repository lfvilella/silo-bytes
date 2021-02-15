package com;

/**
 *
 * @author felipe
 */
import javafx.fxml.FXML;
import javafx.fxml.Initializable;
import javafx.scene.control.ListView;

import com.models.User;
import com.utils.File;
import java.net.URL;
import java.util.ArrayList;
import java.util.ResourceBundle;
import javafx.collections.FXCollections;
import javafx.collections.ObservableList;


public class UserListController extends BaseController implements Initializable {

    @FXML
    private ListView<User> userListView;

    private ArrayList<User> users = File.userList();
    private ObservableList<User> usersDisplay;
    
    @Override
    public void initialize(URL arg0, ResourceBundle arg1) {
        this.usersDisplay = FXCollections.observableArrayList(users);
        this.userListView.setItems(this.usersDisplay);
    }

}