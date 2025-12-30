### **Overview**

This tool was created to collect and analyze job listing data.

The personal goal behind the project was to gather as much information as possible about specific roles in order to better understand the technical requirements and prepare accordingly.

It can be used to get a general sense of the current job market, regardless of role or seniority level.

---

### **Current Version**

**Mark I – Prototype**

This version focuses on extracting, transforming, storing, and displaying job listing data.

It does **not** include advanced filtering, data analysis, or enhanced visualizations.

---

### **Features**

- Fetch job listings from the Adzuna API based on a search term
- Store job data locally in a database
- Display saved job listings through a CLI command
- Basic logging and error handling

---

### **Project Structure**

- adzuna_client.py – External API integration
- main.py – CLI entry point and command definitions
- connection.py – Database connection and local persistence setup

---

### **How It Works**

1. The user provides input using the fetch command
2. The system connects to the external API using configured credentials
3. Job data is extracted, transformed, and stored locally
4. Stored data can be displayed using the show command

---

### **Requirements**

- Python 3.x
- External API credentials (Adzuna)
- Internet connection

---

### **Setup**

1. Clone the repository
2. Create a virtual environment
3. Install dependencies
4. Generate your own API credentials (App ID and Key) at:
    
    https://developer.adzuna.com/signup
    
5. Configure environment variables
6. Run the application

---

### **Usage**

```python
python -m src.cli.main fetch developer
python -m src.cli.main fetch "python developer"

python -m src.cli.main show
```

---

### **Limitations**

- Limited number of results per search
- No pagination or filtering
- Intended for learning and experimentation

---

### **Next Steps**

- Improve data visualization
- Add filtering options
- Refactor internal structure
- Improve CLI usability

---

### **License**

> This project is for educational purposes.
> 

---

### **Final Note**

> This project was created with the goal of building something real — a tool that helps me better understand what the job market is asking for and how I can prepare for it.
> 

> This is only a prototype and represents the first step toward a more complete system.
>