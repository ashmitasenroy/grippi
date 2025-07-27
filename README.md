# Grippi - Full-Stack Campaign Analytics Dashboard

Grippi is a full-stack web application designed to help marketers track and visualize the performance of their campaigns. It provides a clean, intuitive dashboard to monitor key metrics, offering insights at a glance.

<!-- Add a link to your live demo if you have one -->
<!-- [![Live Demo](https://img.shields.io/badge/Live-Demo-brightgreen?style=for-the-badge)](https://your-grippi-demo-link.com/) -->

<!-- Add a screenshot of your dashboard here! It makes a huge difference. -->
![Grippi Dashboard Screenshot](./assets/grippi-screenshot.png)

---

### 🎯 Project Purpose & Motivation

In many scenarios, campaign data is scattered across different platforms, making it difficult to get a clear, consolidated view of performance. I built Grippi to solve this problem by creating a single source of truth—a user-friendly dashboard that fetches data from a central backend service and presents it in a clean, visual format.

---

### 🛠️ Tech Stack

This project is a full-stack application with a React frontend and a Python backend.

#### **Frontend:**
*   **Framework:** React.js
*   **Styling:** CSS / Material-UI *(<-- Replace with what you used)*
*   **Data Fetching:** Axios / Fetch API

#### **Backend:**
*   **Framework:** Python with FastAPI
*   **Database:** SQLite / MySQL *(<-- Replace with what you used)*

---

### ✨ Features

- **Data Visualization:** Clean charts and graphs to visualize key campaign metrics like clicks, conversions, and budget.
- **Campaign Overview:** A central table displaying all campaigns with their current status and performance data.
- **Responsive Design:** A mobile-friendly layout that ensures the dashboard is usable on any device.
- **RESTful API:** A well-defined backend API to serve campaign data to the frontend.

---

### 🚀 Running Locally

To run this project on your local machine, you will need to run both the frontend (this repository) and the backend service.

1.  **Clone the repository:**
    ```sh
    git clone https://github.com/ashmitasenroy/grippi.git
    ```

2.  **Navigate into the project directory:**
    ```sh
    cd grippi
    ```

3.  **Install dependencies:**
    ```sh
    npm install
    ```

4.  **Set up environment variables:**
    The frontend needs to know the URL of your backend API. Create a new file in the root of the project named `.env.local` and add the following line:
    ```
    REACT_APP_API_URL=http://localhost:8000
    ```
    *(Note: Adjust the port if your backend runs on a different one.)*

5.  **Start the development server:**
    ```sh
    npm start
    ```
    The application will open automatically at `http://localhost:3000`.

---

### 🔌 API Reference

*(This is where the excellent API Reference section you already wrote should go. I've included it below to make this a complete template.)*

This section documents the core endpoints for the Grippi backend service.

---

#### Get All Campaigns

*   `GET /api/campaigns`

Fetches a summary of all marketing campaigns.

**Query Parameters:**

| Parameter | Type   | Description                                                        |
| :-------- | :----- | :----------------------------------------------------------------- |
| `status`  | String | **Optional**. Filters campaigns by status (e.g., 'active', 'completed'). |

**Example Response (`200 OK`):**
```json
[
  {
    "id": 1,
    "name": "Summer Sale 2024",
    "status": "active",
    "budget": 5000
  },
  {
    "id": 2,
    "name": "Winter Launch",
    "status": "completed",
    "budget": 7500
  }
]
