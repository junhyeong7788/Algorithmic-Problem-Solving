# [level 0] n 번째 원소까지 - 181889 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/181889) 

### 성능 요약

메모리: 10.2 MB, 시간: 0.00 ms

### 구분

코딩테스트 연습 > 코딩 기초 트레이닝

### 채점결과

정확성: 100.0<br/>합계: 100.0 / 100.0

### 제출 일자

2024년 09월 14일 17:13:18

### 문제 설명

<p>정수 리스트 <code>num_list</code>와 정수 <code>n</code>이 주어질 때, <code>num_list</code>의 첫 번째 원소부터 <code>n</code> 번째 원소까지의 모든 원소를 담은 리스트를 return하도록 solution 함수를 완성해주세요.</p>

<hr>

<h5>제한사항</h5>

<ul>
<li>2 ≤ <code>num_list</code>의 길이 ≤ 30</li>
<li>1 ≤ <code>num_list</code>의 원소 ≤ 9</li>
<li>1 ≤ <code>n</code> ≤ <code>num_list</code>의 길이
___</li>
</ul>

<h5>입출력 예</h5>
<table class="table">
        <thead><tr>
<th>num_list</th>
<th>n</th>
<th>result</th>
</tr>
</thead>
        <tbody><tr>
<td>[2, 1, 6]</td>
<td>1</td>
<td>[2]</td>
</tr>
<tr>
<td>[5, 2, 1, 7, 5]</td>
<td>3</td>
<td>[5, 2, 1]</td>
</tr>
</tbody>
      </table>
<hr>

<h5>입출력 예 설명</h5>

<p>입출력 예 #1</p>

<ul>
<li>[2, 1, 6]의 첫 번째 원소부터 첫 번째 원소까지의 모든 원소는 [2]입니다.</li>
</ul>

<p>입출력 예 #2</p>

<ul>
<li>[5, 2, 1, 7, 5]의 첫 번째 원소부터 세 번째 원소까지의 모든 원소는 [5, 2, 1]입니다.</li>
</ul>


> 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges
---
### 🤔 REMIND
- 리스트 슬라이싱, enumerate()

### 💻 접근법
인사이트 : 처음에는 다른 정답 코드 1번 처럼 for loop를 사용하여 풀이하려고 하였다.
- 간단하게 리스트 슬라이싱으로 풀 수 있는 문제였다.

### 📝 슈도코드
```
def solution함수 (정수 리스트 num_list, n번째 원소):
    return num_list[첫번째부터 n번째 인덱스까지 리스트 인덱싱]
```
```python
# 풀이 코드
def solution(num_list, n):
    return num_list[0:n] # [:n] 도 가능
```

### 👍 다른 정답 코드
1.
```python
def solution(num_list, n):
    answer = []
    for i in range(n):
        answer.append(num_list[i])
    return answer
```
- `for i in range(n)` : 0부터 n-1까지의 정수를 반환하는 이터레이터
- `answer.append(num_list[i])` : i는 인덱스, num_list의 첫 번째 요소부터 n번째 요소까지 하나씩 answer에 추가됨
2.
```python
def solution(num_list, n):
    return [v for i,v in enumerate(num_list) if i<n]
```
- `enumerate(num_list)` : num_list의 요소들을 인덱스와 함께 반복할 수 있도록 해주는 함수
-  enumerate는 (인덱스, 요소) 형태의 튜플로 반환하여, 여기서 i는 인덱스, v는 num_list의 해당 인덱스에 있는 요소이다.
