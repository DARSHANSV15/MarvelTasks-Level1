# MarvelTasks-Level1

# Task 1: 3D Printing
### 3D Printers
3D printers are devices that create three-dimensional objects by depositing material layer by layer based on a digital model. The basic operation involves slicing a 3D model into thin layers and then gradually building the physical object by adding these layers on top of each other.![Alt](https://worldoflilliputs.com/wp-content/uploads/2019/03/1-Copy.jpg)
### Slicer
Slicer translates 3D models into a series of instructions (G-code) that the 3D printer can understand and execute. Slicer software takes into account various parameters, such as layer height, infill density, print speed, and support structures, to generate the optimal toolpaths for creating a physical object layer by layer.
### STL File
STL (Standard Triangle Language or Stereolithography) is a file format widely used in 3D printing. It represents the surface geometry of a 3D object using a collection of triangular facets.
### G-code File
G-code is a programming language used in 3D printing. G-code instructions control the movements and operations of machines, specifying toolpaths and parameters. In the context of 3D printing, G-code files contain a series of commands that guide the 3D printer\'s extruder and build platform to create a physical object layer by layer.
### 3D printer terminologies
* **Bed Temperature:** The temperature of the print bed or build platform, which helps in   the first layer adhesion and overall print stability.
* **Infill Density:** The percentage of material used within the interior of a printed object, affecting its strength, weight, and print time.
* **Layer Height:** The thickness of each individual layer of filament laid down during the printing process, impacting print resolution and time.
* **Print Speed:** The speed at which the 3D printer head or nozzle moves while laying down the filament, influencing the print quality and duration.
* **Support Structures:**  Additional, often temporary, material printed to support overhanging features during the printing process, which are removed after completion.
![](https://img.playbook.com/-cvNoCr21BVWIT8itMoIxyYog57aGyYzbtx1AsQo8ow/Z3M6Ly9wbGF5Ym9v/ay1hc3NldHMtcHVi/bGljL2I0NTY2YTBj/LWI5NDYtNDBmZC1i/MDZjLTdjYzU0MTFi/ZTAyNA)
_______
# Task 2: API
![API](https://voyager.postman.com/illustration/diagram-what-is-an-api-postman-illustration.svg)
An **API (Application Programming Interface)** is a set of rules and tools that allows different software applications to communicate with each other. It defines the methods and data formats that applications can use to request and exchange information. APIs facilitate the integration of different systems, enabling them to work together seamlessly.
#### Crux Code:
```js
$(function () {
  $("#myForm").submit(function (e) {
    e.preventDefault();

    var city = $("#city").val();

    getWeather(city);
  });
});

function getWeather(city) {
  $(".weather-temperature").openWeather({
    key: "ea5ceda552fc62d695e46455e0a5ddbb",
    city: city,
    descriptionTarget: ".weather-description",
    windSpeedTarget: ".weather-wind-speed",
    minTemperatureTarget: ".weather-min-temperature",
    maxTemperatureTarget: ".weather-max-temperature",
    humidityTarget: ".weather-humidity",
    sunriseTarget: ".weather-sunrise",
    sunsetTarget: ".weather-sunset",
    placeTarget: ".weather-place",
    iconTarget: ".weather-icon",
    customIcons: "../src/img/icons/weather/",
    success: function (data) {
      // show weather
      $(".weather-wrapper").show();
      console.log(data);
    },
    error: function (data) {
      console.log(data.error);
      $(".weather-wrapper").remove();
    },
  });
}
```
![Alt](https://img.playbook.com/Gn7bpVASYph9WDjc-_prftAgU5UBbVtI9n3bnnjJe2A/Z3M6Ly9wbGF5Ym9v/ay1hc3NldHMtcHVi/bGljLzc0ZTliZTYy/LTJmODEtNDk3Ny1i/N2NjLTljNWI3MTI0/MTRmYw)
_____
# Task 3: Working with Github
**GitHub** is a platform that allows developers to automate their software development workflows directly within the GitHub repository. GitHub enables continuous integration and continuous deployment (CI/CD) processes, making it easier for teams to collaborate and streamline their development pipelines.<br />

**Forking** refers to the process of creating a personal copy of someone else\'s repository (a collection of files and the entire version history of those files) in a distributed version control system like Git. When you fork a repository, you are essentially creating your own independent copy of the project, which can be modified without affecting the original repository.<br />

A **pull request (PR)** in GitHub is a proposed code change submitted by a developer for review and integration into the main codebase.
![](https://img.playbook.com/PiJnGwXuM_PM9UjnBDIwYtgQjLnv0xQHwTbt56VN3-8/Z3M6Ly9wbGF5Ym9v/ay1hc3NldHMtcHVi/bGljLzlhZTY5ZTRh/LTI1YjItNGRjNS04/ZjM2LTVlYjkzMDBk/MmExYg)
![](https://img.playbook.com/c2eZgNM0zNvC72q_pE16fvJUaco2EQtohiQzwUJRShM/Z3M6Ly9wbGF5Ym9v/ay1hc3NldHMtcHVi/bGljL2U3ODljNGIz/LWYzYzQtNGJlMC05/NTcwLTgxMGEwMDgw/YmJlZA)
![](https://img.playbook.com/quO27iUgfCDEphZuTk4Vx9IkC3hoM1x6y-qAmFTSqfI/Z3M6Ly9wbGF5Ym9v/ay1hc3NldHMtcHVi/bGljLzZiZTBkN2Iw/LTQwMmMtNDhhMi1i/MGJhLTRmMTI4NmZj/YzQ4Mg)
_____
# Task 4: Get familiar with the command line on ubuntu:
* Create a folder named test.
* cd into that folder.
* Create a blank file without using any text editor.
* List the files in that folder.
* Create 2600 folders in this folder where each folder is named M90.
```shell
for i in {1..2600}; do
    mkdir "M$i"
done
```
* Concatenate two text files containing any random text and display them on the terminal.
```shell
echo "Random Text File 1" &gt; file1.txt
echo "Random Text File 2" &gt; file2.txt
cat file1.txt file2.txt
```
![](https://img.playbook.com/WRowWO_KNQkxpIRH3UckRfbZ0cRodQDZHid0eur5XAU/Z3M6Ly9wbGF5Ym9v/ay1hc3NldHMtcHVi/bGljLzVlMTM2YTcx/LWY3N2ItNGEyMS05/Yjc5LTJhYmY3ZGY4/NGUwYQ)
![](https://img.playbook.com/Mc1LEdbvOjzHSmuGyO_bGaJ6OXaNXUGm64hjQuoMbkg/Z3M6Ly9wbGF5Ym9v/ay1hc3NldHMtcHVi/bGljLzA4NTU4Mjk2/LTFkMTktNDRhZi1i/YmM0LTlkMmUwMWY0/YjIzOQ)
[Check the full code here (Github repo).](https://github.com/DARSHANSV15/MarvelTasks-Level2/tree/main/Task4_UbuntuCLI)
<br /><br />
_____
# Task 6: Working with Pandas and Matplotlib:
**Pandas** is a Python library for data manipulation, offering structures like DataFrame for efficient handling of structured data, crucial in data science and analysis.<br /><br />
**Matplotlib** is a comprehensive Python 2D plotting library, enabling the creation of diverse visualizations with fine-grained customization.
![](https://img.playbook.com/m2FmbfJhFb_2rWJvw-OjP26BHMTf693-Dyznja_TKDc/Z3M6Ly9wbGF5Ym9v/ay1hc3NldHMtcHVi/bGljLzE3MmY1Zjcy/LTk4OGUtNDk2OC04/MmYzLTFlMmI4ZWY3/ZjA0Mw)
![](https://img.playbook.com/76dpxX6WlPWkGYOmIY6T84jrq5hNroYnyH7k1FcFqlc/Z3M6Ly9wbGF5Ym9v/ay1hc3NldHMtcHVi/bGljLzJmNjc1YmJi/LWZmOWEtNDg4ZC04/OGY1LTYyMjZlOTVj/MjgzZA)
![](https://img.playbook.com/peDrDj3qgmwdlgpqOCno0lWaVYHQZ6FEVvry-NgGAck/Z3M6Ly9wbGF5Ym9v/ay1hc3NldHMtcHVi/bGljL2FhMzYzNzcw/LTJjOTEtNGUwMC04/ZjM1LTJjMWIyZTQx/NmYwNA)
![](https://img.playbook.com/3pQyEHGoDaxxbjhHojLQiFTK6RTx0FAoAHFDr7iGQHY/Z3M6Ly9wbGF5Ym9v/ay1hc3NldHMtcHVi/bGljLzY1NTU0OTA4/LTliMGEtNDU2ZS04/NmZiLWFhZjI2YTNk/MGU2Nw)
_____
# Task 7: Create a Portfolio Webpage
A portfolio webpage is a personal or professional website that showcases an individual\'s or a company\'s work, achievements, skills, and projects. It serves as a digital portfolio, providing a centralized platform to display a collection of work samples, resume, and other relevant information.<br /><br />
* [My portfolio webpage link](https://darshansv15.github.io/portfolio/)<br />
* [Git Repo](https://github.com/DARSHANSV15/portfolio/)<br /><br />
_____
# Task 8: Writing Resource Article using Markdown
Markdown is a lightweight markup language that uses plain text formatting syntax to stylize and structure documents, widely used for creating content for the web, including documents, blog posts, and readme files.<br /><br />
* [Link to the article]()<br /><br />
_____
# Task 9: Tinkercad
### Distance measurement using Ultrasonic sensor and Arduino
**Arduino:** It is an open-source electronics platform. It consists ATmega328 8-bit Microcontroller. It can be able to read inputs from different sensors &amp; we can send instructions to the microcontroller in the Arduino. It provides Arduino IDE to write code &amp; connect the hardware devices like Arduino boards &amp; sensors.<br /><br />
**Ultrasonic Sensor:** An ultrasonic Sensor is a device used to measure the distance between the sensor and an object without physical contact. This device works based on time-to-distance conversion.<br /><br />
**Working Principle of Ultrasonic Sensor:**<br />
Ultrasonic sensors measure distance by sending and receiving the ultrasonic wave. The ultrasonic sensor has a sender to emit the ultrasonic waves and a receiver to receive the ultrasonic waves. The transmitted ultrasonic wave travels through the air and is reflected by hitting the Object. Arduino calculates the time taken by the ultrasonic pulse wave to reach the receiver from the sender. <br /><br />We know that the speed of sound in air is nearly 344 m/s.<br /><br />So, the known parameters are time and speed (constant). Using these parameters, we can calculate the distance traveled by the sound wave.
```Formula: 
Distance = Speed * Time
```
In the code, the “duration” variable stores the time taken by the sound wave traveling from the emitter to the receiver. That is double the time to reach the object, whereas the sensor returns the total time including sender to object and object to receiver. Then, the time taken to reach the object is half of the time taken to reach the receiver. So we can write the expression as
```
Distance = Speed of Sound in Air * (Time Taken / 2)
Note: Speed of sound in air = 344 m/s.
```
### Circuit Diagram
![](https://media.geeksforgeeks.org/wp-content/uploads/20221112194103/UltrasonicDistancecircuit.jpg)
![](https://media.geeksforgeeks.org/wp-content/uploads/20221121195114/UltrasonicDistanceMeasurementOutput.gif)
* [Link to my work](https://www.tinkercad.com/things/dDJksTARloq-test-circuit-for-distance-measurement-using-arduino-?sharecode=EQj07RLpfInTQeNAvb9V1PwPDKR_eUCU13ZuRBbewAg)
<br /><br />
_____
# Task 11: LED Toggle Using ESP32
The primary goal of this tutorial is to fabricate a functional web server capable of controlling two LEDs connected to the GPIO pins of the ESP32. This web server will be readily accessible by inputting the ESP32’s IP address into any browser within the local network. The web interface will be equipped with ON/OFF buttons, providing an intuitive means of managing the LED states.<br />This is just a simple example to build a web server that controls ESP32 outputs pins. here we are using LED for executing this project.
###  Components Required
* ESP32 development board –  read ESP32 Development Boards Review and Comparison
* 2x 5mm LED
* 2x 330 Ohm Resistor
* Breadboard
* Jumper wires
![](https://img.pbkstaging.com/gSRlyKPPuIwtfCWL28f09Kg43LaF9vUJdJZ4QlVgSIs/Z3M6Ly9wbGF5Ym9v/ay1hc3NldHMtcHVi/bGljL2EyOTFjY2Jh/LWM3NGUtNGE4Yi04/OTM0LThlY2I3NGEy/NTA1Mg)
![](https://img.playbook.com/5IH49vba0Zsj4ANvdBPIcV-nhizTXu-xrk7AC6KBtA4/Z3M6Ly9wbGF5Ym9v/ay1hc3NldHMtcHVi/bGljLzg1MWIxMzc0/LTg0NzYtNDNiZS1h/YWM1LTMzN2U1Y2Mx/NjJiYg)
![](https://img.pbkstaging.com/cq4uJ3kL5aLBBu89h3tIaH0W2tsw_l5OhJNp5RQMC6M/Z3M6Ly9wbGF5Ym9v/ay1hc3NldHMtcHVi/bGljLzUyNDczNDEx/LTYxNzMtNDE3Zi1h/YTAzLTk2ODlhNWE1/NmMxYw)
_____
# Task 12: Soldering Prerequisites
### What is Soldering?
Soldering is the process of joining two or more electronic parts together by melting solder around the connection. Solder is a metal alloy and when it cools it creates a strong electrical bond between the parts.
![](https://df16b0.p3cdn1.secureserver.net/wp-content/uploads/2017/04/how-to-solder-reference-guide-section-1.jpg)
### Soldering Tools
* Soldering Iron
* Soldering Station
* Brass or Conventional Sponge
* Soldering Iron Stand
* Solder
* Perf Board
* Flux
### Desoldering
The good thing about using solder is the fact that it can be removed easily in a technique known as desoldering. This comes in handy if you need to remove a component or make a correction to your electronic circuit.
### My Work
![img1](https://img.playbook.com/jstGbGPttFkVUakQIjc0XUAWfC3yxi2EPhMLJVpd5lU/Z3M6Ly9wbGF5Ym9v/ay1hc3NldHMtcHVi/bGljL2JhYjYxNWJk/LTc2NzktNDA5Yy1h/N2U0LTk1NzY5MGY3/NjI0Mg)
![img2](https://img.playbook.com/ymMbs67u8rN-u2hPsjnZ5bLrJJ7kVnn1G5nMAduWlPE/Z3M6Ly9wbGF5Ym9v/ay1hc3NldHMtcHVi/bGljLzRiM2Y4ZDAy/LWMwMTctNGFjMC04/YzVhLWFmNTRiNzE0/YTEzMQ)
_____
# Task 13: 555 Astable Timer
An **astable 555 multivibrator** is a type of electronic oscillator circuit that uses a popular integrated circuit (IC) known as the 555 timer IC that produces continuous square wave or pulse wave output, commonly used for generating clock signals and timekeeping in digital circuits.  <br />
In the astable mode, the 555 timer functions as an oscillator, generating a continuous square wave output. This makes it useful for generating clock pulses, tone generation, and various timing applications.
### Why "555"?
The name "555" comes from the three 5-kiloohm resistors used in the original design in its internal voltage divider network.
### What is an Oscilloscope?
An oscilloscope is an electronic test instrument used to visualize electrical signals as they vary over time. It displays the voltage of an electrical signal on a two-dimensional graph, with the vertical axis representing voltage and the horizontal axis representing time. This graphical representation is called an oscillogram or waveform.
![](https://img.playbook.com/bsbJ40fVE91v4JTf4c02sGUDdF7JyQLvyBI11RHdNz0/Z3M6Ly9wbGF5Ym9v/ay1hc3NldHMtcHVi/bGljLzIxYmNlZGI0/LTkxMWItNGZiMi05/MGY2LWM5MzU0MDdm/MGY5MQ)
![](https://img.playbook.com/81DzSazo-1f_wBSa22t72SXypV0lWGTfL4uSh-P4qw4/Z3M6Ly9wbGF5Ym9v/ay1hc3NldHMtcHVi/bGljL2MyMjU5M2Vj/LWNlMGItNGJlMy05/NDJlLTRkY2Y1MTY1/YWQ2OQ)
![](https://img.playbook.com/_6qA0_ldFGQm7XQNcsRmdkekEt6awWhNrgf6c9Sx9qA/Z3M6Ly9wbGF5Ym9v/ay1hc3NldHMtcHVi/bGljLzlhYTM2ZDk0/LTEzMjctNDFkNS04/ODFmLTlkMjM5NGIy/NzdmOA)
_____
# Task 15: Active Participation
I took part in the CodeFury-6.0 conducted by IEEE UVCE where the competitors in teams were given a task to make a web or mobile application addressing the Mental Health issues among the Gen-Z youths.  
I along with two of my classmates created a wonderful website, the site is live on github and the link is given below.
![CodeFury-6.0 Participation certificate](https://img.playbook.com/r8KDqYlGkoJgqbsFDJsYbAt8ywFIghaaxsTQ9Xcnp_w/Z3M6Ly9wbGF5Ym9v/ay1hc3NldHMtcHVi/bGljL2I5OTM1YTI5/LTIyYTUtNGNiZS1i/NzgwLWFlNzVlODhm/YWY0Ng)
* [Mental Health Website](https://darshansv15.github.io/CodeFury-6.0/)
<br /><br />
_____