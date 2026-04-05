package com.backend.donna;

import org.springframework.web.bind.annotation.*;
import org.springframework.web.client.RestTemplate;
import java.util.Map;
import java.util.HashMap;

@RestController
@RequestMapping("/bot")
public class WebhookController {

    private final RestTemplate restTemplate = new RestTemplate();

    @PostMapping(value = "/receive", produces = "application/xml")
    @ResponseBody
    public String receive(@RequestParam("Body") String body) {
        try {
            // 1. Send the WhatsApp text to your Python "Brain"
            // Use 127.0.0.1 to be more specific than 'localhost'
            String pythonUrl = "http://127.0.0.1:8000/analyze";

            // 2. Prepare the request as a Map
            Map<String, String> request = new HashMap<>();
            request.put("text", body);

            // 3. Call Python and get the response as a Map
            // This FIXES the "Type definition error" you were seeing
            Map<String, Object> responseFromBrain = restTemplate.postForObject(pythonUrl, request, Map.class);

            // 4. Extract the pieces from the Map
            // We cast them to String because the Map holds Objects
            String replyText = (String) responseFromBrain.get("response_to_user");
            String intent = (String) responseFromBrain.get("intent");

            // 5. Log the action in your Java Console
            System.out.println("\n--- DONNA ACTION LOG ---");
            System.out.println("User Said: " + body);
            System.out.println("AI Intent: " + intent);
            System.out.println("AI Reply:  " + replyText);
            System.out.println("------------------------\n");

            // 6. Send the reply back to your phone via Twilio
            return "<Response><Message><Body>" + replyText + "</Body></Message></Response>";

        } catch (Exception e) {
            // Print the full stack trace in your IDE so we can see what actually went wrong
            e.printStackTrace();
            return "<Response><Message><Body>Donna Brain Freeze: " + e.getMessage() + "</Body></Message></Response>";
        }
    }
}