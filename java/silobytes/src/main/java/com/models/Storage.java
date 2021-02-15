package com.models;

/**
 *
 * @author felipe
 */
import java.time.LocalDateTime;
import java.io.Serializable;


public class Storage extends Base implements Serializable {
    Client client;
    Silo silo;
    Product product;
    int quantity;
    LocalDateTime entryDate;
    LocalDateTime withdrawalDate;
    String paymentMethod;
    String status;

    public Storage(
        Client client,
        Silo silo,
        Product product,
        int quantity,
        LocalDateTime entryDate,
        LocalDateTime withdrawalDate,
        String paymentMethod,
        String status
    ) {
        this.client = client;
        this.silo = silo;
        this.product = product;
        this.quantity = quantity;
        this.entryDate = entryDate;
        this.withdrawalDate = withdrawalDate;
        this.paymentMethod = paymentMethod;
        this.status = status;
    }
}
