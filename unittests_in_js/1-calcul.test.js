const assert = require("assert");
const calculateNumber = require("./1-calcul");

describe("calculateNumber", () => {
  describe("SUM", () => {
    it("should return the rounded sum of two numbers", () => {
      assert.strictEqual(calculateNumber("SUM", 1.4, 4.5), 6);
    });
  });

  describe("SUBTRACT", () => {
    it("should return the rounded difference of two numbers", () => {
      assert.strictEqual(calculateNumber("SUBTRACT", 1.4, 4.5), -4);
    });
  });

  describe("DIVIDE", () => {
    it("should return the rounded division of two numbers", () => {
      assert.strictEqual(calculateNumber("DIVIDE", 1.4, 4.5), 0.2);
    });

    it("should return Error when dividing by 0", () => {
      assert.strictEqual(calculateNumber("DIVIDE", 1.4, 0), "Error");
    });
  });
});
