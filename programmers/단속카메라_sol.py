# 카메라 위치를 기준으로 바꿔가며 검증
def solution(routes):
    routes = sorted(routes, key=lambda x: x[1])
    last_camera = -30000

    answer = 0

    for route in routes:
        if last_camera < route[0]:
            answer += 1
            last_camera = route[1]

    return answer

print(solution([[-20,-15], [-14,-5], [-18,-13], [-5,-3]]))
print(solution([[-20,-15], [-14,-5]]))
print(solution([[-20,-15]]))