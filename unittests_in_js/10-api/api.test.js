const chai = require("chai");
const request = require("request");
const expect = chai.expect;

describe("API Tests", () => {
  // Test for the root endpoint
  describe('Root Endpoint "/"', () => {
    it("should return correct status code and welcome message", (done) => {
      request("http://localhost:7865", (error, response, body) => {
        expect(response.statusCode).to.equal(200);
        expect(body).to.equal("Welcome to the payment system");
        done();
      });
    });
  });

  // Test suite for cart endpoint
  describe('Cart Endpoint "/cart/:id"', () => {
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

  // Test suite for available_payments endpoint
  describe('Available Payments Endpoint "/available_payments"', () => {
    it("should return correct payment methods", (done) => {
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

  // Test suite for POST /login endpoint
  describe('Login Endpoint "POST /login"', () => {
    it("should welcome the user", (done) => {
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
});
