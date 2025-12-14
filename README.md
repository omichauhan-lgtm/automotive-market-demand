# AutoSight - AI-Powered Automotive Analytics SaaS

## ⭐ Overview
“This project is based on analytical work performed during my Data Analyst Internship at Rajputana Vehicles Pvt. Ltd.”

## 🏗️ Architecture
- **Backend**: FastAPI (Python), SQLAlchemy, PostgreSQL (or SQLite for dev), Redis.
- **Frontend**: React (Vite), TailwindCSS, Recharts.
- **Infrastructure**: Docker Compose.

## 🚀 Getting Started

### Prerequisites
- Docker & Docker Compose
- Node.js & npm
- Python 3.9+

### Quick Start (Docker)
1. **Run the full stack**:
   ```bash
   docker-compose up --build
   ```
2. **Access the App**:
   - Frontend: `http://localhost:3000`
   - Backend API: `http://localhost:8000/docs`

### Manual Setup (Development)

#### Backend
1. Navigate to `backend/`:
   ```bash
   cd backend
   pip install -r requirements.txt
   ```
2. Run the server:
   ```bash
   uvicorn main:app --reload
   ```

#### Frontend
1. Navigate to `frontend/`:
   ```bash
   cd frontend
   npm install
   npm run dev
   ```

## 🔑 Key Features
- **Multi-Tenancy**: Secure login and tenant isolation.
- **Data Ingestion**: Upload CSV datasets for analysis.
- **Analytics Dashboard**: Real-time KPIs, Customer Segmentation (K-Means), and Demand Forecasting.
- **AI Recommendations**: Automated insights based on uploaded data.

## 📂 Project Structure
```
automotive-market-analysis/
 ├── 📂 backend/            # FastAPI Application
 │   ├── 📂 routers/        # API Endpoints (Auth, Tenants, Analytics)
 │   ├── models.py          # Database Models
 │   ├── schemas.py         # Pydantic Schemas
 │   └── main.py            # Entry point
 ├── 📂 frontend/           # React Application
 │   ├── 📂 src/
 │   │   ├── 📂 pages/      # Login, Dashboard, Upload
 │   │   └── App.tsx        # Routing
 ├── docker-compose.yml     # Container Orchestration
 └── README.md              # Documentation
```
