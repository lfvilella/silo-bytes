package com.models;

/**
 *
 * @author felipe
 */
import java.time.LocalDateTime;
import java.io.Serializable;


public class Base implements Serializable {
    LocalDateTime createdAt;
    LocalDateTime updatedAt;
    
    public Base(){
        this.createdAt = LocalDateTime.now();
        this.updatedAt = LocalDateTime.now();
    }
    
    public LocalDateTime getCreatedAt() {
        return createdAt;
    }

    public void setCreatedAt(LocalDateTime createdAt) {
        this.createdAt = createdAt;
    }

    public LocalDateTime getUpdatedAt() {
        return updatedAt;
    }

    public void setUpdatedAt(LocalDateTime updatedAt) {
        this.updatedAt = updatedAt;
    }
}
