# Study Planner

#### Video Demo:
https://youtu.be/ScFNFXsEnhM?si=YlwXXOmdRT3kFB9M

#### Description:
Study Planner is a web-based application designed to help users plan their study time in a smart and balanced way. The goal of this project is to generate a fair and realistic study plan based on the user’s available free time and their performance in different subjects.

The user starts by entering their available free time in hours and minutes. Then, they provide the names of their lessons, the score achieved in each lesson, and a total score value. Based on this data, the application automatically calculates the importance of each lesson and distributes the available study time proportionally.

A key feature of this project is that **no lesson is ever removed from the plan**. All lessons receive study time based on their calculated importance. Additionally, the output time is displayed in a human-friendly format. For example, instead of showing `2.5 hours`, the application displays `2 hours and 30 minutes`. All time values are rounded to realistic intervals such as quarter hours, half hours, or full hours.

---

### How It Works
The core logic of the application is based on an **importance calculation**. The importance of each lesson is determined using the ratio between the lesson score and the total score. The user’s free time is then divided proportionally among all lessons based on these importance values.

This approach ensures fairness, prevents unrealistic schedules, and creates a balanced study plan that the user can actually follow.

---

### Technologies Used
This project was developed using the following technologies:

- **Python** as the main programming language
- **Flask** for building the web application
- **SQLite** for storing study plan history
- **HTML & CSS** for the user interface
- **JavaScript** for client-side interactivity

---

### Project Structure
The overall structure of the project is as follows:

- `app.py`  
  The main Flask application file that defines routes and handles requests.

- `helpers.py`  
  Contains helper functions used for calculating lesson importance and distributing study time.

- `database.py`  
  Manages the SQLite database, including table creation and storing/retrieving study plans.

- `templates/`  
  Contains HTML templates such as:
  - `layout.html`
  - `index.html`
  - `form.html`
  - `result.html`
  - `history.html`
  - `faq.html`

- `static/`  
  Contains CSS and JavaScript files.

---

### History Feature
To make the application more useful, SQLite is used to store previously generated study plans. Users can view their recent plans on the History page. This feature was implemented without an account system to keep the application simple and user-friendly.

---

### Design Decisions
Several design decisions were made during development. Flask was chosen for its simplicity and suitability for small to medium-sized web applications. SQLite was selected because it is lightweight and easy to integrate without requiring a separate database server.

The application focuses on clarity, usability, and realistic planning rather than complex visual design. The main objective was to ensure that the generated study plans are practical and easy to understand.

---

### Conclusion
Study Planner is a practical tool that shows how backend logic, databases, and frontend interfaces can work together to solve a real-world problem. This project was created as the final project for CS50x and reflects the concepts learned throughout the course, including Python, Flask, SQL, and web development basics.
