# Twilio Trivia

This repository contains a Flask app that uses a Twilio phone number to send trivia questions and check answers based on the user reply.


### Using the App
You can send a message containing any text to 714-278-4402 and wait to get a question. Once you receive the question, you can reply with your answer just as one letter (e.g. A). Then you will get a response with either the correct answer or letting you know that your answer was correct.

### Example

![twilio-trivia-screenshot](https://user-images.githubusercontent.com/28850719/34463702-58c23b2c-ee19-11e7-8c80-413cbb01226e.png)

### Recreating the App
In order to run your own version of the app and add more functionality, you'll need a Twilio account.

You can create a free Twilio account to get your `twilio_account_sid` and `twilio_auth_token`and setup a new phone number. You can sign up here: https://www.twilio.com/try-twilio.

This app also uses a free trivia API called opentdb.com. You can simply make a request and specify the number of questions you want. You can also specify other parameters such as category and difficulty. For more information see here: https://opentdb.com/api_config.php.

