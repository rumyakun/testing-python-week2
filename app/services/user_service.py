from datetime import datetime

import cv2
import numpy as np

from app.face.face_db import save_user
from app.face.face_embedding import extract_embedding


def register_user(user_id: str, image_bytes: bytes) -> dict:
    """이미지와 ID로 회원 등록"""
    image_np = np.frombuffer(image_bytes, dtype=np.uint8)
    image = cv2.imdecode(image_np, cv2.IMREAD_COLOR)
    embedding = extract_embedding(image)
    save_user(user_id, embedding)
    return {"user_id": user_id, "registered_at": str(datetime.now())}


def authenticate_user(image_bytes: bytes):
    """이미지로 회원 인증"""
    pass


def get_user(user_id):
    """user_id로 회원 정보 조회"""
    pass


def delete_user(user_id):
    """user_id로 회원 삭제"""
    pass
