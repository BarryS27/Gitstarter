# Gitstarter
#### Video Demo:  <https://youtu.be/-E6hMQy048A>

![Python](https://img.shields.io/badge/Python-3.13-blue?style=flat&logo=python)
![Flask](https://img.shields.io/badge/Flask-Web%20Framework-green?style=flat&logo=flask)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5.3-purple?style=flat&logo=bootstrap)

## 📌 Description

Gitstarter is a web application designed to lower the barrier of entry for open-source contributions. It serves as a specialized search tool that aggregates beginner-friendly GitHub issues, helping students and new developers find projects they can actually contribute to.

The primary goal of this project is to solve the "analysis paralysis" often faced by beginners. While GitHub hosts millions of repositories, finding an issue that is active, unassigned, and explicitly labeled for beginners (e.g., "good first issue") can be time-consuming using the native search interface. GitStarter automates this filtering process, providing a curated list of opportunities in real-time.

---

## 📂 Project Structure

The project is built using **Python (Flask)** for the backend and **HTML/CSS (Bootstrap)** for the frontend. It follows a modular structure to ensure code maintainability.

### 1. `app.py`
This is the main application entry point. It initializes the Flask instance and defines the application's routes.
* **Route Handling**: The application uses a single route (`/`) that supports both `GET` and `POST` methods.
    * `GET`: Renders the initial search interface.
    * `POST`: Captures the user's input (programming language), calls the helper function to fetch data, and renders the results page.
* **Controller Logic**: `app.py` acts strictly as a controller. It receives user input and passes it to the model layer (`helpers.py`) without containing complex business logic itself.

### 2. `helpers.py`
This module encapsulates all interactions with the GitHub API. Separating this logic from `app.py` allows for better testing and cleaner code.
* **`search_issues(lang)`**: This function constructs a parameterized query string for the GitHub Search API.
* **API Interaction**: It uses the `requests` library to fetch data. The function handles HTTP responses and parses the JSON output to extract only relevant fields: issue title, repository URL, and issue URL.
* **Error Handling**: A `try-except` block is implemented to gracefully handle potential API failures or network connectivity issues, ensuring the application remains stable.

### 3. `templates/`
The frontend is built using Jinja2 templating to render dynamic content.
* **`layout.html`**: Defines the global structure of the application, including the navigation bar and footer. It loads external resources such as the Bootstrap CSS framework.
* **`index.html`**: Extends `layout.html`. It contains the search form and the logic loop (`{% for issue in results %}`) to display search results. It also includes conditional rendering to handle states where no issues are found.

---

## 🛠️ Design Choices

### API Filtering Strategy
One of the key challenges was determining the optimal set of filters for the GitHub API.
* **Initial Approach**: I initially attempted to filter for issues with strictly zero comments (`comments:0`) and no assignees (`no:assignee`).
* **The Problem**: While this ensured high availability, it often resulted in zero search results for less popular programming languages, creating a poor user experience.
* **The Solution**: I refined the logic in `helpers.py` to prioritize the `good first issue` label and the `state:open` status. This provides a balanced result set—ensuring the issues are beginner-friendly while maintaining a sufficient quantity of results for the user to explore.

### Frontend Architecture
I utilized **Bootstrap 5** for the user interface. As this is primarily a backend-focused project, relying on a CSS framework allowed me to ensure responsiveness across mobile and desktop devices without spending excessive time on custom styling. The use of **Jinja2** templates was essential for rendering data server-side, which kept the frontend logic simple and avoided the complexity of a separate JavaScript frontend framework.

### Future Improvements
Currently, the application is stateless. In future iterations, I plan to integrate a **SQLite database** to allow users to save or "bookmark" specific issues. This would involve implementing a user authentication system (Login/Register) to manage personal lists.
