# Streamlit Deployment Guide

This project can be deployed easily via **Streamlit Community Cloud** (recommended, free, 1-click), **Docker**, or any cloud platform (Render, Railway, AWS, GCP, Azure, Hugging Face).

---

## 1. Streamlit Community Cloud (Recommended - Free & 1-Click)

The repository is pre-configured for native Streamlit Community Cloud deployment:
- Entry point: `app.py`
- Dependencies: `requirements.txt`
- Theme configuration: `.streamlit/config.toml`

### Steps to Deploy:
1. Push this repository to your GitHub account (e.g. `https://github.com/<your-username>/dwmlab`).
2. Visit **[share.streamlit.io](https://share.streamlit.io/)** and sign in with GitHub.
3. Click **"New app"**.
4. Configure the settings:
   - **Repository**: `<your-username>/dwmlab`
   - **Branch**: `main`
   - **Main file path**: `app.py`
5. Click **"Deploy!"**.
6. Streamlit Cloud will automatically build the environment and provide a public live URL (e.g. `https://<your-app-name>.streamlit.app`).

---

## 2. Docker Deployment (Local or Cloud Containers)

A [Dockerfile](file:///c:/Users/Ruhaan/OneDrive/Desktop/dwm%20lab%20project/Dockerfile) is provided.

### Build and Run Locally:
```bash
# 1. Build Docker image
docker build -t pizza-mdw-app .

# 2. Run the container
docker run -p 8501:8501 pizza-mdw-app
```
Access the application at `http://localhost:8501`.

---

## 3. Cloud Platforms (Render / Railway / Fly.io)

### Render (Web Service):
1. Connect your GitHub repository to [Render.com](https://render.com/).
2. Select **Web Service** $\rightarrow$ **Docker** (or Python environment).
3. If using Python:
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `streamlit run app.py --server.port $PORT --server.address 0.0.0.0`
4. Deploy.

### Railway / Fly.io:
Railway and Fly.io automatically detect the [Dockerfile](file:///c:/Users/Ruhaan/OneDrive/Desktop/dwm%20lab%20project/Dockerfile) in the root and build it without extra configuration.

---

## 4. Hugging Face Spaces

1. Create a new Space on [Hugging Face](https://huggingface.co/spaces).
2. Choose **Streamlit** as the Space SDK.
3. Push the files to the Space repository. Hugging Face will automatically execute `app.py`.
