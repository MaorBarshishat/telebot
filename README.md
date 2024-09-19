now I want u to fix here where u want

# telebot_auto_testing
this is an appium client that tests the telebot automatically
it communicates with the appium server.

in order to execute the test you may either run it as a socker, or as a python program.

as a docker:
```
   sudo docker run -d maorbarshishat/appium_client_auto_test_maor:2.0
```

as a python command:
 ```
    git clone https://github.com/MaorBarshishat/telebot_auto_testing.git
    cd telebot_auto_testing/
    pip install -r requirements.txt
    python3 prepare_device.py
    python3 testing.py
```
