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

describe("/available_payments endpoint", () => {
  it("should return the correct payment methods object", (done) => {
    request(
      "http://localhost:7865/available_payments",
      (error, response, body) => {
        expect(response.statusCode).to.equal(200);
        expect(JSON.parse(body)).to.deep.equal({
          payment_methods: {
            credit_cards: true,
            paypal: false,
          },
        });
        done();
      }
    );
  });
});

describe("/login endpoint", () => {
  it("should return the welcome message for a user", (done) => {
    const options = {
      url: "http://localhost:7865/login",
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ userName: "Betty" }),
    };

    request(options, (error, response, body) => {
      expect(response.statusCode).to.equal(200);
      expect(body).to.equal("Welcome Betty");
      done();
    });
  });
});
