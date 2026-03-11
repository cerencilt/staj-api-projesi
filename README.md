# Token Auth API Project

This is a backend API project developed with Python and Django.

## Project Setup

1. **Clone the repository:**
   `git clone https://github.com/cerencilt/token-auth-api.git`

2. **Create and activate virtual environment:**
   `python -m venv venv`
   `source venv/bin/activate` # For Windows: venv\Scripts\activate

3. **Install requirements:**
   `pip install -r requirements.txt`

4. **Run the project:**
   `python manage.py runserver`

5. **Setup Environment Variables**
Copy the sample environment file and update the values with your own:

```powershell
copy .env.sample .env 
Open the .env file and replace your-secret-key-goes-here with your actual Django secret key. 
   
   ## Running Tests

The project includes automated tests to verify authentication and API endpoints. To run the tests, use the following command:
`python manage.py test` 
