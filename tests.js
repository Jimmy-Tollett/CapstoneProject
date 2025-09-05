function checkAsterixLength(messageBytes) {
  // messageBytes: Uint8Array
  if (messageBytes.length < 3) throw new Error("Message too short to contain header");
  const declaredLen = (messageBytes[1] << 8) | messageBytes[2];
  const actualLen = messageBytes.length;
  return declaredLen === actualLen;
}


test('valid message', () => {
  // Example ASTERIX message in hex (same as Python test)
  const hexStr = "15 00 3b c3 1b 7b 6b c1 81 00 00 00 01 00 0c 3d 56 bb dd 19 af fb a3 ad ce 7a fe 12 7a fe 12 17 44 51 f5 14 12 03 f3 05 78 40 7f f6 08 df 51 c7 7a fe 13 04 13 33 db 98";
  const messageBytes = hexStringToUint8Array(hexStr);
  expect(checkAsterixLength(messageBytes)).toBe(true);
});


test('invalid message', () => {
  // Remove a byte to make the length invalid
  const hexStr = "15 00 3b c3 1b 7b 6b c1 81 00 00 00 01 00 0c 3d 56 bb dd 19 af fb a3 ad ce 7a fe 12 7a fe 12 17 44 51 f5 14 12 03 f3 05 78 40 7f f6 08 df 51 c7 7a fe 13 04 13 33 db";
  const messageBytes = hexStringToUint8Array(hexStr);
  expect(checkAsterixLength(messageBytes)).toBe(false);
});

function hexStringToUint8Array(hexStr) {
  const clean = hexStr.replace(/\s+/g, '');
  const arr = new Uint8Array(clean.length / 2);
  for (let i = 0; i < clean.length; i += 2) {
    arr[i / 2] = parseInt(clean.substr(i, 2), 16);
  }
  return arr;
}