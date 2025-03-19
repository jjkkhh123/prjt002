import sys
import time
from PyQt5.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget, QPushButton, QHBoxLayout
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QFont

# 변수 초기화
antimatter = 10  # 초기 안티매터 양
first_antimatter_dimension = 0  # 초기 1차 안티매터 디멘션 양
second_antimatter_dimension = 0  # 초기 2차 안티매터 디멘션 양
third_antimatter_dimension = 0  # 초기 3차 안티매터 디멘션 양
first_dimension_cost = 10  # 1차 안티매터 디멘션 구입 비용
second_dimension_cost = 100  # 2차 안티매터 디멘션 구입 비용
third_dimension_cost = 100000  # 3차 안티매터 디멘션 구입 비용
first_dimension_multiple = 10  # 1차 안티매터 디멘션 배수
second_dimension_multiple = 1  # 2차 안티매터 디멘션 배수
third_dimension_multiple = 1  # 3차 안티매터 디멘션 배수
first_dimension_count = 0  # 1차 안티매터 디멘션 구입 카운트
second_dimension_count = 0  # 2차 안티매터 디멘션 구입 카운트
third_dimension_count = 0  # 3차 안티매터 디멘션 구입 카운트
tick_speed = 1000  # 초기 틱 스피드 (1초)
tick_speed_multiplier = 1.1  # 틱 스피드 배수
tick_speed_cost = 1000  # 틱 스피드 구입 비용

# 안티매터 증가 함수
def increase_antimatter():
    global antimatter, first_antimatter_dimension, first_dimension_multiple, second_antimatter_dimension, second_dimension_multiple, third_antimatter_dimension, third_dimension_multiple
    antimatter += first_antimatter_dimension * first_dimension_multiple  # 1차 디멘션 배수에 따라 안티매터 증가
    first_antimatter_dimension += second_antimatter_dimension * second_dimension_multiple  # 2차 디멘션 배수에 따라 1차 디멘션 증가
    second_antimatter_dimension += third_antimatter_dimension * third_dimension_multiple  # 3차 디멘션 배수에 따라 2차 디멘션 증가
    label.setText(f"Antimatter: {antimatter:.2e}" if antimatter >= 1000 else f"Antimatter: {antimatter}")  # 안티매터 라벨 업데이트
    tick_speed_label.setText(f"Tick Speed: {1000 / tick_speed:.2e}x" if tick_speed < 1000 else f"Tick Speed: {1000 / tick_speed:.2f}x")  # 틱 스피드 라벨 업데이트
    dimension_label.setText(f"First: {first_antimatter_dimension:.2e}" if first_antimatter_dimension >= 1000 else f"First: {first_antimatter_dimension}")  # 1차 디멘션 라벨 업데이트
    second_dimension_label.setText(f"Second: {second_antimatter_dimension:.2e}" if second_antimatter_dimension >= 1000 else f"Second: {second_antimatter_dimension}")  # 2차 디멘션 라벨 업데이트
    third_dimension_label.setText(f"Third: {third_antimatter_dimension:.2e}" if third_antimatter_dimension >= 1000 else f"Third: {third_antimatter_dimension}")  # 3차 디멘션 라벨 업데이트

# 1차 안티매터 디멘션 증가 함수
def increase_dimension():
    global antimatter, first_antimatter_dimension, first_dimension_cost, first_dimension_multiple, first_dimension_count
    if antimatter >= first_dimension_cost:  # 1차 디멘션 구입 비용이 충분한지 확인
        antimatter -= first_dimension_cost  # 안티매터에서 비용 차감
        first_antimatter_dimension += 1  # 1차 디멘션 증가
        first_dimension_count += 1  # 구입 카운트 증가
        if first_dimension_count == 10:  # 10번째 구입마다
            first_dimension_cost *= 10  # 비용 10배 증가
            first_dimension_multiple *= 2  # 배수 2배 증가
            first_dimension_count = 0  # 카운트 초기화
        label.setText(f"Antimatter: {antimatter:.2e}" if antimatter >= 1000 else f"Antimatter: {antimatter}")  # 안티매터 라벨 업데이트
        dimension_label.setText(f"First: {first_antimatter_dimension:.2e}" if first_antimatter_dimension >= 1000 else f"First: {first_antimatter_dimension}")  # 1차 디멘션 라벨 업데이트
        first_dimension_cost_label.setText(f"Cost: {first_dimension_cost:.2e}" if first_dimension_cost >= 1000 else f"Cost: {first_dimension_cost}")  # 1차 디멘션 비용 라벨 업데이트
        first_dimension_multiple_label.setText(f"Multiple: {first_dimension_multiple:.2e}" if first_dimension_multiple >= 1000 else f"Multiple: {first_dimension_multiple}")  # 1차 디멘션 배수 라벨 업데이트

# 2차 안티매터 디멘션 증가 함수
def increase_second_dimension():
    global antimatter, second_antimatter_dimension, second_dimension_cost, second_dimension_multiple, second_dimension_count
    if antimatter >= second_dimension_cost:  # 2차 디멘션 구입 비용이 충분한지 확인
        antimatter -= second_dimension_cost  # 안티매터에서 비용 차감
        second_antimatter_dimension += 1  # 2차 디멘션 증가
        second_dimension_count += 1  # 구입 카운트 증가
        if second_dimension_count == 10:  # 10번째 구입마다
            second_dimension_cost *= 10  # 비용 10배 증가
            second_dimension_multiple *= 2  # 배수 2배 증가
            second_dimension_count = 0  # 카운트 초기화
        label.setText(f"Antimatter: {antimatter:.2e}" if antimatter >= 1000 else f"Antimatter: {antimatter}")  # 안티매터 라벨 업데이트
        second_dimension_label.setText(f"Second: {second_antimatter_dimension:.2e}" if second_antimatter_dimension >= 1000 else f"Second: {second_antimatter_dimension}")  # 2차 디멘션 라벨 업데이트
        second_dimension_cost_label.setText(f"Cost: {second_dimension_cost:.2e}" if second_dimension_cost >= 1000 else f"Cost: {second_dimension_cost}")  # 2차 디멘션 비용 라벨 업데이트
        second_dimension_multiple_label.setText(f"Multiple: {second_dimension_multiple:.2e}" if second_dimension_multiple >= 1000 else f"Multiple: {second_dimension_multiple}")  # 2차 디멘션 배수 라벨 업데이트

# 3차 안티매터 디멘션 증가 함수
def increase_third_dimension():
    global antimatter, third_antimatter_dimension, third_dimension_cost, third_dimension_multiple, third_dimension_count
    if antimatter >= third_dimension_cost:  # 3차 디멘션 구입 비용이 충분한지 확인
        antimatter -= third_dimension_cost  # 안티매터에서 비용 차감
        third_antimatter_dimension += 1  # 3차 디멘션 증가
        third_dimension_count += 1  # 구입 카운트 증가
        if third_dimension_count == 10:  # 10번째 구입마다
            third_dimension_cost *= 10  # 비용 10배 증가
            third_dimension_multiple *= 2  # 배수 2배 증가
            third_dimension_count = 0  # 카운트 초기화
        label.setText(f"Antimatter: {antimatter:.2e}" if antimatter >= 1000 else f"Antimatter: {antimatter}")  # 안티매터 라벨 업데이트
        third_dimension_label.setText(f"Third: {third_antimatter_dimension:.2e}" if third_antimatter_dimension >= 1000 else f"Third: {third_antimatter_dimension}")  # 3차 디멘션 라벨 업데이트
        third_dimension_cost_label.setText(f"Cost: {third_dimension_cost:.2e}" if third_dimension_cost >= 1000 else f"Cost: {third_dimension_cost}")  # 3차 디멘션 비용 라벨 업데이트
        third_dimension_multiple_label.setText(f"Multiple: {third_dimension_multiple:.2e}" if third_dimension_multiple >= 1000 else f"Multiple: {third_dimension_multiple}")  # 3차 디멘션 배수 라벨 업데이트

# 틱 스피드 증가 함수
def increase_tick_speed():
    global antimatter, tick_speed, tick_speed_cost
    if antimatter >= tick_speed_cost:  # 틱 스피드 구입 비용이 충분한지 확인
        antimatter -= tick_speed_cost  # 안티매터에서 비용 차감
        tick_speed_cost *= 10  # 비용 10배 증가
        tick_speed /= tick_speed_multiplier  # 틱 스피드 1.1배 증가
        timer.setInterval(int(tick_speed))  # 타이머 간격 업데이트
        label.setText(f"Antimatter: {antimatter:.2e}" if antimatter >= 1000 else f"Antimatter: {antimatter}")  # 안티매터 라벨 업데이트
        tick_speed_label.setText(f"Tick Speed: {1000 / tick_speed:.2e}x" if tick_speed < 1000 else f"Tick Speed: {1000 / tick_speed:.2f}x")  # 틱 스피드 라벨 업데이트
        tick_speed_cost_label.setText(f"Tick Speed Cost: {tick_speed_cost:.2e}" if tick_speed_cost >= 1000 else f"Tick Speed Cost: {tick_speed_cost}")  # 틱 스피드 비용 라벨 업데이트

def buy_max_first_dimension():
    global antimatter, first_dimension_cost
    while antimatter >= first_dimension_cost:
        increase_dimension()

def buy_max_second_dimension():
    global antimatter, second_dimension_cost
    while antimatter >= second_dimension_cost:
        increase_second_dimension()

def buy_max_third_dimension():
    global antimatter, third_dimension_cost
    while antimatter >= third_dimension_cost:
        increase_third_dimension()

def buy_max_tick_speed():
    global antimatter, tick_speed_cost
    while antimatter >= tick_speed_cost:
        increase_tick_speed()

# PyQt 애플리케이션 생성
app = QApplication(sys.argv)

# 메인 윈도우 생성
window = QWidget()
window.setWindowTitle("Antimatter Dimensions")  # 윈도우 제목 설정
window.setGeometry(100, 100, 1500, 900)  # 윈도우 위치 및 크기 설정

# 안티매터 값을 표시할 라벨 생성
label = QLabel(f"Antimatter: {antimatter}", window)
label.setFont(QFont("Arial", 24))  # 글씨 크기 24로 설정

# 틱 스피드를 표시할 라벨 생성
tick_speed_label = QLabel(f"Tick Speed: {1000 / tick_speed:.2e}x" if tick_speed < 1000 else f"Tick Speed: {1000 / tick_speed:.2f}x", window)

# 1차 안티매터 디멘션 값을 표시할 라벨 생성
dimension_label = QLabel(f"First: {first_antimatter_dimension}", window)

# 2차 안티매터 디멘션 값을 표시할 라벨 생성
second_dimension_label = QLabel(f"Second: {second_antimatter_dimension}", window)

# 3차 안티매터 디멘션 값을 표시할 라벨 생성
third_dimension_label = QLabel(f"Third: {third_antimatter_dimension}", window)

# 1차 안티매터 디멘션 가격을 표시할 라벨 생성
first_dimension_cost_label = QLabel(f"Cost: {first_dimension_cost}", window)

# 2차 안티매터 디멘션 가격을 표시할 라벨 생성
second_dimension_cost_label = QLabel(f"Cost: {second_dimension_cost}", window)

# 3차 안티매터 디멘션 가격을 표시할 라벨 생성
third_dimension_cost_label = QLabel(f"Cost: {third_dimension_cost}", window)

# 1차 안티매터 디멘션 배수를 표시할 라벨 생성
first_dimension_multiple_label = QLabel(f"Multiple: {first_dimension_multiple}", window)

# 2차 안티매터 디멘션 배수를 표시할 라벨 생성
second_dimension_multiple_label = QLabel(f"Multiple: {second_dimension_multiple}", window)

# 3차 안티매터 디멘션 배수를 표시할 라벨 생성
third_dimension_multiple_label = QLabel(f"Multiple: {third_dimension_multiple}", window)

# 틱 스피드 비용을 표시할 라벨 생성
tick_speed_cost_label = QLabel(f"Tick Speed Cost: {tick_speed_cost}", window)

# 1차 안티매터 디멘션을 증가시키는 버튼 생성
button = QPushButton("Buy", window)
button.clicked.connect(increase_dimension)

# 2차 안티매터 디멘션을 증가시키는 버튼 생성
second_button = QPushButton("Buy", window)
second_button.clicked.connect(increase_second_dimension)

# 3차 안티매터 디멘션을 증가시키는 버튼 생성
third_button = QPushButton("Buy", window)
third_button.clicked.connect(increase_third_dimension)

# 틱 스피드를 증가시키는 버튼 생성
tick_speed_button = QPushButton("Increase Tick Speed", window)
tick_speed_button.clicked.connect(increase_tick_speed)

# 레이아웃 설정
layout = QVBoxLayout()
layout.addWidget(label)
layout.addWidget(tick_speed_label)
first_layout = QHBoxLayout()
first_layout.addWidget(dimension_label)
first_layout.addWidget(first_dimension_cost_label)
first_layout.addWidget(first_dimension_multiple_label)
first_layout.addWidget(button)
max_button = QPushButton("Buy Max", window)
max_button.clicked.connect(buy_max_first_dimension)
first_layout.addWidget(max_button)
layout.addLayout(first_layout)

second_layout = QHBoxLayout()
second_layout.addWidget(second_dimension_label)
second_layout.addWidget(second_dimension_cost_label)
second_layout.addWidget(second_dimension_multiple_label)
second_layout.addWidget(second_button)
max_second_button = QPushButton("Buy Max", window)
max_second_button.clicked.connect(buy_max_second_dimension)
second_layout.addWidget(max_second_button)
layout.addLayout(second_layout)

third_layout = QHBoxLayout()
third_layout.addWidget(third_dimension_label)
third_layout.addWidget(third_dimension_cost_label)
third_layout.addWidget(third_dimension_multiple_label)
third_layout.addWidget(third_button)
max_third_button = QPushButton("Buy Max", window)
max_third_button.clicked.connect(buy_max_third_dimension)
third_layout.addWidget(max_third_button)
layout.addLayout(third_layout)

tick_speed_layout = QHBoxLayout()
tick_speed_layout.addWidget(tick_speed_cost_label)
tick_speed_layout.addWidget(tick_speed_button)
max_tick_speed_button = QPushButton("Buy Max", window)
max_tick_speed_button.clicked.connect(buy_max_tick_speed)
tick_speed_layout.addWidget(max_tick_speed_button)
layout.addLayout(tick_speed_layout)

window.setLayout(layout)

# 매 초마다 increase_antimatter 함수를 호출하는 타이머 설정
timer = QTimer()
timer.timeout.connect(increase_antimatter)
timer.start(tick_speed)

# 윈도우 표시
window.show()

# PyQt 애플리케이션 실행
sys.exit(app.exec_())
