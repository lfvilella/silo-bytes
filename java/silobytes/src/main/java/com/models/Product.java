package com.models;

/**
 *
 * @author felipe
 */
import java.io.Serializable;


public class Product implements Serializable {
    String name;
    String description;
    
    public Product(){
        this.name = "";
        this.description = "";
    }
    
    public Product(String name, String description){
        this.name = name;
        this.description = description;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    
    
}
