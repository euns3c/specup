# specup

python 언어와 Django 프레임워크를 처음 사용해봐서 모든 step이 부족한 점 사과드립니다.

오류가 생기는 부분에 대해서 말씀드리겠습니다.
포인트와 포인트 사용 횟수 칼럼인데요,
views.py에서 points에 UserPointHistory.objects.all().aggregate(Sum('delta'))를 할당했는데 화면에 출력되지 않았습니다.
포인트 사용 횟수는
if UserPointHistory.delta > 0
count()를 사용한다는 것까지는 알았지만 정확한 문장으로 코딩할 수 없었습니다.

비록 문제 1번을 해결하지 못했지만 어설프게나마 python을 접해볼 수 있는 소중한 경험이었습니다. 감사합니다.
