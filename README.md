<div align="center">
  <h1>AI-Machine Learning for Workplace Safety</h1>
</div>

## Overview
This repository illustrates the outcomes of our project, where we combined the features of [**YOLOv8**](https://docs.ultralytics.com/models/yolov8/) with the advanced features of the [**ZED 2i Stereo Camera**](https://www.stereolabs.com/en-vn/store/products/zed-2i) to enhance workplace safety. By automating the detection of safety hazards, tracking attendance, and monitoring restricted areas, our system improves compliance and helps prevent accidents in real time.

## Table of Contents
- [Overview](#overview)
- [Introduction](#introduction)
- [Features](#features)
  - [1. Personal Protective Equipment (PPE) Alliance](#1-personal-protective-equipment-ppe-alliance)
  - [2. Attendance Checking](#2-attendance-checking)
  - [3. Collision Detection](#3-collision-detection)
  - [4. Monitoring Restricted Areas](#4-monitoring-restricted-areas)
- [Project Showcases](#project-showcases)
- [Contributing](#contributing)

## Introduction
This repository demonstrates the outcomes (illustration) of the project, where we combined features of YOLOv8 and the ZED  Stereo Camera to create an intelligent system for workplace safety. Our solution:
- Detects missing personal protective equipment (PPE).
- Monitors attendance real-time video analysis.
- Detects potential collision risks.
- Prevents unauthorized access to restricted areas.

## Features

### 1. Personal Protective Equipment (PPE) Alliance
- **Description:**  
  The AI system detects when essential safety gear is missing and sends an instant alert to supervisors.
- **RESULT:**
-----------------------------------------------------------------------------------------------------------
<table>
  <tr>
    <td align="center">
      <img src="https://github.com/user-attachments/assets/0fc0a5d7-3c85-499f-bff6-6f00e7d2ed09" alt="Image" style="max-width:500px;"><br>
      <a href="https://drive.google.com/file/d/1uZVfHp9Ozv-E5JeqSxvioz4LID68796z/view?usp=sharing">Oriented 2D Bounding Box-Single Object</a>
    </td>
    <td align="center">
      <img src="https://github.com/user-attachments/assets/b145b428-993a-43e4-982c-0ce5d5b66f82" alt="Image" style="max-width:500px;"><br>
      <a href="https://drive.google.com/file/d/19lpnCCVyU8uwEltai_TQamfRccufaTpc/view?usp=sharing">Oriented 2D Bounding Box-Multi Object 1</a>
    </td>
    <td align="center">
      <img src="https://github.com/user-attachments/assets/c15b0713-043c-4aa7-b78e-0a862f78f8b5" alt="Image" style="max-width:500px;"><br>
      <a href="https://drive.google.com/file/d/1kVVWp92PEKI4f0ZZxPNUAjiAo_Yfr6Ti/view?usp=sharing">Oriented 2D Bounding Box-Multi Object 2</a>
    </td>
  </tr>
</table>



  -----------------------------------------------------------------------------------------------------------
  
  ![Image](https://github.com/user-attachments/assets/1a87d790-b2ef-4fd2-960c-612bc90a184d)

<p style="font-size:14px;">
  <a href="https://drive.google.com/file/d/1cfB8La54vsUN23Gm1juyfRsneBOwS861/view?usp=sharing">Detect Gloves</a>
</p>

  -----------------------------------------------------------------------------------------------------------
  
### 2. Attendance Checking
- **Description:**  
  This feature uses video analysis to track and record worker attendance in real time, providing visual insights via 2D-3D bounding boxes visualization, path tracking, and skeletal mapping.
- **RESULT:**

  
  -----------------------------------------------------------------------------------------------------------

  
<table>
  <tr>
    <td align="center">
      <img src="https://github.com/user-attachments/assets/f0b58a09-32d2-446f-a74c-3c17d6f20bf3" alt="Image" style="max-width:500px;"><br>
      <p style="font-size:14px;">
        <a href="https://drive.google.com/file/d/1FOxS07OzbCEtZhL0K0uKo-oL1Jwj5xfJ/view?usp=sharing">3D Single Object Detection</a>
      </p>
    </td>
    <td align="center">
      <img src="https://github.com/user-attachments/assets/a2474dd0-7f34-40c8-86bd-fca357cdaf79" alt="Image" style="max-width:500px;"><br>
      <p style="font-size:14px;">
        <a href="https://drive.google.com/file/d/1mUitkUFkOpuZhfWfF4Pmp74YXTN6fpqE/view?usp=sharing">3D Multi Object Detection</a>
      </p>
    </td>
  </tr>
</table>



-----------------------------------------------------------------------------------------------------------


<p align="left">
  <img src="https://github.com/user-attachments/assets/852547ad-d084-4a65-906b-7d0dea06c2a9" alt="Image" style="width:400px;">
</p>

<p style="font-size:14px;">
  <a href="https://drive.google.com/file/d/10XNzQmqHLbXP0m8IqhA_vULauLyDSXhg/view?usp=sharing">2D-Path Tracking (Object Detection module combined with Positional Tracking)</a>
</p>

-----------------------------------------------------------------------------------------------------------


<p align="left">
  <img src="https://github.com/user-attachments/assets/0305aac2-308f-4b79-8102-38d4a9f039c2" alt="Image" style="max-width:500px;">
</p>

<p style="font-size:14px;">
  <a href="https://drive.google.com/file/d/1Vq03UE4xT31C9A9bUoRnHUZ5scvhwWJ_/view?usp=sharing">Skeletal Mapping</a>
</p>

-----------------------------------------------------------------------------------------------------------

<table>
  <tr>
    <td align="center">
      <img src="https://github.com/user-attachments/assets/7785d6a1-5177-4018-ad1b-314240746e9b" alt="Image" style="width:300px;"><br>
      <p style="font-size:14px;">
        <a href="https://drive.google.com/file/d/1_oGq_Ota1AswhgxY7KoMrF3OaDu4USY-/view?usp=sharing">Glove Tracking 2D Bounding Boxes</a>
      </p>
    </td>
    <td align="center">
      <img src="https://github.com/user-attachments/assets/a0878e4c-84f7-4787-9932-27e633fd257e" alt="Image" style="max-width:500px;"><br>
      <p style="font-size:14px;">
        <a href="https://drive.google.com/file/d/1OOZrPtdO73041hSPGHqUlrspx4ib5MKf/view?usp=sharing">Glove Tracking 3D Bounding Boxes</a>
      </p>
    </td>
  </tr>
</table>



-----------------------------------------------------------------------------------------------------------

### 3. Collision Detection
- **Description:**  
  The system uses AI-powered cameras to continuously monitor potential collision risks and sends instant alerts to prevent accidents. 
- **RESULT:**

<p align="left">
  <img src="https://github.com/user-attachments/assets/47871cd0-0c32-4bd4-b0ad-17fba7604491" alt="Image" style="max-width:500px;">
</p>

<p style="font-size:14px;">
  <a href="https://drive.google.com/file/d/1mmzJ1swOASvycPc1MHiX0xkx3YdBF2yl/view?usp=sharing">Collision 2D Bounding Boxes Detection</a>
</p>

-----------------------------------------------------------------------------------------------------------

### 4. Monitoring Restricted Areas
- **Description:**  
  The system detects unauthorized entries into restricted areas and sends immediate alerts to ensure safety and security.
- **RESULT:**


<p align="left">
  <img src="https://github.com/user-attachments/assets/f9962b3d-2f98-4ff8-b53a-63841e998673" alt="Image" style="max-width:500px;">
</p>

<p style="font-size:14px;">
  <a href="https://drive.google.com/file/d/1KI23bDyp1kJJyESqbUqkN2yBLVCTc7nc/view?usp=sharing">Restricted Areas Monitoring</a>
</p>

-----------------------------------------------------------------------------------------------------------
## Project Showcases
My team and I have showcased our project at two competitions. Please refer to the attached slides and posters for further insight into our work.
- **Slides:**  
  - ASU and Dow Vietnam STEM Program: Engineering Projects (eProjects): [SLIDES_](https://www.canva.com/design/DAGD0D0vCEo/GhAnUO4RIJx7czJX5sYpKA/edit?utm_content=DAGD0D0vCEo&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton)  
  - HCMUT-Bach Khoa Innovation:  
    - Round 1: [SLIDES ROUND_1](https://www.canva.com/design/DAGNahcuLN8/179mbD2YSGEzi08a4v11iA/edit?utm_content=DAGNahcuLN8&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton)  
    - Round 2: [SLIDES ROUND_2](https://www.canva.com/design/DAGOAIKt0Rk/sXdGzur-AA2vTTB4JQXBCg/edit?utm_content=DAGOAIKt0Rk&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton)
- **Poster:**  
  - ASU and Dow Vietnam STEM Program: Engineering Projects (eProjects): [POSTER](https://www.canva.com/design/DAGDn5ZiZlU/-RmX7bFNcwLv10TA8aCVyw/edit?utm_content=DAGDn5ZiZlU&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton)


## Contributing
Contributions are welcome! If you would like to improve this project:
- Fork the repository.
- Create a new branch for your feature or bug fix.
- Submit a pull request with a detailed explanation of your changes.


