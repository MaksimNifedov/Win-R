package com.example.demo.controller;


import com.example.demo.model.Client;
import com.example.demo.service.ClientService;
import net.minidev.json.JSONObject;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RestController;

import java.util.HashMap;
import java.util.List;
import java.util.Map;

@RestController
public class ClientController {
    private final ClientService clientService;
    private static final HashMap<String, Integer> count = new HashMap<>();

    JSONObject sampleObject = new JSONObject();


    @Autowired
    public ClientController(ClientService clientService) {
        this.clientService = clientService;
    }

    @PostMapping(value = "/clients")
    public ResponseEntity<?> create(@RequestBody Client client) {
        if(client.getArtist()!=null) {
            clientService.create(client);
            return new ResponseEntity<>(HttpStatus.CREATED);
        }
        else {
            return new ResponseEntity<>(HttpStatus.NOT_FOUND);
        }
    }
    @GetMapping(value = "/clients")
    public ResponseEntity< Map<Object,Long>> read() {
        final List<String> clients = clientService.readAll();
        Map<Object,Long> resultMap = new HashMap<>();
        for (String element : clients) {
            if (resultMap.containsKey(element)) {
                Long ttt = resultMap.get(element)+1;
                resultMap.put(element, ttt);
            } else {
                resultMap.put(element, 1L);
            }
        }
        return clients != null &&  !clients.isEmpty()
                ? new ResponseEntity<>(resultMap, HttpStatus.OK)
                : new ResponseEntity<>(HttpStatus.NOT_FOUND);
    }
}
