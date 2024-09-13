# [level 0] n의 배수 고르기 - 120905 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/120905) 

### 성능 요약

메모리: 10.1 MB, 시간: 0.01 ms

### 구분

코딩테스트 연습 > 코딩테스트 입문

### 채점결과

정확성: 100.0<br/>합계: 100.0 / 100.0

### 제출 일자

2024년 09월 14일 00:12:37

### 문제 설명

<p>정수 <code>n</code>과 정수 배열 <code>numlist</code>가 매개변수로 주어질 때, <code>numlist</code>에서 <code>n</code>의 배수가 아닌 수들을 제거한 배열을 return하도록 solution 함수를 완성해주세요.</p>

<hr>

<h5>제한사항</h5>

<ul>
<li>1 ≤ <code>n</code> ≤ 10,000</li>
<li>1 ≤ <code>numlist</code>의 크기 ≤ 100</li>
<li>1 ≤ <code>numlist</code>의 원소 ≤ 100,000</li>
</ul>

<hr>

<h5>입출력 예</h5>
<table class="table">
        <thead><tr>
<th>n</th>
<th>numlist</th>
<th>result</th>
</tr>
</thead>
        <tbody><tr>
<td>3</td>
<td>[4, 5, 6, 7, 8, 9, 10, 11, 12]</td>
<td>[6, 9, 12]</td>
</tr>
<tr>
<td>5</td>
<td>[1, 9, 3, 10, 13, 5]</td>
<td>[10, 5]</td>
</tr>
<tr>
<td>12</td>
<td>[2, 100, 120, 600, 12, 12]</td>
<td>[120, 600, 12, 12]</td>
</tr>
</tbody>
      </table>
<hr>

<h5>입출력 예 설명</h5>

<p>입출력 예 #1</p>

<ul>
<li><code>numlist</code>에서 3의 배수만을 남긴 [6, 9, 12]를 return합니다.</li>
</ul>

<p>입출력 예 #2</p>

<ul>
<li><code>numlist</code>에서 5의 배수만을 남긴 [10, 5]를 return합니다.</li>
</ul>

<p>입출력 예 #3</p>

<ul>
<li><code>numlist</code>에서 12의 배수만을 남긴 [120, 600, 12, 12]를 return합니다.</li>
</ul>


> 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges
---
### 🤔 REMIND
- lambda, filter, list comprehension

### 💻 접근법
인사이트 : [[level 0] 배열 만들기 1 - 181901](https://github.com/junhyeong7788/Python-Problem-Solving/tree/6a548316f6466e450cbbd161d48f6498a89ec936/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4/0/181901.%E2%80%85%EB%B0%B0%EC%97%B4%E2%80%85%EB%A7%8C%EB%93%A4%EA%B8%B0%E2%80%851)
- 해당 문제와 동일하게 풀이하였다.

### 📝 슈도코드
```
def solution함수(매개변수1 n, 매개변수2 numlist를 받는다):
    빈 리스트 answer 선언
    numlist의 각 요소 i에 대해 반복
        만약 i가 n으로 나누어 떨어지면,
             i를 answer 리스트에 추가한다.
    answer리스트를 반환
```
```python
# 풀이 코드 1
def solution(n, numlist):
    answer = []
    for i in numlist:
        if i % n == 0:
            answer.append(i)
    return answer
```
```python
# 풀이 코드 2 - list comprehension
def solution(n, numlist):
    return [i for i in numlist if i % n == 0]
```

### 👍 다른 정답 코드
```python
def solution(n, numlist):
    return list(filter(lambda v: v%n==0, numlist))
```
- `lambda v: v % n == 0`: v라는 변수를 입력 받아서 v % n== 0 인지를 확인하는 조건식 / v가 n으로 나누어떨어지면 True를 반환하고, 그렇지 않으면 False를 반환
- `filter`: 첫 번째 인자로 조건을 평가하는 함수를 받고, 두 번째 인자로 반복 가능한 객체를 받는다. 두 번쨰 인자로 받은 리스트 또는 다른 반복 가능한 객체에서 각 요소를 하나씩 가져와 첫 번째 인자로 받은 함수에 전달 / 해당 함수가 True를 반환하는 경우만 그 값을 선택해서 새로운 객체로 반환
