package com.backend.donna;

import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class WebhookController {

    @PostMapping("/webhook")
    public String receiveMessage(
            @RequestParam("Body") String body,
            @RequestParam("From") String from) {

        System.out.println("Message: " + body);
        System.out.println("From: " + from);

        return "Hi, I'm Donna 👀";
    }
}