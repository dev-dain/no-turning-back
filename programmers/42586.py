# 08-18

import math

def solution(progresses: list[int], speeds: list[int]) -> list[int]:
  needs = [math.ceil((100 - progress) / speed) for progress, speed in zip(progresses, speeds)]
  release = []
  idx = 0

  for i in range(len(needs)):
    # max로 해서 이전 인덱스부터 지금 인덱스까지 가장 큰 값과 비교
    if i == 0 or max(needs[idx:i]) < needs[i]:
      release.append(1)
      idx = i
      continue
    release[-1] += 1
    
  return release