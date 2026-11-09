from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI(
    title="SPORT HUB",
    description="Farg'ona yoshlar sport platformasi",
    version="1.0.0"
)

@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <!DOCTYPE html>
    <html lang="uz">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>SPORT HUB</title>
        <style>
            body {
                margin: 0;
                font-family: Arial, sans-serif;
                background: #101827;
                color: white;
                text-align: center;
            }
            header {
                padding: 25px;
                background: #17243a;
            }
            h1 { color: #35d07f; font-size: 42px; }
            main { padding: 70px 20px; }
            p { color: #cbd5e1; font-size: 18px; }
            .button {
                display: inline-block;
                background: #35d07f;
                color: #101827;
                padding: 14px 28px;
                border-radius: 8px;
                text-decoration: none;
                font-weight: bold;
            }
        </style>
    </head>
    <body>
        <header><h2>SPORT HUB</h2></header>
        <main>
            <h1>Sport — bizning kelajagimiz!</h1>
            <p>Farg'ona yoshlari uchun yagona sport platformasi.</p>
            <p>Musobaqalar, jamoalar va yangi imkoniyatlar bir joyda.</p>
            <a class="button" href="/docs">Platformani ko'rish</a>
        </main>
    </body>
    </html>
    """

@app.get("/health")
def health():
    return {"status": "ok", "project": "SPORT HUB"}

import os
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from supabase import create_client

app = FastAPI(
    title="SPORT HUB",
    description="Farg'ona yoshlar sport platformasi",
    version="1.0.0"
)

supabase = create_client(
    os.getenv("SUPABASE_URL"),
    os.getenv("SUPABASE_KEY")
)

@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <!DOCTYPE html>
    <html lang="uz">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>SPORT HUB</title>
        <style>
            body {
                margin: 0;
                font-family: Arial, sans-serif;
                background: #101827;
                color: white;
                text-align: center;
            }
            header {
                padding: 25px;
                background: #17243a;
            }
            h1 { color: #35d07f; font-size: 42px; }
            main { padding: 70px 20px; }
            p { color: #cbd5e1; font-size: 18px; }
            .button {
                display: inline-block;
                background: #35d07f;
                color: #101827;
                padding: 14px 28px;
                border-radius: 8px;
                text-decoration: none;
                font-weight: bold;
            }
        </style>
    </head>
    <body>
        <header><h2>SPORT HUB</h2></header>
        <main>
            <h1>Sport — bizning kelajagimiz!</h1>
            <p>Farg'ona yoshlari uchun yagona sport platformasi.</p>
            <p>Musobaqalar, jamoalar va yangi imkoniyatlar bir joyda.</p>
            <a class="button" href="/docs">Platformani ko'rish</a>
        </main>
    </body>
    </html>
    """

@app.get("/health")
def health():
    return {"status": "ok", "project": "SPORT HUB"}

@app.get("/database-test")
def database_test():
    try:
        supabase.table("users").select("id").limit(1).execute()
        return {"status": "connected", "database": "SPORT HUB"}
    except Exception:
        return {"status": "error", "message": "Database connection failed"}
@app.get("/database-test")
def database_test():
    ...
