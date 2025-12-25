# User Manual – Daylight Glare Measurement Device (DGP)

## 1. Introduction
This manual describes the usage of the daylight glare measurement device
developed for evaluating glare in interior spaces using the
**Daylight Glare Probability (DGP)** metric.

The device is based on a **Raspberry Pi** equipped with a **fisheye camera**
and uses tools from the **RADIANCE** software package, particularly
**Evalglare**, to compute DGP values from HDR images.

---

## 2. System Overview
The measurement system consists of:
- Raspberry Pi (control and processing unit)
- Fisheye camera
- RADIANCE software package
- Bash scripts for automated measurement and evaluation

The system captures fisheye images of the interior environment, converts them
into HDR format, and evaluates glare using the DGP metric.

---

## 3. Hardware Setup

### 3.1 Camera Orientation
The camera must be mounted **with the connection cable pointing downward**.

This orientation is critical because the **position index** used in the DGP
calculation is **not symmetric** for upward and downward directions.
Incorrect camera orientation may lead to inaccurate glare evaluation results.

### 3.2 Camera Placement
- Place the device at the approximate eye position of the observer.
- Ensure that the camera has an unobstructed view of the interior space.

---

## 4. Software Requirements

### 4.1 Accessing the Raspberry Pi
1.  Connect the Raspberry Pi to the same network as your PC.
2.  Open RealVNC and connect.

### 4.2 Running the code
1. Run the file measure.sh at the path home/Documents/GLARE_METER/Bash_sctipts
   - you can run it in the command line using command: bash measure.sh


