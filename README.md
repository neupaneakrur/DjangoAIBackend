# Technology Channel AI

A Django-based AI completion API with PostgreSQL database storage for prompts and responses.

## Features

- 🤖 AI-powered text completions using OpenAI API
- 🗄️ PostgreSQL database storage for all prompts and responses
- 📊 Admin interface to view and manage completions
- ⚡ RESTful API endpoints
- 📈 Request metadata tracking (IP, user agent, processing time)
- 🎨 Beautiful homepage with status indicator

## Setup Instructions

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. PostgreSQL Setup

#### Option A: Using Existing PostgreSQL Installation

1. **Update Database Settings**
   Edit `technologychannelai/settings.py` and update the DATABASES section:
   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.postgresql',
           'NAME': 'your_database_name',
           'USER': 'your_postgres_username',
           'PASSWORD': 'your_postgres_password',
           'HOST': 'localhost',
           'PORT': '5432',
       }
   }
   ```

#### Option B: Create New PostgreSQL Database

1. **Install PostgreSQL** (if not already installed)
   - Windows: Download from https://www.postgresql.org/download/windows/
   - Linux: `sudo apt-get install postgresql postgresql-contrib`
   - Mac: `brew install postgresql`

2. **Start PostgreSQL Service**
   - Windows: Check Services app for PostgreSQL service
   - Linux/Mac: `sudo systemctl start postgresql`

3. **Create Database and User**
   ```sql
   CREATE DATABASE technologychannelai_db;
   CREATE USER technologychannelai_user WITH PASSWORD 'your_secure_password';
   GRANT ALL PRIVILEGES ON DATABASE technologychannelai_db TO technologychannelai_user;
   ```

4. **Update Settings**
   Edit `technologychannelai/settings.py`:
   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.postgresql',
           'NAME': 'technologychannelai_db',
           'USER': 'technologychannelai_user',
           'PASSWORD': 'your_secure_password',
           'HOST': 'localhost',
           'PORT': '5432',
       }
   }
   ```

### 3. Environment Variables

Set your OpenAI API key as an environment variable:
```bash
# Windows
set OPENAI_API_KEY=your_openai_api_key_here

# Linux/Mac
export OPENAI_API_KEY=your_openai_api_key_here
```

### 4. Database Migration

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Create Superuser

```bash
python manage.py createsuperuser
```

### 6. Run the Server

```bash
python manage.py runserver
```

## API Endpoints

### 1. AI Completion
- **URL**: `/api/complete/`
- **Method**: POST
- **Body**: `{"prompt": "Your question here"}`
- **Response**: 
  ```json
  {
    "response": "AI generated response",
    "completion_id": 1,
    "processing_time": 2.345,
    "tokens_used": 150
  }
  ```

### 2. Completions List
- **URL**: `/api/completions/`
- **Method**: GET
- **Query Parameters**: 
  - `page` (default: 1)
  - `limit` (default: 10)
- **Response**: Paginated list of all stored completions

## Admin Interface

Access the admin interface at `/admin/` to:
- View all AI completions
- Filter by model, date, IP address
- Search through prompts and responses
- View processing times and metadata

## Database Schema

The `AICompletion` model stores:
- **prompt**: User's input text
- **response**: AI's generated response
- **model_used**: AI model version
- **temperature**: Generation temperature setting
- **tokens_used**: Number of tokens consumed
- **processing_time**: Request processing time in seconds
- **ip_address**: Client IP address
- **user_agent**: Client user agent string
- **created_at**: Timestamp of creation
- **updated_at**: Timestamp of last update

## Troubleshooting

### PostgreSQL Connection Issues

1. **Check if PostgreSQL is running**
   ```bash
   # Windows
   net start postgresql-x64-15
   
   # Linux/Mac
   sudo systemctl status postgresql
   ```

2. **Verify credentials**
   - Check username and password in settings.py
   - Ensure database exists
   - Verify user has proper permissions

3. **Test connection**
   ```bash
   psql -h localhost -U your_username -d your_database
   ```

### Common Issues

- **"password authentication failed"**: Check PostgreSQL password in settings.py
- **"database does not exist"**: Create the database first
- **"permission denied"**: Grant proper privileges to the user

## Development

### Running Setup Script

```bash
python setup_postgres.py
```

This will display detailed setup instructions for PostgreSQL configuration.

### Testing the API

1. **Test AI Completion**
   ```bash
   curl -X POST http://localhost:8000/api/complete/ \
     -H "Content-Type: application/json" \
     -d '{"prompt": "What is artificial intelligence?"}'
   ```

2. **View Stored Completions**
   ```bash
   curl http://localhost:8000/api/completions/
   ```

## License

This project is open source and available under the MIT License. 