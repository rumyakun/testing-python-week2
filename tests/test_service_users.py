from app.services.user_service import register_user


def test_register_user():
    # Given: 사용자의 ID와 얼굴 이미지가 주어짐
    image_path = "images/Aaron_Peirsol/Aaron_Peirsol_0001.jpg"
    user_id = "aaron_peirsol"

    # When: 사용자 등록 기능을 실행
    with open(image_path, "rb") as f:
        image_data = f.read()
        result = register_user(user_id, image_data)

    # Then: 사용자 등록 기능이 성공
    assert result["user_id"] == "aaron_peirsol"
    assert result["registered_at"] is not None
