# [level 0] 배열 원소의 길이 - 120854 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/120854) 

### 성능 요약

메모리: 10.1 MB, 시간: 0.00 ms

### 구분

코딩테스트 연습 > 코딩테스트 입문

### 채점결과

정확성: 100.0<br/>합계: 100.0 / 100.0

### 제출 일자

2024년 09월 27일 00:45:46

### 문제 설명

<p>문자열 배열 <code>strlist</code>가 매개변수로 주어집니다. <code>strlist</code> 각 원소의 길이를 담은 배열을 retrun하도록 solution 함수를 완성해주세요.</p>

<hr>

<h5>제한사항</h5>

<ul>
<li>1 ≤ <code>strlist</code> 원소의 길이 ≤ 100</li>
<li><code>strlist</code>는 알파벳 소문자, 대문자, 특수문자로 구성되어 있습니다.</li>
</ul>

<hr>

<h5>입출력 예</h5>
<table class="table">
        <thead><tr>
<th>strlist</th>
<th>result</th>
</tr>
</thead>
        <tbody><tr>
<td>["We", "are", "the", "world!"]</td>
<td>[2, 3, 3, 6]</td>
</tr>
<tr>
<td>["I", "Love", "Programmers."]</td>
<td>[1, 4, 12]</td>
</tr>
</tbody>
      </table>
<hr>

<h5>입출력 예 설명</h5>

<p>입출력 예 #1</p>

<ul>
<li>["We", "are", "the", "world!"]의 각 원소의 길이인 [2, 3, 3, 6]을 return합니다.</li>
</ul>

<p>입출력 예 #2</p>

<ul>
<li>["I", "Love", "Programmers."]의 각 원소의 길이인 [1, 4, 12]을 return합니다.</li>
</ul>


> 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges
---
### 🤔 REMIND
- `len()` : 주어진 입력의 길이나 요소의 개수를 반환, 이 함수는 **문자열, 리스트, 튜플, 딕셔너리, 세트** 등 다양한 컬렉션 유형에 사용 가능

### 💻 접근법
인사이트 : 
- 1번 풀이 : for loop로 strlist 내 문자열을 순회하고 `len()` 함수로 각 요소의 문자열 개수를 센다.
- 2번 풀이 :  리스트 컴프리헨션으로 리스트 생성 후 반환

### 📝 슈도코드
```
def solution(문자열 배열 strlist을 매개변수로 받는다):
    answer 리스트 변수 선언
    for strlist의 요소를 순회:
        answer 변수에 문자열 i의 길이를 추가한다.
    return answer 리스트 변수를 반환
```
```python
# 풀이 코드 1
def solution(strlist):
    answer = []
    for i in strlist:
        answer.append(len(i))
    return answer
```
```python
# 풀이코드 2
def solution(strlist):
    return [len(i) for i in strlist] 
```

### 👍 다른 정답 코드
1.
```python
def solution(strlist):
    return list(map(len, strlist))
```
- `map(len, strlist)`: strlist의 각 요소(문자열)에 len함수를 적용
    - 기본 형태 : `map(function, iterable)` = `(각 요소에 적용될 함수, 함수가 적용될 반복 가능한 데이터 구조)`
