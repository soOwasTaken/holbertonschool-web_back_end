const expect = require("chai").expect;
const calculateNumber = require("./2-calcul_chai");

describe("calculateNumber with Chai", () => {
  describe("SUM", () => {
    it("should return the rounded sum of two numbers", () => {
      expect(calculateNumber("SUM", 1.4, 4.5)).to.equal(6);
    });
  });

  describe("SUBTRACT", () => {
    it("should return the rounded difference of two numbers", () => {
      expect(calculateNumber("SUBTRACT", 1.4, 4.5)).to.equal(-4);
    });
  });

  describe("DIVIDE", () => {
    it("should return the rounded division of two numbers", () => {
      expect(calculateNumber("DIVIDE", 1.4, 4.5)).to.be.closeTo(0.2, 0.1);
    });

    it("should return Error when dividing by 0", () => {
      expect(calculateNumber("DIVIDE", 1.4, 0)).to.equal("Error");
    });
  });
});
