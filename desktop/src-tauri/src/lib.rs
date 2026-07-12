// Prevents additional console window on Windows in release
#![cfg_attr(not(debug_assertions), windows_subsystem = "windows")]

use serde::{Deserialize, Serialize};

#[derive(Debug, Serialize, Deserialize)]
struct Message {
    role: String,
    content: String,
}

#[tauri::command]
async fn get_backend_url() -> String {
    // Desktop app connects to backend on localhost:8000
    // In production, this could be configurable
    std::env::var("BACKEND_URL")
        .unwrap_or_else(|_| "http://localhost:8000".to_string())
}

#[cfg_attr(mobile, tauri::mobile_entry_point)]
pub fn run() {
    tauri::Builder::default()
        .plugin(tauri_plugin_shell::init())
        .invoke_handler(tauri_handler![get_backend_url])
        .run(tauri::generate_context!())
        .expect("error while running tauri application");
}
