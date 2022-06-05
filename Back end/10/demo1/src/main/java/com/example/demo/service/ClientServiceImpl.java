package com.example.demo.service;

import com.example.demo.model.Client;
import org.springframework.stereotype.Service;

import java.util.ArrayList;
import java.util.List;

@Service
public class ClientServiceImpl implements ClientService {


    // Хранилище клиентов
    private static final ArrayList <String> CLIENT_REPOSITORY_MAP = new ArrayList<>();


    @Override
    public void create(Client client) {

        CLIENT_REPOSITORY_MAP.add(client.getArtist());


    }

    public List<String> readAll() {

        return new ArrayList<>(CLIENT_REPOSITORY_MAP);
    }


}
