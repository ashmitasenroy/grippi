# Grippi - Full-Stack Campaign Analytics Dashboard

Grippi is a full-stack web application designed for the clear visualization and tracking of marketing campaign performance. It features a React frontend and a Python/FastAPI backend that serves data from a relational SQLite database.

<!-- 
**ACTION REQUIRED:**
1. Take a screenshot of your Grippi dashboard.
2. Create an `assets` folder in this repository.
3. Save the image as `grippi-screenshot.png` inside the `assets` folder.
4. Uncomment the line below. 
-->
<!-- ![Grippi Dashboard Screenshot](./assets/grippi-screenshot.png) -->

---

### 🎯 Project Purpose & Motivation

The goal of Grippi was to build a full-stack application that solves a real-world problem: consolidating scattered campaign data. More importantly, it was an exercise in designing a robust backend system with a clear, relational database schema and a well-defined RESTful API to serve that data.

---

### 🛠️ Tech Stack

| Area      | Technology                                           |
| :-------- | :--------------------------------------------------- |
| **Frontend**  | React.js, CSS3, Axios                                |
| **Backend**   | Python, FastAPI                                      |
| **Database**  | **SQLite** (for its lightweight, serverless nature)  |
| **API Testing**   | Postman                                      |

---

### 🏛️ Database Design & Schema

The core of Grippi is its relational database. I chose **SQLite** because it's a lightweight, file-based, and serverless solution, perfect for self-contained applications and rapid development without requiring a separate database server. The schema is designed for data integrity and efficient querying.

#### **Entity-Relationship Diagram (ERD)**

This diagram illustrates the relationships between the database tables. GitHub will automatically render this Mermaid.js code.

```mermaid
erDiagram
    CAMPAIGNS {
        int id PK "Campaign ID"
        varchar name "Unique Campaign Name"
        varchar status "'active', 'paused', 'completed'"
        float budget "Total allocated budget"
    }

    PERFORMANCE_DATA {
        int id PK "Data Point ID"
        int campaign_id FK "Foreign Key to Campaigns"
        date record_date "Date of data record"
        int clicks "Daily click count"
        int impressions "Daily impression count"
        int conversions "Daily conversion count"
    }

    CAMPAIGNS ||--o{ PERFORMANCE_DATA : "has"
