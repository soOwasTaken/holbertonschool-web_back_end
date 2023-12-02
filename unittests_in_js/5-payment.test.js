const sinon = require("sinon");
const assert = require("chai").assert;
const sendPaymentRequestToApi = require("./5-payment");

describe("sendPaymentRequestToApi with hooks", () => {
  let consoleSpy;

  beforeEach(() => {
    // Set up spy before each test
    consoleSpy = sinon.spy(console, "log");
  });

  afterEach(() => {
    // Restore the spy after each test
    consoleSpy.restore();
  });

  it('should log "The total is: 120" for sendPaymentRequestToApi(100, 20)', () => {
    sendPaymentRequestToApi(100, 20);
    assert(consoleSpy.calledWith("The total is: 120"));
    assert(consoleSpy.calledOnce);
  });

  it('should log "The total is: 20" for sendPaymentRequestToApi(10, 10)', () => {
    sendPaymentRequestToApi(10, 10);
    assert(consoleSpy.calledWith("The total is: 20"));
    assert(consoleSpy.calledOnce);
  });
});
