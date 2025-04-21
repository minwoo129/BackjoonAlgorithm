function solution(expressions) {
  // 1) 파싱
  const exprs = expressions.map(expr => {
    const [A, op, B, , C] = expr.split(" ");
    return { A, op, B, C };
  });

  // 숫자 문자열 s가 진법 b에서 유효한지 검사
  function isValidNumber(s, b) {
    return [...s].every(ch => {
      const d = Number(ch);
      return !isNaN(d) && d < b;
    });
  }

  // 2) 진법 후보 추리기
  const candidateBases = [];
  for (let b = 2; b <= 9; b++) {
    // A, B 자릿값 유효성 검사
    if (exprs.some(({ A, B }) => !isValidNumber(A, b) || !isValidNumber(B, b)))
      continue;

    // C가 지워지지 않은 식들에 대해 연산 결과 일치 여부 검사
    let ok = true;
    for (const { A, op, B, C } of exprs) {
      if (C === "X") continue;
      const a = parseInt(A, b);
      const c = parseInt(B, b);
      const r = op === "+" ? a + c : a - c;
      if (r < 0 || r.toString(b) !== C) {
        ok = false;
        break;
      }
    }
    if (ok) candidateBases.push(b);
  }

  // 3) 지워진 결과 채우기
  const result = [];
  for (const { A, op, B, C } of exprs) {
    if (C !== "X") continue;

    // 각 후보 진법에서 연산 결과 문자열 구하기
    const answers = new Set();
    for (const b of candidateBases) {
      const a = parseInt(A, b);
      const c = parseInt(B, b);
      const r = op === "+" ? a + c : a - c;
      answers.add(r.toString(b));
    }

    // 유일하다면 그 값, 아니면 "?"
    const fill = answers.size === 1 ? [...answers][0] : "?";
    result.push(`${A} ${op} ${B} = ${fill}`);
  }

  return result;
}