# Phone-first Flask Portfolio Template

## Included

- Mobile-first portfolio homepage
- Long-scroll sections with CSS 3D motion studies
- Flask templates in `templates/`
- CSS and JavaScript in `static/`
- Environment-based admin login
- Central Firebase configuration in `config.py`
- Starter admin dashboard

## Local setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
python app.py
```

Open:

- Portfolio: `http://localhost:5000/`
- Admin login: `http://localhost:5000/admin/login`

## Hosting variables

Add the values from `.env.example` to Render, Railway, or your hosting provider.
Do not commit `.env`, real admin credentials, or Firebase private service-account
credentials to GitHub.

## Next integration step

The starter dashboard is intentionally small. The production version can connect
the profile, projects, assets, navigation, and conversations screens to Firestore
with real-time listeners and protected server-side write routes.