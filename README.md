# Full Stack App Setup Instructions

This README provides step-by-step instructions to set up and run the full-stack application, including both the React frontend and the API backend. Follow these steps to get started:

---

## Prerequisites
Ensure you have the following installed on your system:

- **Node.js** (v16 or higher recommended) 
  Download from [Node.js Official Website](https://nodejs.org/).
- **Python** (v3.8 or higher recommended)
  Download from [Python Official Website](https://www.python.org/).
- **npm** (comes with Node.js) or **yarn** (optional)
- A database tool (e.g., MySQL or SQLite) for setting up the database

---

## Steps to Set Up the Frontend (React App)

### 1. Create a New React App
1. Open your terminal and run the following command to create a new React app:
   ```bash
   npx create-react-app my-react-app
   ```
2. Navigate to the newly created app's directory:
   ```bash
   cd my-react-app
   ```

### 2. Replace Files
1. Replace the default **`public`** and **`src`** folders with the ones provided in this project:
   - Copy the `public` folder from this project and paste it into your app's root directory.
   - Copy the `src` folder from this project and paste it into your app's root directory.

2. Overwrite any existing files if prompted.

### 3. Install Dependencies
1. Copy the `package.json` and `package-lock.json` files from this project and replace the ones in your app's root directory.
2. Install the required dependencies:
   ```bash
   npm install
   ```
   This command will install all the dependencies specified in the `package.json` file.

---

## Running the Frontend Application
1. Start the development server:
   ```bash
   npm start
   ```
2. Open your browser and navigate to:
   ```
   http://localhost:3000
   ```

---

## Steps to Set Up the Backend (API)

### 1. Navigate to the API Directory
1. Copy the `api` folder from this project to your desired location.
2. Navigate to the `api` folder:
   ```bash
   cd api
   ```

### 2. Install Python Dependencies
1. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```
2. Install the required Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```
   Ensure the `requirements.txt` includes the following:
   ```
   fastapi
   uvicorn
   sqlalchemy
   pillow
   tensorflow
   numpy
   ```

### 3. Set Up the Database
1. Use the provided `sql.sql` file to set up your database:
   - Open your database tool (e.g., MySQL Workbench, SQLite, etc.).
   - Execute the SQL commands in `sql.sql` to create the required tables and schema.

### 4. Run the Backend Server
1. Start the API server by running the `main.py` file:
   ```bash
   python main.py
   ```
2. The API will be available at:
   ```
   http://localhost:8000
   ```

---

## Notes
- For frontend-backend integration, ensure the API URL in the React app matches your backend server URL (e.g., `http://localhost:5000`).
- If you encounter any issues, check for missing dependencies or environment variables.

---

## Project Structure
After setting up both frontend and backend, your project directory should look like this:
```
project_root/
├── api/
│   ├── main.py
│   ├── sql.sql
│   ├── requirements.txt
│   ├── ...
├── my-react-app/
│   ├── node_modules/
│   ├── public/
│   │   ├── index.html
│   │   ├── ...
│   ├── src/
│   │   ├── App.js
│   │   ├── index.js
│   │   ├── ...
│   ├── package.json
│   ├── package-lock.json
│   ├── ...
```
---

Enjoy building your full-stack application!
