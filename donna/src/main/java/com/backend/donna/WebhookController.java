package com.backend.donna;

import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.client.RestTemplate;

import java.util.HashMap;
import java.util.Map;

@RestController
public class WebhookController {

    @PostMapping(value = "/webhook", produces = "application/xml")
    public String receiveMessage(
            @RequestParam("Body") String body,
            @RequestParam("From") String from) {

        System.out.println("User Message: " + body);

        RestTemplate restTemplate = new RestTemplate();

        Map<String, String> request = new HashMap<>();
        request.put("message", body);

        Map response = restTemplate.postForObject(
                "http://localhost:8000/parse",
                request,
                Map.class
        );

        System.out.println("AI Response: " + response);

        return "<Response><Message>Got it 👀</Message></Response>";
    }
}