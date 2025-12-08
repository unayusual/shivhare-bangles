# Shivhare Bangles Store

A Django-based e-commerce web application for selling bangles with built-in analytics tracking.

## Features

- **Product Management**: Display bangles with images, descriptions, and pricing
- **Customer Inquiries**: Allow customers to inquire about products via contact form
- **Analytics Dashboard**: Track page visits and product interactions
- **Admin Panel**: Manage products, inquiries, and view analytics
- **Authentication**: Built-in user authentication and password reset functionality
- **Mobile Responsive**: Works on all devices

## Tech Stack

- **Backend**: Django 5.2
- **Database**: PostgreSQL (via NeonDB) / SQLite (for local development)
- **Hosting**: Vercel
- **Static Files**: WhiteNoise
- **Dependencies**: See `requirements.txt`

## Local Development Setup

### Prerequisites

- Python 3.12+
- pip
- Virtual environment (recommended)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/unayusual/shivhare-bangles.git
   cd shivhare-bangles
   ```

2. **Create and activate virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   ```bash
   cp .env.example .env
   # Edit .env with your settings (SECRET_KEY, DEBUG=True for local dev)
   ```

5. **Run migrations**
   ```bash
   python manage.py migrate
   ```

6. **Create a superuser (admin)**
   ```bash
   python manage.py createsuperuser
   ```

7. **Collect static files**
   ```bash
   python manage.py collectstatic --no-input
   ```

8. **Run the development server**
   ```bash
   python manage.py runserver
   ```

9. **Access the application**
   - Frontend: http://127.0.0.1:8000/
   - Admin Panel: http://127.0.0.1:8000/admin/
   - Analytics: http://127.0.0.1:8000/analytics/

## Deployment to Vercel with NeonDB

### Step 1: Set up NeonDB

1. Go to [NeonDB Console](https://console.neon.tech/)
2. Create a new project
3. Copy your PostgreSQL connection string (it looks like):
   ```
   postgresql://user:password@ep-xxx-xxx.region.aws.neon.tech/neondb?sslmode=require
   ```

### Step 2: Deploy to Vercel

1. **Install Vercel CLI** (optional)
   ```bash
   npm install -g vercel
   ```

2. **Push your code to GitHub**
   ```bash
   git push origin main
   ```

3. **Deploy via Vercel Dashboard**
   - Go to [Vercel](https://vercel.com/)
   - Click "New Project"
   - Import your GitHub repository
   - Configure environment variables:
     - `SECRET_KEY`: Generate a strong random string (you can use: `python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"`)
     - `DEBUG`: Set to `False`
     - `DATABASE_URL`: Your NeonDB connection string
   - Deploy!

4. **Or deploy via CLI**
   ```bash
   vercel --prod
   ```

### Step 3: Run Migrations on Vercel

After deployment, migrations will be run automatically via the `build.sh` script during the build process. The build script includes:
```bash
python manage.py collectstatic --no-input
python manage.py migrate
```

### Step 4: Create Admin User on Production

You'll need to create a superuser for production. Since Vercel is serverless, the recommended approach is:

1. **Temporarily connect locally to NeonDB** (safest method):
   - Create a `.env.production` file with your production DATABASE_URL
   - Load it and run: `python manage.py createsuperuser`
   - Delete the `.env.production` file immediately after
   
2. **Alternative**: Create a custom management command to set up an initial admin user during deployment

**Security Note**: Never include database credentials in shell history or version control.

## Environment Variables

| Variable | Description | Required | Default |
|----------|-------------|----------|---------|
| `SECRET_KEY` | Django secret key for cryptographic signing | Yes | (dev key) |
| `DEBUG` | Enable/disable debug mode | No | `True` |
| `DATABASE_URL` | PostgreSQL connection string (for NeonDB) | Yes (production) | SQLite (local) |
| `ALLOWED_HOSTS` | Additional allowed hosts (comma-separated) | No | - |
| `CSRF_TRUSTED_ORIGINS` | Additional CSRF origins (comma-separated) | No | - |

## Project Structure

```
shivhare-bangles/
├── analytics/              # Analytics app (page visits, product interactions)
│   ├── models.py          # PageVisit, ProductInteraction models
│   ├── views.py           # Analytics dashboard
│   └── middleware.py      # Tracking middleware
├── store/                 # Main store app
│   ├── models.py          # Product, Inquiry models
│   ├── views.py           # Store views
│   └── urls.py            # Store URLs
├── shivhare_store/        # Project settings
│   ├── settings.py        # Django settings
│   ├── urls.py            # Main URL configuration
│   └── wsgi.py            # WSGI configuration
├── templates/             # HTML templates
├── static/                # Static files (CSS, JS, images)
├── staticfiles/           # Collected static files (auto-generated)
├── requirements.txt       # Python dependencies
├── vercel.json           # Vercel deployment configuration
├── build.sh              # Build script for Vercel
└── manage.py             # Django management script
```

## Key Files for Deployment

- **`vercel.json`**: Configures Vercel deployment settings
- **`build.sh`**: Runs during deployment (install deps, collectstatic, migrate)
- **`requirements.txt`**: Python dependencies
- **`shivhare_store/wsgi.py`**: WSGI application entry point
- **`.env.example`**: Template for environment variables

## Security Features

When `DEBUG=False` (production), the following security features are enabled:
- HTTPS redirect
- Secure cookies (SESSION and CSRF)
- HTTP Strict Transport Security (HSTS)
- XSS filtering
- Content type sniffing protection
- Clickjacking protection (X-Frame-Options)

## Troubleshooting

### Static files not loading on Vercel
- Ensure `python manage.py collectstatic` runs in `build.sh`
- Check that `STATIC_ROOT` is properly set in settings
- WhiteNoise middleware is properly configured

### Database connection issues
- Verify your `DATABASE_URL` is correct
- Ensure NeonDB allows connections from Vercel's IP ranges
- Check that `psycopg2-binary` is in requirements.txt

### 500 Internal Server Error
- Check Vercel function logs
- Verify environment variables are set correctly
- Ensure `SECRET_KEY` is set and `DEBUG=False`

## License

This project is private and proprietary.

## Support

For issues or questions, please contact the development team or create an issue in the repository.

## Contributing

This is a private project. Contributions are welcome from team members only.
