# 💻 Classes Challenge

This project focuses on designing a system that manages multiple processes running simultaneously on different machines. Some of these processes share similar patterns in their request, response, and structure. The goal is to create a unified execution stack capable of handling any job without duplicating code.  

## 🧠 Challenge Description  

You are tasked with creating an execution stack that accepts any job, processes it, and returns the data. To achieve this, you must design a structure where the common aspects of requests, processing, and responses are implemented in a shared and reusable way.  

### Key Requirements

1. **Interfaces**: Define interfaces for the common aspects of processes.  
2. **Polymorphism**: Use polymorphism to differentiate operations dynamically.  
3. **Hierarchy**: Establish a class hierarchy to implement common or specific methods across processes.  

## 🚀 Objectives  

1. Create a generic base class with common attributes and methods.  
2. Extend this base class into specialized subclasses tailored for specific types of processes.  
3. Leverage **interfaces**, **polymorphism**, and **hierarchy** to minimize code duplication.  
4. Use **Pandas** to integrate data manipulation into the challenge by processing a dataset as part of the solution.  

## 🛠️ Approach  

- **Generic Class**: Design a base class that includes shared logic for request handling, data processing, and response generation.  
- **Subclasses**: Create subclasses inheriting from the base class and implementing specific details for different types of processes.  
- **Dataset Integration**: Use a dataset to simulate real-world scenarios and align the challenge with practical applications of Python and Pandas.  

## 📂 Project Structure  

```plaintext  
ClassesChallenge/  
│  
├── base_class.py           # Generic base class with shared logic  
├── specialized_class_a.py  # Subclass for Process Type A
├── specialized_class_b.py  # Subclass for Process Type B
├── ...
├── dataset/                # Directory for the dataset used in the challenge  
│   └── data.csv
├── main.py                 # Entry point for the project execution  
└── README.md               # Project overview and instructions  
```  

## 📄 Dataset  

Source: The dataset is avaliable at [Google Drive](https://drive.google.com/file/d/1RTruyBzZdcfi-jMAWNPVineFINQ0CNu-/)
The project uses a dataset to simulate process execution and align the challenge with data manipulation using Pandas. The dataset should be placed in the `dataset` directory and referenced in the code for processing.  

## 📈 Goals  

- Develop a clean and reusable codebase for handling multiple processes.  
- Apply object-oriented programming principles (OOP): interfaces, polymorphism, and hierarchy.  
- Enhance Python and Pandas skills through practical implementation.  

## 🛠️ Tools and Libraries  

- **Python**: The primary language for the challenge.  
- **Pandas**: For data manipulation and analysis.  

## 🚀 How to Run  

1. Clone the repository and navigate to the project directory.  
2. Ensure the dataset is placed in the `dataset` directory.  
3. Run the `main.py` file to execute the project and simulate the process execution.  