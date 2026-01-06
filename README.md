# GemstoneLux - Premium Gemstone Website

A high-end, responsive Django website for showcasing and selling certified gemstones.

## 🚀 Features
- **Premium UI/UX**: Gold & Charcoal color scheme, Playfair Display fonts, smooth animations.
- **Product Catalog**: Advanced filtering (Category, Origin, Price), Sorting, and Search.
- **Gemstone Details**: High-res images (with zoom hover), detailed specs (Carat, Treatment, Certification).
- **Inquiry System**: WhatsApp integration for direct sales and a contact form for leads.
- **Admin Panel**: customized for easy inventory management with image previews.

## 🛠️ Tech Stack
- **Framework**: Django 5
- **Database**: SQLite (Development)
- **Frontend**: Bootstrap 5, Custom CSS
- **Icons**: FontAwesome

## 📦 Setup Instructions

1.  **Clone the repository** (if applicable) or navigate to the project folder.

2.  **Install Dependencies**:
    ```bash
    pip install django pillow
    ```

3.  **Run Migrations**:
    ```bash
    python manage.py migrate
    ```

4.  **Create Superuser** (to access Admin panel):
    ```bash
    python manage.py createsuperuser
    ```

5.  **Run Server**:
    ```bash
    python manage.py runserver
    ```

6.  **Access the Website**:
    - **Home**: `http://127.0.0.1:8000/`
    - **Admin**: `http://127.0.0.1:8000/admin/`

## 💎 Managing Gemstones & Images
- Login to the Admin panel.
- Go to **Stores > Gemstones**.
- Add new gemstones.
- **Note**: Ensure you have some images to upload to see the UI in full effect.

## 📄 Pages
- **Home**: Hero section, Trusted badges, Featured Collection.
- **Collection**: Full catalog with sidebar filters.
- **Detail**: Single product view with specs and inquiry buttons.
- **About**: Brand story.
- **Contact**: Inquiry form.

---
*Created for GemstoneLux Business*
