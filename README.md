# Sensor Data Extraction and Graphing

This project allows you to extract data from a sensor, read the data from a separate file, and convert it into a graph.

## Materials Required
- **Raspberry Pi Zero 2W**
- **ZMPT101B Voltage Sensor**
- **4 Female-to-Female Jumper Wires**

## Wiring Instructions
Connect the ZMPT101B sensor to the Raspberry Pi Zero 2W as follows:

| ZMPT101B Pin | Raspberry Pi Pin |
|-------------|-----------------|
| **GND** | **GND** |
| **OUT** | **Any GPIO Pin** |
| **VCC** | **5V or 3.3V** |

## Setup and Execution
1. **Modify the Code:**
   - Open the `veri_write.py` file.
   - Update the **GPIO pin number** to match the one you connected the ZMPT101B OUT pin to.
   - Save the file.

2. **Connect the Components:**
   - Ensure all the connections are secure.
   - Connect the ZMPT101B sensor to the voltage source you want to measure.

3. **Run the Program:**
   - Open the terminal on Raspberry Pi.
   - Navigate to the folder containing your code.
   - Run the following commands:
     ```bash
     python3 /home/pi/veri/veri_write.py
     ```
     *(This writes the sensor data to a file.)*
     
     ```bash
     python3 /home/pi/veri/veri_read.py
     ```
     *(This reads the data and generates a graph.)*

## Important Notes
- The ZMPT101B sensor outputs **analog data**, but the Raspberry Pi Zero 2W does **not** have a built-in ADC (Analog-to-Digital Converter).
- Without an ADC (like ADS1015), the Raspberry Pi will only recognize **high (1) or low (0) signals**.
- If you need actual voltage values, use an **ADC module** to convert the analog signal into digital values.

---

## License

This project is licensed under the General Public License - see the [LICENSE](LICENSE) file for details.
