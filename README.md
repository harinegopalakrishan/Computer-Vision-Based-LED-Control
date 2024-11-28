# Computer-Vision-Based-LED-Control

https://github.com/user-attachments/assets/6f4f5208-ad2e-4834-baa2-7d2c6cdac94b

- This project demonstrates the use of computer vision to control an LED. 
- By leveraging a camera feed, the system detects specific gestures or movements to activate or deactivate an LED. 
- The implementation combines computer vision techniques with hardware control to achieve an interactive and innovative solution.
------
Features
- Real-Time Object Detection: Uses a computer vision algorithm to detect specific gestures or patterns in the camera feed.
- LED Control: Controls the state of an LED (ON/OFF) based on the detected input.
- PyFirmata Integration: Seamlessly communicates with Arduino using the PyFirmata library.
- Hardware Integration: Communicates with microcontrollers or similar devices to send control signals.
---
Prerequisites

Software:
- Python (3.9.13)
- cvzone 1.6.1(pip install cvzone)
- pyFirmata 1.1.0(pip install pyfirmata)

Hardware:
- Webcam.
- Arduino UNO
- LED.
---
Procedures:

Step 1:
Hardware Setup
- Before running the project, ensure your hardware setup is ready
- Components Needed:
		5xLED,
		Arduino UNO,
		Breadboard,
		Jumper Wires.

Step 2:
- Upload the StandardFirmata sketch to your Arduino:

- Open the Arduino IDE.
- Go to File > Examples > Firmata > StandardFirmata.
- Select the correct board and port, then upload the sketch to your Arduino.

Step 3:
- Run controller.py

Step 4:
- Run app.py



			
