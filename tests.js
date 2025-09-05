function isValidMessage(message, declaredLength) {
  return message.length === declaredLength;
}

test('valid message', () => {
  const message = "FLIGHT123";
  const declaredLength = 9;
  expect(isValidMessage(message, declaredLength)).toBe(true);
});

test('invalid message', () => {
  const message = "FLIGHT123";
  const declaredLength = 8;
  expect(isValidMessage(message, declaredLength)).toBe(false);
});