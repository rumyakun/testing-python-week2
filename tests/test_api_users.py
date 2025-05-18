def test_register_user_api(client):
    # Given: 사용자의 ID와 얼굴 이미지가 주어짐
    # Given: API 테스트 클라이언트가 fixture로 제공됨
    image_path = "images/Aaron_Peirsol/Aaron_Peirsol_0001.jpg"
    user_id = "aaron_peirsol"

    # When: 사용자 등록 API (POST /users/register)를 호출
    with open(image_path, "rb") as img_file:
        response = client.post(
            "/users/register",
            data={"user_id": user_id},
            files={"image": ("user1.jpg", img_file, "image/jpeg")},
        )

    # Then: 사용자 등록 기능이 성공(200)
    # Then: 응답 내용은 등록된 사용자 ID 및 등록 시각이 포함
    assert response.status_code == 200
    data = response.json()
    assert data["user_id"] == user_id
    assert data["registered_at"] is not None
