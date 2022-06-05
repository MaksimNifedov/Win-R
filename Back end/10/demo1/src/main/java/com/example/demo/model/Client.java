package com.example.demo.model;

import java.util.Arrays;
import java.util.List;

public class Client {
    private String artist;
    private String phone;

    public String getPhone() {
        return phone;
    }

    public void setPhone(String phone) {
        this.phone = phone;
    }
    public String getArtist() {
        return artist;
    }

    public void setArtist(String artist) {

        List<String> nameArtst  = Arrays.asList("no-name","mc-pupkin","golden-hearts");
            if(nameArtst.contains(artist)){
                this.artist = artist;
            }
       else {
                this.artist = null;

            }


    }
}
