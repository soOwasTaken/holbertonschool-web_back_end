const chai = require("chai");
const request = require("request");
const expect = chai.expect;

describe("Index page", () => {
    it("should return correct status code", (done) => {
        request("http://localhost:7865", (error, response, body) => {
            expect(response.statusCode).to.equal(200);
            done();
        });
    });
    it("should return 'Welcome to the payment system'", (done) => {
        request("http://localhost:7865", (error, response, body) => {
            expect(body).to.equal("Welcome to the payment system");
            done();
        });
    });
});

describe("Cart page", () => {
  it("should return correct status code and result for a number id", (done) => {
    request("http://localhost:7865/cart/12", (error, response, body) => {
      expect(response.statusCode).to.equal(200);
      expect(body).to.equal("Payment methods for cart 12");
      done();
    });
  });

  it("should return 404 status code for a non-number id", (done) => {
    request("http://localhost:7865/cart/hello", (error, response, body) => {
      expect(response.statusCode).to.equal(404);
      done();
    });
  });

});
