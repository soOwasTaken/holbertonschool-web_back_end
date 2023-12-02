const sinon = require("sinon");
const assert = require("chai").assert;
const sendPaymentRequestToApi = require("./4-payment");
const Utils = require("./utils");

describe("sendPaymentRequestToApi with stub", () => {
  it("should call Utils.calculateNumber with specific arguments and stub the result", () => {
    const stub = sinon.stub(Utils, "calculateNumber").returns(10);

    const consoleSpy = sinon.spy(console, "log");

    sendPaymentRequestToApi(100, 20);

    assert(stub.calledWith("SUM", 100, 20));
    assert(consoleSpy.calledWith("The total is: 10"));

    stub.restore();
    consoleSpy.restore();
  });
});
