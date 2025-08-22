# Office Management System

## Overview
A simple, responsive web application for managing employee data. This system allows you to add, view, filter, and remove employees efficiently through a modern interface built with **HTML5** and **Bootstrap 5**.

---

## Features

- **Add Employee:** Easily add new employees with details like name, department, role, salary, phone, and hire date.
- **View Employees:** See all employees in a sortable, responsive table.
- **Filter Employees:** Search employees by name, department, or role to quickly find specific records.
- **Remove Employee:** Delete employees from the system via a convenient dropdown interface.
- **Clean UI:** Bootstrap 5 styling ensures the app is mobile-friendly and visually appealing.

---

## Technologies Used

- **HTML5** for markup  
- **Bootstrap 5** for responsive styling and components  
- **Bootstrap Icons** for UI icons  
- **Server-Side Templating** (e.g., Django, Flask, or similar)  

---

## Project Structure

- `index.html` / Homepage — Main dashboard with navigation buttons  
- `add_employee.html` — Form to add employees  
- `employee_list.html` — Table showing all employees  
- `filter_employee.html` — Form and table for filtering employees  
- `remove_employee.html` — Dropdown interface to remove employees  

---

## Setup Instructions

1. Clone the repository.
2. Set up your backend server (e.g., Django or Flask) to serve these pages and handle form submissions.
3. Ensure you have Bootstrap and Bootstrap Icons included (CDN links are already in HTML).
4. Run the server and navigate to the homepage.
5. Use the navigation buttons to access different functionalities.

---

## Backend Notes

- Protect POST routes with CSRF tokens.
- Provide backend context variables such as:
  - `emps` — List of employees  
  - `departments` — List of departments for dropdowns  
  - `roles` — List of roles for dropdowns  
- Implement backend routes to add, list, filter, and remove employees.

#License
This project is open source. You are free to use, modify, and distribute it.

