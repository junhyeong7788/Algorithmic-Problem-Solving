# [level 0] 부분 문자열 이어 붙여 문자열 만들기 - 181911 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/181911) 

### 성능 요약

메모리: 10.1 MB, 시간: 0.04 ms

### 구분

코딩테스트 연습 > 코딩 기초 트레이닝

### 채점결과

정확성: 100.0<br/>합계: 100.0 / 100.0

### 제출 일자

2024년 09월 23일 00:13:48

### 문제 설명

<p>길이가 같은 문자열 배열 <code>my_strings</code>와 이차원 정수 배열 <code>parts</code>가 매개변수로 주어집니다. <code>parts[i]</code>는 [s, e] 형태로, <code>my_string[i]</code>의 인덱스 s부터 인덱스 e까지의 부분 문자열을 의미합니다. 각 <code>my_strings</code>의 원소의 <code>parts</code>에 해당하는 부분 문자열을 순서대로 이어 붙인 문자열을 return 하는 solution 함수를 작성해 주세요.</p>

<hr>

<h5>제한사항</h5>

<ul>
<li>1 ≤ <code>my_strings</code>의 길이 = <code>parts</code>의 길이 ≤ 100</li>
<li>1 ≤ <code>my_strings</code>의 원소의 길이 ≤ 100</li>
<li><code>parts[i]</code>를 [s, e]라 할 때, 다음을 만족합니다.

<ul>
<li>0 ≤ s ≤ e &lt; <code>my_strings[i]</code>의 길이</li>
</ul></li>
</ul>

<hr>

<h5>입출력 예</h5>
<table class="table">
        <thead><tr>
<th>my_strings</th>
<th>parts</th>
<th>result</th>
</tr>
</thead>
        <tbody><tr>
<td>["progressive", "hamburger", "hammer", "ahocorasick"]</td>
<td>[[0, 4], [1, 2], [3, 5], [7, 7]]</td>
<td>"programmers"</td>
</tr>
</tbody>
      </table>
<hr>

<h5>입출력 예 설명</h5>

<p>입출력 예 #1</p>

<ul>
<li>예제 1번의 입력을 보기 좋게 표로 나타내면 다음과 같습니다.</li>
</ul>

|i|my_strings[i]|parts[i]|부분 문자열|
|-|-------------|--------|--------|
|0|"progressive"|[0, 4]|"progr"|
|1|"hamburger"|[1, 2]|"am"|
|2|"hammer"|[3, 5]|"mer"|
|3|"ahocorasick"|[7, 7]|"s"|

<div class="highlight"><pre class="codehilite"><code>각 부분 문자열을 순서대로 이어 붙인 문자열은 "programmers"입니다. 따라서 "programmers"를 return 합니다.
</code></pre></div>

> 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges
---
### 🤔 REMIND
- `zip()` : 여러 개의 반복 가능한 객체를 병렬로 순회할 수 있도록 튜플을 묶어주는 함수
- `enumerate()` : 반복 가능한 객체를 인덱스와 함께 반환하는 함수, 주로 리스트, 튜플, 문자열 등 반복 가능한 객체를 순회할 때 해당 요소와 그에 해당하는 인덱스를 동시에 사용할 수 있게 해줌

### 💻 접근법
인사이트 : enumerate()사용

### 📝 슈도코드
```
def solution (길이가 같은 문자열 배열 my_strings와 2차원 정수 배열 parts를 매개변수로 받는다):
    변수 answer를 빈 문자열로 초기화

    각 인덱스 idx와 값 val에 대해 parts 리스트를 순회:
        - my_strings에서 idx번째 문자열에서 val[0]부터 val[1]까지의 부분 문자열을 추출
        - 추출된 부분 문자열을 answer에 추가

    answer를 반환
```
```python
# 풀이 코드
def solution(my_strings, parts):
    answer = ''
    
    for idx, val in enumerate(parts):
        answer += my_strings[idx][val[0]:val[1]+1]
        
    return answer
```
- `enumerate(parts)`: parts 리스트를 순회하면서 인덱스와 값을 동시에 가져온다. / idx : 현재 순회 중인 문자열의 인덱스를 가리킴, val : 자를 범위 [start, end]를 의미
- `answer += my_strings[idx][val[0]:val[1]+1]`
    - `val[0]과 val[1]`: parts 리스트에서 가져온 시작 인덱스와 끝 인덱스를 의미, 여기서 val[1]+1은 파이썬 슬라이싱에서 끝 인덱스가 포함되지 않기 때문에 범위에 끝 인덱스를 포함시키기 위해 +1을 한다.
    - 문제 : `my_string[0][0:5], my_string[1][1:3], my_string[2][3:6], my_string[3][7:8]`


### 👍 다른 정답 코드
1.
```python
def solution(my_strings, parts):
    answer = ""
    for i, (s, e) in enumerate(parts):
        answer += my_strings[i][s:e+1]
    return answer
```
- 위 풀이 코드를 생략없이 보면 이렇게 볼 수 있다.
2.
```python
def solution(my_strings, parts):
    return ''.join([x[y[0]:y[1]+1] for x,y in zip(my_strings, parts)])
```
- `zip(my_strings, parts)`: 여러 개의 iterable을 병렬로 묶어 튜플로 반환
- my_strings와 parts를 같은 인덱스끼리 묶어서 (x, y)라는 튜플로 만듬
- `x[y[0]:y[1]+1]` : x라는 문자열에서 `y[0]`부터 `y[1] + 1`까지의 부분 문자열을 슬라이싱
