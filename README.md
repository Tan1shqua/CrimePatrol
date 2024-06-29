# CrimePatrol - Real-Time Crime Reporting Application

Welcome to **CrimePatrol**, an innovative real-time crime reporting application built with the power of Django and modern web technologies. CrimePatrol is designed to empower citizens, enhance public safety, and streamline the crime reporting process. Dive into the technical intricacies of this project and learn how you can contribute to making our communities safer.

## Table of Contents
1. [Introduction](#introduction)
2. [Features](#features)
3. [Architecture](#architecture)
4. [Setup and Installation](#setup-and-installation)
5. [User Management and Access Control](#user-management-and-access-control)
6. [Technologies Used](#technologies-used)
7. [API Endpoints](#api-endpoints)
8. [Contributing](#contributing)
9. [License](#license)

## Introduction
CrimePatrol is a full-stack web application that provides a platform for citizens to report crimes in real-time. Leveraging the Django framework, the app offers a robust backend for managing reports, user authentication, and geospatial data. The frontend integrates Leaflet.js for interactive maps, allowing users to visualize crime data dynamically.

## Features
- **Real-Time Crime Reporting**: Citizens can submit detailed crime reports with descriptions, locations, and multimedia attachments.
- **Interactive Maps**: View reported crimes on an interactive map with clustering for better data visualization.
- **User Roles and Permissions**: Distinct roles for citizens, police, and admins ensure secure and appropriate access.
- **Secure Authentication**: User authentication through Django's built-in system and OAuth integration.
- **Media Uploads**: Attach images or videos to reports to provide more context and evidence.
- **Search and Filtering**: Easily search and filter reports based on crime type, location, and date.

## Architecture
CrimePatrol is architected to ensure scalability, security, and ease of use:

- **Backend**: Django powers the backend, utilizing Django Rest Framework (DRF) for creating RESTful APIs and Channels for real-time features.
- **Frontend**: HTML, CSS, and JavaScript (with Leaflet.js) provide a responsive and interactive user interface.
- **Database**: PostgreSQL is used for its robustness and support for geospatial data.
- **Real-Time Updates**: WebSockets and Channels allow for real-time updates and notifications.

### Workflow
1. **User Authentication**: Users register and log in using secure authentication methods.
2. **Report Submission**: Citizens report crimes with detailed descriptions and geolocation data.
3. **Data Storage**: Reports are stored in a PostgreSQL database, leveraging Django's ORM for efficient data handling.
4. **Map Visualization**: Reports are visualized on an interactive map using Leaflet.js and marker clustering.
5. **Admin Management**: Admins manage reports, users, and overall system settings through a secure admin interface.

## Setup and Installation
Follow these steps to set up CrimePatrol on your local machine:

### Prerequisites
- Python 3.8+
- PostgreSQL
- Node.js (for frontend dependencies)

### Installation
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/CrimePatrol.git
   cd CrimePatrol
   ```

2. **Create and Activate Virtual Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure PostgreSQL**:
   - Create a PostgreSQL database and user.
   - Update `settings.py` with your database credentials:
     ```python
     DATABASES = {
         'default': {
             'ENGINE': 'django.db.backends.postgresql',
             'NAME': 'CrimePatrol_db',
             'USER': 'your_db_user',
             'PASSWORD': 'your_db_password',
             'HOST': 'localhost',
             'PORT': '5432',
         }
     }
     ```

5. **Run Migrations**:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Create a Superuser**:
   ```bash
   python manage.py createsuperuser
   ```

7. **Run the Development Server**:
   ```bash
   python manage.py runserver
   ```

8. **Access the Application**:
   Open your browser and go to `http://localhost:8000`.

## User Management and Access Control
CrimePatrol incorporates a robust user management system with clear access controls:

- **Roles**: Users are categorized as Citizens, Police, or Admins.
- **Authentication**: Utilizes Django's authentication along with OAuth for social logins.
- **Authorization**: Implements Django's permission system to restrict access based on user roles.
- **Profile Management**: Users can update their profiles and manage their account settings.

## Technologies Used
- **Django**: High-level Python web framework.
- **Django Rest Framework**: Toolkit for building Web APIs.
- **Django Channels**: Asynchronous support for Django.
- **PostgreSQL**: Advanced relational database with geospatial support.
- **Leaflet.js**: JavaScript library for interactive maps.
- **HTML/CSS/JavaScript**: Core web technologies for frontend development.

## API Endpoints
CrimePatrol exposes a set of RESTful APIs for various functionalities:

- **User Authentication**: `/api/auth/`
- **Crime Reports**: `/api/reports/`
- **User Management**: `/api/users/`

Refer to the API documentation for detailed endpoint information and usage.

## Contributing
We welcome contributions from the community! To contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -m 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Create a pull request.

## License
CrimePatrol is licensed under the MIT License. See `LICENSE` for more information.

---

Thank you for checking out CrimePatrol! Together, we can make our communities safer and more connected. Happy coding!


![Screenshot 2024-06-29 162420](https://github.com/davesohamm/CrimePetrol/assets/127236862/3536aefc-4411-4c57-b5f8-5d5867b31542)
![Screenshot 2024-06-29 162434](https://github.com/davesohamm/CrimePetrol/assets/127236862/fbb14311-92cc-4c1e-b7a3-7a5ff9f9846c)
![Screenshot 2024-06-29 162451](https://github.com/davesohamm/CrimePetrol/assets/127236862/277baf26-5ac7-4d79-a8e1-3b661575c0e8)
![Screenshot 2024-06-29 164007](https://github.com/Tan1shqua/CrimePatrol/assets/127236862/f32c3970-7db3-435a-a60c-82cbac269318)
