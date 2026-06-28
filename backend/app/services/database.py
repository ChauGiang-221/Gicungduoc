"""
Firebase Firestore service for persistent storage.
"""
import os
from datetime import datetime
from typing import Optional

try:
    import firebase_admin
    from firebase_admin import credentials, firestore

    _firebase_initialized = False

    def _init_firebase():
        global _firebase_initialized
        if _firebase_initialized:
            return
        creds_path = os.getenv("FIREBASE_CREDENTIALS_PATH", "")
        if creds_path and os.path.exists(creds_path):
            cred = credentials.Certificate(creds_path)
            firebase_admin.initialize_app(cred)
        else:
            firebase_admin.initialize_app()
        _firebase_initialized = True

    _init_firebase()

    def get_db():
        return firestore.client()

except ImportError:
    def get_db():
        return None


class DatabaseService:
    def __init__(self):
        self.db = get_db()

    # ===== Conversations =====
    async def save_message(self, user_id: str, conversation_id: str, role: str, content: str, provider: str = "openai"):
        if not self.db:
            return
        doc_ref = self.db.collection("users").document(user_id).collection("conversations").document(conversation_id)
        doc_ref.set({"user_id": user_id, "updated_at": datetime.utcnow().isoformat()}, merge=True)
        messages_ref = doc_ref.collection("messages").document()
        messages_ref.set({
            "role": role,
            "content": content,
            "provider": provider,
            "timestamp": datetime.utcnow().isoformat(),
        })

    async def get_conversations(self, user_id: str, limit: int = 20):
        if not self.db:
            return []
        convs_ref = self.db.collection("users").document(user_id).collection("conversations")
        docs = convs_ref.order_by("updated_at", direction=firestore.Query.DESCENDING).limit(limit).stream()
        return [doc.to_dict() | {"id": doc.id} for doc in docs]

    async def get_messages(self, user_id: str, conversation_id: str, limit: int = 100):
        if not self.db:
            return []
        msgs_ref = (
            self.db.collection("users").document(user_id)
            .collection("conversations").document(conversation_id)
            .collection("messages")
        )
        docs = msgs_ref.order_by("timestamp").limit(limit).stream()
        return [doc.to_dict() for doc in docs]

    async def delete_conversation(self, user_id: str, conversation_id: str):
        if not self.db:
            return
        self.db.collection("users").document(user_id).collection("conversations").document(conversation_id).delete()


db_service = DatabaseService()
