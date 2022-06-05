package com.example.demo.service;

import com.example.demo.model.Client;

import java.util.List;
public interface ClientService {

    /**
     * Создает нового клиента
     * @param client - клиент для создания
     */
    void create(Client client);

    /**
     * Возвращает список всех имеющихся клиентов
     * @return список клиентов
     */
    List<String> readAll();


    /**
     * Возвращает клиента по его ID
     * @param phone - телефонный номер клиента
     * @return - объект клиента с заданным телефонным номером
     */


    /**
     * Обновляет клиента с заданным мобильным номером,
     * в соответствии с переданным клиентом
     * @param client - клиент в соответсвии с которым нужно обновить данные
     * @param phone  - номер телефона клиента которого нужно обновить
     * @return - true если данные были обновлены, иначе false
     */

}
