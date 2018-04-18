import ast
from app.views import status


def bytes_to_dict(src):
    return ast.literal_eval(src.decode('utf-8'))


# TODO: testcase naming 및 structure 정의 필요
# TODO: view별로 class화할 수 있는지 research
# TODO: 공통된 부분 decorator 등의 기법으로 제거
def test_status_view_with_success_response(rf):
    """request는 항상 success status code를 리턴한다."""
    request = rf.get('/runners/status')
    response = status(request)
    assert response.status_code == 200


def test_status_view_with_platform_info(rf):
    """request는 platform 정보를 json 형태로 리턴한다."""
    request = rf.get('/runners/status')
    response = status(request)
    info = bytes_to_dict(response.content)
    for key in ['system', 'release', 'version']:
        assert key in info
