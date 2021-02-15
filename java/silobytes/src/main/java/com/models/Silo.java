package com.models;

/**
 *
 * @author felipe
 */
public class Silo extends Base {
    String name;
    String description;
    float size;
    
    public Silo(){
        this.name = "";
        this.description = "";
    }
    
    public Silo(String name, String description){
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
    
    public float getSize() {
        return size;
    }

    public void setSize(float size) {
        this.size = size;
    }
}
