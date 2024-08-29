## Output

![](https://github.com/DochevM/Raspberry_Pi_3/blob/main/Documents/Output_ubidots_rednote.gif)

## Connections

| Raspberry Pi 3      |     L154ASUxx      |
| ------------------- | ------------------ |
| GPIO27              | Green              |
| GPIO22              | RED                |
| GPIO17              | BLUE               |
| GND                 | GND                |

![alt text](https://github.com/DochevM/Raspberry_Pi_3/blob/main/Documents/RGB_diagram.png)
![alt text](https://github.com/DochevM/Raspberry_Pi_3/blob/main/Documents/GPIO_diagram.jpg)


## Node-Red project
### Just copy and import this project to Node-Red

<details>

<summary>Here is the code for the project</summary>

```

[
    {
        "id": "7bb27b7ae089c6e5",
        "type": "tab",
        "label": "Flow 1",
        "disabled": false,
        "info": "",
        "env": []
    },
    {
        "id": "9e19ab92.655258",
        "type": "ubidots_in",
        "z": "7bb27b7ae089c6e5",
        "tier": "business",
        "name": "RaspberryPiUbidots",
        "token": "BBUS-tT890bQj0HdEIOF7jsbqOZCS48uQDQ",
        "device_label": "raspberry",
        "tls_checkbox_in": true,
        "custom_topic_checkbox": false,
        "label_variable_1": "control",
        "label_variable_2": "",
        "label_variable_3": "",
        "label_variable_4": "",
        "label_variable_5": "",
        "label_variable_6": "",
        "label_variable_7": "",
        "label_variable_8": "",
        "label_variable_9": "",
        "label_variable_10": "",
        "checkbox_variable_1_last_value": true,
        "checkbox_variable_2_last_value": true,
        "checkbox_variable_3_last_value": true,
        "checkbox_variable_4_last_value": true,
        "checkbox_variable_5_last_value": true,
        "checkbox_variable_6_last_value": true,
        "checkbox_variable_7_last_value": true,
        "checkbox_variable_8_last_value": true,
        "checkbox_variable_9_last_value": true,
        "checkbox_variable_10_last_value": true,
        "x": 350,
        "y": 220,
        "wires": [
            [
                "aa56f39f.127be",
                "65877a10.6f4fc4"
            ]
        ]
    },
    {
        "id": "aa56f39f.127be",
        "type": "function",
        "z": "7bb27b7ae089c6e5",
        "name": "Parse Ubidots Value",
        "func": "var lastValue = msg.payload.control.value;\nmsg.payload = Number(lastValue);\nreturn msg;",
        "outputs": 1,
        "timeout": "",
        "noerr": 0,
        "initialize": "",
        "finalize": "",
        "libs": [],
        "x": 600,
        "y": 220,
        "wires": [
            [
                "c2ce4045.d20e5",
                "7f3ca3e8.c7a3a4"
            ]
        ]
    },
    {
        "id": "c2ce4045.d20e5",
        "type": "rpi-gpio out",
        "z": "7bb27b7ae089c6e5",
        "name": "LED",
        "pin": "17",
        "set": "",
        "level": "0",
        "freq": "",
        "out": "out",
        "bcm": true,
        "x": 830,
        "y": 220,
        "wires": []
    },
    {
        "id": "65877a10.6f4fc4",
        "type": "debug",
        "z": "7bb27b7ae089c6e5",
        "name": "",
        "active": true,
        "tosidebar": true,
        "console": false,
        "tostatus": false,
        "complete": "false",
        "x": 610,
        "y": 300,
        "wires": []
    },
    {
        "id": "7f3ca3e8.c7a3a4",
        "type": "debug",
        "z": "7bb27b7ae089c6e5",
        "name": "",
        "active": true,
        "tosidebar": true,
        "console": false,
        "tostatus": false,
        "complete": "false",
        "x": 850,
        "y": 300,
        "wires": []
    },
    {
        "id": "a78c085c.6e3988",
        "type": "inject",
        "z": "7bb27b7ae089c6e5",
        "name": "",
        "props": [
            {
                "p": "payload"
            }
        ],
        "repeat": "",
        "crontab": "",
        "once": true,
        "onceDelay": 0.1,
        "topic": "",
        "payload": "{\"control\": 0}",
        "payloadType": "json",
        "x": 350,
        "y": 20,
        "wires": [
            [
                "44bd18f.f127168"
            ]
        ]
    },
    {
        "id": "44bd18f.f127168",
        "type": "ubidots_out",
        "z": "7bb27b7ae089c6e5",
        "name": "RaspberryPiUbidots",
        "token": "BBUS-tT890bQj0HdEIOF7jsbqOZCS48uQDQ",
        "label_device": "raspberry-pi",
        "device_label": "raspberry",
        "tier": "business",
        "tls_checkbox": true,
        "x": 600,
        "y": 60,
        "wires": []
    },
    {
        "id": "6b6ca1576c761c04",
        "type": "ubidots_in",
        "z": "7bb27b7ae089c6e5",
        "tier": "business",
        "name": "RaspberryPiUbidots",
        "token": "BBUS-tT890bQj0HdEIOF7jsbqOZCS48uQDQ",
        "device_label": "raspberry",
        "tls_checkbox_in": true,
        "custom_topic_checkbox": false,
        "label_variable_1": "control2",
        "label_variable_2": "",
        "label_variable_3": "",
        "label_variable_4": "",
        "label_variable_5": "",
        "label_variable_6": "",
        "label_variable_7": "",
        "label_variable_8": "",
        "label_variable_9": "",
        "label_variable_10": "",
        "checkbox_variable_1_last_value": true,
        "checkbox_variable_2_last_value": true,
        "checkbox_variable_3_last_value": true,
        "checkbox_variable_4_last_value": true,
        "checkbox_variable_5_last_value": true,
        "checkbox_variable_6_last_value": true,
        "checkbox_variable_7_last_value": true,
        "checkbox_variable_8_last_value": true,
        "checkbox_variable_9_last_value": true,
        "checkbox_variable_10_last_value": true,
        "x": 370,
        "y": 380,
        "wires": [
            [
                "dd076ba064e622d8",
                "2d84680990934525"
            ]
        ]
    },
    {
        "id": "dd076ba064e622d8",
        "type": "function",
        "z": "7bb27b7ae089c6e5",
        "name": "Parse Ubidots Value",
        "func": "var lastValue = msg.payload.control2.value;\nmsg.payload = Number(lastValue);\nreturn msg;",
        "outputs": 1,
        "timeout": "",
        "noerr": 0,
        "initialize": "",
        "finalize": "",
        "libs": [],
        "x": 620,
        "y": 380,
        "wires": [
            [
                "209733c0bc78ac17",
                "9aca8dd00d5664ca"
            ]
        ]
    },
    {
        "id": "209733c0bc78ac17",
        "type": "rpi-gpio out",
        "z": "7bb27b7ae089c6e5",
        "name": "LED",
        "pin": "27",
        "set": "",
        "level": "0",
        "freq": "",
        "out": "out",
        "bcm": true,
        "x": 850,
        "y": 380,
        "wires": []
    },
    {
        "id": "2d84680990934525",
        "type": "debug",
        "z": "7bb27b7ae089c6e5",
        "name": "",
        "active": true,
        "tosidebar": true,
        "console": false,
        "tostatus": false,
        "complete": "false",
        "x": 630,
        "y": 460,
        "wires": []
    },
    {
        "id": "9aca8dd00d5664ca",
        "type": "debug",
        "z": "7bb27b7ae089c6e5",
        "name": "",
        "active": true,
        "tosidebar": true,
        "console": false,
        "tostatus": false,
        "complete": "false",
        "x": 870,
        "y": 460,
        "wires": []
    },
    {
        "id": "3cd3a4ba898f1474",
        "type": "ubidots_in",
        "z": "7bb27b7ae089c6e5",
        "tier": "business",
        "name": "RaspberryPiUbidots",
        "token": "BBUS-tT890bQj0HdEIOF7jsbqOZCS48uQDQ",
        "device_label": "raspberry",
        "tls_checkbox_in": true,
        "custom_topic_checkbox": false,
        "label_variable_1": "control3",
        "label_variable_2": "",
        "label_variable_3": "",
        "label_variable_4": "",
        "label_variable_5": "",
        "label_variable_6": "",
        "label_variable_7": "",
        "label_variable_8": "",
        "label_variable_9": "",
        "label_variable_10": "",
        "checkbox_variable_1_last_value": true,
        "checkbox_variable_2_last_value": true,
        "checkbox_variable_3_last_value": true,
        "checkbox_variable_4_last_value": true,
        "checkbox_variable_5_last_value": true,
        "checkbox_variable_6_last_value": true,
        "checkbox_variable_7_last_value": true,
        "checkbox_variable_8_last_value": true,
        "checkbox_variable_9_last_value": true,
        "checkbox_variable_10_last_value": true,
        "x": 430,
        "y": 600,
        "wires": [
            [
                "c9abec32efe0c024",
                "8fcd20f93d21479a"
            ]
        ]
    },
    {
        "id": "c9abec32efe0c024",
        "type": "function",
        "z": "7bb27b7ae089c6e5",
        "name": "Parse Ubidots Value",
        "func": "var lastValue = msg.payload.control3.value;\nmsg.payload = Number(lastValue);\nreturn msg;",
        "outputs": 1,
        "timeout": "",
        "noerr": 0,
        "initialize": "",
        "finalize": "",
        "libs": [],
        "x": 680,
        "y": 600,
        "wires": [
            [
                "ddee43ddefa12faa",
                "7382e8bfa744706c"
            ]
        ]
    },
    {
        "id": "ddee43ddefa12faa",
        "type": "rpi-gpio out",
        "z": "7bb27b7ae089c6e5",
        "name": "LED",
        "pin": "22",
        "set": "",
        "level": "0",
        "freq": "",
        "out": "out",
        "bcm": true,
        "x": 910,
        "y": 600,
        "wires": []
    },
    {
        "id": "8fcd20f93d21479a",
        "type": "debug",
        "z": "7bb27b7ae089c6e5",
        "name": "",
        "active": true,
        "tosidebar": true,
        "console": false,
        "tostatus": false,
        "complete": "false",
        "x": 690,
        "y": 680,
        "wires": []
    },
    {
        "id": "7382e8bfa744706c",
        "type": "debug",
        "z": "7bb27b7ae089c6e5",
        "name": "",
        "active": true,
        "tosidebar": true,
        "console": false,
        "tostatus": false,
        "complete": "false",
        "x": 930,
        "y": 680,
        "wires": []
    },
    {
        "id": "319fb39a82a61b78",
        "type": "inject",
        "z": "7bb27b7ae089c6e5",
        "name": "",
        "props": [
            {
                "p": "payload"
            }
        ],
        "repeat": "",
        "crontab": "",
        "once": true,
        "onceDelay": 0.1,
        "topic": "",
        "payload": "{\"control2\": 0}",
        "payloadType": "json",
        "x": 360,
        "y": 60,
        "wires": [
            [
                "44bd18f.f127168"
            ]
        ]
    },
    {
        "id": "03dc934b79369edc",
        "type": "inject",
        "z": "7bb27b7ae089c6e5",
        "name": "",
        "props": [
            {
                "p": "payload"
            }
        ],
        "repeat": "",
        "crontab": "",
        "once": true,
        "onceDelay": 0.1,
        "topic": "",
        "payload": "{\"control3\": 0}",
        "payloadType": "json",
        "x": 360,
        "y": 100,
        "wires": [
            [
                "44bd18f.f127168"
            ]
        ]
    }
]

```

</details>